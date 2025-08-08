# 🎥 YouTube Playlist Downloader CLI Tool

![Python version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=flat-square)

![License](https://img.shields.io/github/license/prem-prabhat/youtube-playlist-downloader?style=flat-square)

![Stars](https://img.shields.io/github/stars/prem-prabhat/youtube-playlist-downloader?style=flat-square)

![Issues](https://img.shields.io/github/issues/prem-prabhat/youtube-playlist-downloader?style=flat-square)

---

A simple yet powerful **command-line tool** to download YouTube playlists or single videos with handy features:

✅ Logging, ✅ Concurrent downloads, ✅ Safe filenames, ✅ Progress tracking.

---

## ⚠️ Disclaimer

This tool is intended **only** for downloading videos you **own the rights to** or have **explicit permission** to download.

The developer is **not responsible** for any misuse of this tool or violations of YouTube's Terms of Service.

**Please use this tool responsibly and ethically.**

---

## ✨ Features

- 📜 **Playlist Support** — Download all videos from a playlist at once.
- ⏳ **Progress Display** — Shows download percentage, speed, and ETA for each video.
- 🔄 **Retry System** — Automatically retries failed downloads up to 3 times.
- 📝 **Download Log** — Saves detailed logs for all download attempts.
- 🛡️ **Safe Filenames** — Automatically sanitizes video titles.
- ⚡ **Multi-threaded Downloads** — Download multiple videos in parallel.
- 🔔 **Optional Beep** — Play a sound notification when all downloads are complete.

---

## 📦 Installation

```bash
# 1️⃣ Clone this repository
git clone https://github.com/prem-prabhat/youtube-playlist-downloader.git
cd youtube-playlist-downloader

# 2️⃣ Install dependencies
pip install -r requirements.txt
```

## 🛠️ Usage

### 1️⃣ Download a Playlist

```bash
python main.py --url "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```

### 2️⃣ Download a Single Video

```bash
python main.py --url "https://www.youtube.com/watch?v=VIDEO_ID"
```

### 3️⃣ Specify an Output Folder

```bash
python main.py --url "PLAYLIST_OR_VIDEO_URL" --folder "MyDownloads"
```

### 4️⃣ Multi-threaded Downloads (Max 3 Recommended)

```bash
python main.py --url "PLAYLIST_URL" --threads 3
```

### 5️⃣ Play a Beep After Completion

```bash
python main.py --url "PLAYLIST_URL" --beep
```

## 📄 Command-line Arguments

| Argument | Description |
| --- | --- |
| --url | (Required) YouTube playlist or single video URL. |
| --folder | Output folder (default: Downloaded_Lectures). |
| --threads | Number of concurrent downloads (default: 1, max recommended: 3). |
| --beep | Play a beep when all downloads are complete. |

## 🖥️ Example Run

```bash
python main.py --url "https://www.youtube.com/playlist?list=PL12345" --folder "Lectures" --threads 2 --beep
```

### Example Output:

```
📜 Found 10 videos in the playlist.

[1/10] Downloading: 01 - My First Lecture.mp4
📥 25.3% | 2.35 MB/s | ETA: 00:23
✅ Download finished: 01 - My First Lecture.mp4

[2/10] Downloading: 02 - The Second Topic.mp4
...

🎯 All downloads completed!
```

## 📋 Requirements

Python 3.8+

Install dependencies from requirements.txt:

```
yt-dlp
colorama
```

## 📦 Packaging for Public Release (Windows)

Create a standalone .exe file:

```bash
pip install pyinstaller
pyinstaller --onefile main.py --name ytplaylist-downloader
```

The executable will be generated in the dist folder.

## 🤝 Contributing

Contributions are welcome!

- Fork the repo
- Create your feature branch:
    
    ```bash
    git checkout -b feature/AmazingFeaturegit checkout -b feature/AmazingFeature
    ```
    
- Commit changes:
    
    ```bash
    git commit -m "Add AmazingFeature"git commit -m "Add AmazingFeature"
    ```
    
- Push to branch:
    
    ```bash
    git push origin feature/AmazingFeaturegit push origin feature/AmazingFeature
    ```
    
- Open a Pull Request

For bugs or feature requests, please open an issue.

## 📜 License

This project is licensed under the **MIT License** — see the [`LICENSE`](LICENSE) file for details.

## 👨‍💻 Author

**Prem Prabhat**

- GitHub: [@prem-prabhat](https://github.com/prem-prabhat)
- LinkedIn: [Prem Prabhat](https://www.linkedin.com/in/your-linkedin-profile/)
- X: [@prem_prabhat](https://x.com/prem_prabhat)

💌 Feedback and suggestions are welcome!
