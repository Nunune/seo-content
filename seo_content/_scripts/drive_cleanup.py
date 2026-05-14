"""
drive_cleanup.py — Xóa file trùng tên trong Google Drive folder.
Với mỗi nhóm file trùng tên: giữ bản MỚI NHẤT (modifiedTime), xóa các bản cũ hơn.

Usage: python drive_cleanup.py [--dry-run]
"""
import sys, os, json, argparse
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/drive.file']
BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDS_DIR   = os.path.join(os.path.dirname(BASE_DIR), 'credentials')
TOKEN_FILE  = os.path.join(CREDS_DIR, 'drive_token.json')
PROFILE     = os.path.join(BASE_DIR, 'profiles', 'default.json')


def get_creds():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return creds


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--dry-run', action='store_true', help='Chỉ xem, không xóa')
    args = p.parse_args()

    with open(PROFILE, encoding='utf-8') as f:
        folder_id = json.load(f).get('drive_folder_id', '').strip()
    if not folder_id:
        print('[ERROR] Chưa có drive_folder_id trong profiles/default.json')
        sys.exit(1)

    service = build('drive', 'v3', credentials=get_creds())

    # Lấy tất cả file trong folder (drive.file scope chỉ trả file do app tạo)
    all_files = []
    page_token = None
    while True:
        resp = service.files().list(
            q=f"'{folder_id}' in parents and trashed=false",
            fields='nextPageToken, files(id, name, modifiedTime, size)',
            pageSize=100,
            pageToken=page_token
        ).execute()
        all_files.extend(resp.get('files', []))
        page_token = resp.get('nextPageToken')
        if not page_token:
            break

    # Nhóm theo tên
    from collections import defaultdict
    groups = defaultdict(list)
    for f in all_files:
        groups[f['name']].append(f)

    total_deleted = 0
    total_kept = 0

    print(f'\n{"=" * 55}')
    print(f'  DRIVE CLEANUP — folder: {folder_id[:20]}...')
    print(f'  Mode: {"DRY RUN (khong xoa)" if args.dry_run else "THUC TE (se xoa)"}')
    print(f'{"=" * 55}\n')

    for name, files in sorted(groups.items()):
        if len(files) == 1:
            total_kept += 1
            continue

        # Sắp xếp: mới nhất đầu tiên
        files.sort(key=lambda x: x.get('modifiedTime', ''), reverse=True)
        keep = files[0]
        dupes = files[1:]

        size_kb = int(keep.get('size', 0)) // 1024
        print(f'[GIU] {name}  ({size_kb}KB, {keep["modifiedTime"][:10]})')

        for d in dupes:
            d_kb = int(d.get('size', 0)) // 1024
            if args.dry_run:
                print(f'  [XOA-DRY] {d["id"]}  ({d_kb}KB, {d["modifiedTime"][:10]})')
            else:
                service.files().delete(fileId=d['id']).execute()
                print(f'  [XOA] {d["id"]}  ({d_kb}KB, {d["modifiedTime"][:10]})')
            total_deleted += 1

        total_kept += 1

    print(f'\n{"=" * 55}')
    print(f'  Ket qua: giu {total_kept} file | xoa {total_deleted} ban trung')
    if args.dry_run:
        print('  (Chay lai khong co --dry-run de xoa that)')
    print(f'{"=" * 55}\n')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
