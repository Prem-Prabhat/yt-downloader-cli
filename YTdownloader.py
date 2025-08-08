#!/usr/bin/env python3
"""
YouTube Playlist Downloader CLI Tool
====================================

⚠ Disclaimer: This tool is intended for downloading videos you own the rights to
or have permission to download. The developer is not responsible for misuse.

Author: PREM PRABHAT
License: MIT
"""

import os
import time
import yt_dlp
import argparse
import winsound
from concurrent.futures import ThreadPoolExecutor

MAX_RETRIES = 3
RETRY_WAIT = 5

# =========================
# Progress display function
# =========================
def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '').strip()
        speed = d.get('speed')
        eta = d.get('eta')

        speed_str = f"{speed / (1024 * 1024):.2f} MB/s" if speed else "Calculating..."
        eta_str = time.strftime("%H:%M:%S", time.gmtime(eta)) if eta else "Calculating..."

        print(f"\r📥 {percent} | {speed_str} | ETA: {eta_str}", end='', flush=True)

    elif d['status'] == 'finished':
        print(f"\n✅ Download finished: {d['filename']}\n")

# =========================
# Post-processing delay
# =========================
def postprocessor_hook(d):
    if d['status'] == 'finished':
        time.sleep(2)  # small pause after merging

# =========================
# Extract playlist URLs safely
# =========================
def get_playlist_video_urls(playlist_url):
    ydl_opts = {'extract_flat': True, 'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        return [f"https://www.youtube.com/watch?v={e['id']}" for e in info['entries'] if e.get('id')]

# =========================
# Download single video
# =========================
def download_video(video_url, output_folder, log_file):
    retries = 0
    while retries < MAX_RETRIES:
        try:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
                'outtmpl': os.path.join(output_folder, '%(playlist_index)s - %(title)s.%(ext)s'),
                'restrictfilenames': True,
                'noprogress': False,
                'progress_hooks': [progress_hook],
                'postprocessor_hooks': [postprocessor_hook],
                'noplaylist': True,
                'nocheckcertificate': True,
                'nooverwrites': False,
                'ignoreerrors': True,
                'nopart': True,
                'concurrent_fragment_downloads': 3,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                result = ydl.download([video_url])

            with open(log_file, "a", encoding="utf-8") as log:
                log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {video_url} - SUCCESS\n")
            return
        except PermissionError as e:
            if "WinError 32" in str(e):
                retries += 1
                print(f"⚠ File lock detected. Retrying in {RETRY_WAIT} seconds... ({retries}/{MAX_RETRIES})")
                time.sleep(RETRY_WAIT)
            else:
                raise
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {video_url} - FAILED\n")

# =========================
# Main function
# =========================
def main():
    parser = argparse.ArgumentParser(description="YouTube Playlist Downloader CLI Tool")
    parser.add_argument("--url", required=True, help="YouTube playlist or video URL")
    parser.add_argument("--folder", default="Downloaded_Lectures", help="Output folder for downloads")
    parser.add_argument("--threads", type=int, default=1, help="Number of concurrent downloads (max 3 recommended)")
    parser.add_argument("--beep", action="store_true", help="Play sound after completion")
    args = parser.parse_args()

    print("\n⚠ DISCLAIMER: Use this tool only for videos you have rights to.")
    print("The developer is not responsible for misuse.\n")

    os.makedirs(args.folder, exist_ok=True)
    log_file = os.path.join(args.folder, "download_log.txt")

    print("🔍 Fetching video list...")
    urls = get_playlist_video_urls(args.url) if "playlist" in args.url else [args.url]
    print(f"📜 Found {len(urls)} videos.\n")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for video_url in urls:
            executor.submit(download_video, video_url, args.folder, log_file)

    print("\n🎯 All downloads completed!")
    if args.beep:
        winsound.Beep(1000, 500)

if __name__ == "__main__":
    main()
