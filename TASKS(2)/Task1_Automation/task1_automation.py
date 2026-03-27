import argparse
import os
import re
import shutil
import sys

import requests
from bs4 import BeautifulSoup


def move_jpg_files(src_dir: str, dst_dir: str):
    if not os.path.isdir(src_dir):
        raise FileNotFoundError(f"Source folder not found: {src_dir}")
    os.makedirs(dst_dir, exist_ok=True)

    moved = 0
    for fname in os.listdir(src_dir):
        if fname.lower().endswith('.jpg') or fname.lower().endswith('.jpeg'):
            src_path = os.path.join(src_dir, fname)
            dst_path = os.path.join(dst_dir, fname)
            shutil.move(src_path, dst_path)
            moved += 1
    return moved


def extract_email_addresses(src_txt: str, dst_txt: str):
    if not os.path.isfile(src_txt):
        raise FileNotFoundError(f"Source text file not found: {src_txt}")

    with open(src_txt, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    emails = sorted(set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)))

    with open(dst_txt, 'w', encoding='utf-8') as out:
        out.write('\n'.join(emails))

    return emails


def scrape_webpage_title(url: str):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string.strip() if soup.title and soup.title.string else 'NO TITLE FOUND'
    return title


def main():
    parser = argparse.ArgumentParser(description='Task 1: Python automation script collection')
    sub = parser.add_subparsers(dest='command')

    p_move = sub.add_parser('move-jpg', help='Move all JPG/JPEG files from source to destination')
    p_move.add_argument('src', help='Source folder path')
    p_move.add_argument('dst', help='Destination folder path')

    p_email = sub.add_parser('extract-emails', help='Extract email addresses from a text file')
    p_email.add_argument('src', help='Source .txt file path')
    p_email.add_argument('dst', help='Destination .txt file path for extracted email addresses')

    p_scrape = sub.add_parser('scrape-title', help='Scrape and print page title from a URL')
    p_scrape.add_argument('url', help='URL to scrape')

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    try:
        if args.command == 'move-jpg':
            moved = move_jpg_files(args.src, args.dst)
            print(f"Moved {moved} JPG/JPEG files from '{args.src}' to '{args.dst}'")
        elif args.command == 'extract-emails':
            emails = extract_email_addresses(args.src, args.dst)
            print(f"Extracted {len(emails)} unique email(s) into '{args.dst}'")
        elif args.command == 'scrape-title':
            title = scrape_webpage_title(args.url)
            print(f"Title: {title}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
