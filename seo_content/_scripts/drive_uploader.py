"""
drive_uploader.py — Upload .docx to Google Drive

Mặc định dùng OAuth2 (tài khoản Google cá nhân):
  - Lần đầu: mở browser xác thực → lưu token vào credentials/drive_token.json
  - Các lần sau: dùng token đã lưu, tự refresh khi hết hạn

Usage:
  python drive_uploader.py <file_path> [options]

Options:
  --folder-id ID    Google Drive folder ID (mặc định: đọc từ profiles/default.json)
  --convert         Convert sang Google Docs (chỉnh sửa được trực tiếp trên browser)
  --profile path    Path đến default.json (default: seo_content/profiles/default.json)

Setup một lần:
  1. Cloud Console → APIs & Services → Credentials
  2. + Create Credentials → OAuth 2.0 Client ID → Desktop App
  3. Download JSON → lưu vào: credentials/oauth_client.json
  4. Lần đầu chạy script → browser mở → đăng nhập Google → xác nhận quyền
  5. Token tự lưu vào: credentials/drive_token.json (các lần sau không cần browser)
"""

import sys, os, json, argparse
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/drive.file']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # seo_content/
CREDS_DIR = os.path.join(os.path.dirname(BASE_DIR), 'credentials')
OAUTH_CLIENT = os.path.join(CREDS_DIR, 'oauth_client.json')
TOKEN_FILE   = os.path.join(CREDS_DIR, 'drive_token.json')
DEFAULT_PROFILE = os.path.join(BASE_DIR, 'profiles', 'default.json')

DOCX_MIME = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
GDOC_MIME = 'application/vnd.google-apps.document'


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('file_path', help='Path to .docx file to upload')
    p.add_argument('--folder-id', default=None)
    p.add_argument('--convert', action='store_true', help='Convert to Google Docs')
    p.add_argument('--profile', default=DEFAULT_PROFILE)
    return p.parse_args()


def get_folder_id(args):
    if args.folder_id:
        return args.folder_id
    if os.path.exists(args.profile):
        with open(args.profile, encoding='utf-8') as f:
            profile = json.load(f)
        fid = profile.get('drive_folder_id', '').strip()
        if fid:
            return fid
    return None


def get_credentials():
    creds = None

    # Load saved token if exists
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # Refresh or re-authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(OAUTH_CLIENT):
                print(f'[ERROR] OAuth client not found: {OAUTH_CLIENT}')
                print()
                print('Setup một lần:')
                print('  1. Mở: https://console.cloud.google.com/apis/credentials')
                print('  2. + Create Credentials → OAuth 2.0 Client ID → Desktop App')
                print('  3. Download JSON → lưu vào:', OAUTH_CLIENT)
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(OAUTH_CLIENT, SCOPES)
            print('\n[AUTH] Trình duyệt sẽ mở để xác thực Google Drive...')
            print('[AUTH] Nếu trình duyệt không tự mở, copy URL bên dưới và dán vào browser.')
            print('[AUTH] Sau khi đăng nhập xong, quay lại đây — script tiếp tục tự động.\n')
            creds = flow.run_local_server(port=8080, open_browser=True, timeout_seconds=300)

        # Save token for next runs
        os.makedirs(CREDS_DIR, exist_ok=True)
        with open(TOKEN_FILE, 'w') as f:
            f.write(creds.to_json())
        print(f'[OK] Token lưu tại: {TOKEN_FILE}')

    return creds


def upload(file_path, folder_id, convert, creds):
    service = build('drive', 'v3', credentials=creds)

    file_name = os.path.basename(file_path)
    if convert:
        file_name = os.path.splitext(file_name)[0]

    metadata = {'name': file_name}
    if folder_id:
        metadata['parents'] = [folder_id]
    if convert:
        metadata['mimeType'] = GDOC_MIME

    media = MediaFileUpload(file_path, mimetype=DOCX_MIME, resumable=True)

    print(f'[→] Uploading: {os.path.basename(file_path)}')
    if folder_id:
        print(f'[→] Folder: https://drive.google.com/drive/folders/{folder_id}')

    result = service.files().create(
        body=metadata,
        media_body=media,
        fields='id, name, webViewLink'
    ).execute()

    file_id = result['id']
    name    = result['name']
    link    = result.get('webViewLink', f'https://drive.google.com/file/d/{file_id}/view')

    # Anyone with link can view
    service.permissions().create(
        fileId=file_id,
        body={'role': 'reader', 'type': 'anyone'}
    ).execute()

    size_kb = os.path.getsize(file_path) // 1024
    fmt = 'Google Docs' if convert else '.docx'
    print(f'[OK] Uploaded ({fmt}): {name} — {size_kb}KB')
    print(f'[OK] Link: {link}')
    return link


def main():
    args = parse_args()

    if not os.path.exists(args.file_path):
        print(f'[ERROR] File not found: {args.file_path}')
        sys.exit(1)

    folder_id = get_folder_id(args)
    if not folder_id:
        print('[WARN] Chưa có folder_id — file upload vào My Drive root.')
        print('  → Thêm "drive_folder_id" vào seo_content/profiles/default.json')

    creds = get_credentials()
    link = upload(args.file_path, folder_id, args.convert, creds)
    print(link)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
