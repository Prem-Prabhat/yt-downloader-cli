# 🎥 YouTube Playlist Downloader CLI Tool

[![GitHub Release](https://img.shields.io/github/v/release/Prem-Prabhat/yt-downloader-cli?style=flat-square)](https://github.com/Prem-Prabhat/yt-downloader-cli/releases) &nbsp; [![Downloads](https://img.shields.io/github/downloads/Prem-Prabhat/yt-downloader-cli/total?style=flat-square)](https://github.com/Prem-Prabhat/yt-downloader-cli/releases) &nbsp; [![License](https://img.shields.io/github/license/Prem-Prabhat/yt-downloader-cli?style=flat-square)](https://github.com/Prem-Prabhat/yt-downloader-cli/blob/main/LICENSE) &nbsp; [![Stars](https://img.shields.io/github/stars/Prem-Prabhat/yt-downloader-cli?style=flat-square)](https://github.com/Prem-Prabhat/yt-downloader-cli/stargazers) &nbsp; [![Issues](https://img.shields.io/github/issues/Prem-Prabhat/yt-downloader-cli?style=flat-square)](https://github.com/Prem-Prabhat/yt-downloader-cli/issues)

---

A simple yet powerful **command-line tool** to download YouTube playlists or single videos with handy features:

✅ Logging, ✅ Concurrent downloads, ✅ Safe filenames, ✅ Progress tracking.

---

## ⚠️ Disclaimer

This tool is intended **only** for downloading videos you **own the rights to** or have **explicit permission** to download.

The developer is **not responsible** for any misuse of this tool or violations of YouTube's Terms of Service.

**Please use this tool responsibly, ethically, and in compliance with applicable laws.**

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

### 1️⃣ Clone this repository
```bash
git clone https://github.com/Prem-Prabhat/yt-downloader-cli
cd yt-downloader-cli
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🛠️ Usage

### 1️⃣ Download a Playlist
```bash
python YTdownloader.py --url "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```

### 2️⃣ Download a Single Video
```bash
python YTdownloader.py --url "https://www.youtube.com/watch?v=VIDEO_ID"
```

### 3️⃣ Specify an Output Folder
```bash
python YTdownloader.py --url "PLAYLIST_OR_VIDEO_URL" --folder "MyDownloads"
```

### 4️⃣ Multi-threaded Downloads (Max 3 Recommended)
```bash
python YTdownloader.py --url "PLAYLIST_URL" --threads 3
```

### 5️⃣ Play a Beep After Completion
```bash
python YTdownloader.py --url "PLAYLIST_URL" --beep
```

---

## 📄 Command-line Arguments

| Argument | Description |
|----------|-------------|
| `--url` | (Required) YouTube playlist or single video URL. |
| `--folder` | Output folder (default: Downloaded_Lectures). |
| `--threads` | Number of concurrent downloads (default: 1, max recommended: 3). |
| `--beep` | Play a beep when all downloads are complete. |

---

## 🖥️ Example Run

### Linux/MacOS
```bash
python YTdownloader.py --url "https://www.youtube.com/playlist?list=PL12345" --folder "Lectures" --threads 2 --beep
```

### Windows (.exe)
```bash
ytplaylist-downloader.exe --url "https://www.youtube.com/playlist?list=PL12345" --folder "Lectures" --threads 2 --beep
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

---

## 📋 Requirements

- **Python 3.8+**

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## 📦 Packaging for Public Release (Windows)

Create a standalone .exe file:

```bash
pip install pyinstaller
pyinstaller --onefile YTdownloader.py --name ytplaylist-downloader
```

The executable will be available in the `dist` folder.

To add an icon:
```bash
pyinstaller --onefile --icon=icon.ico YTdownloader.py --name ytplaylist-downloader
```

---

## 🤝 Contributing

Contributions are welcome!

1. **Fork the repo**

2. **Create your feature branch:**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Commit changes:**
   ```bash
   git commit -m "Add AmazingFeature"
   ```

4. **Push to branch:**
   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open a Pull Request**

For bugs or feature requests, please [open an issue](https://github.com/Prem-Prabhat/yt-downloader-cli/issues).

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Prem Prabhat**

- **GitHub:** [@prem-prabhat](https://github.com/prem-prabhat)
- **LinkedIn:** [Prem Prabhat](https://linkedin.com/in/prem-prabhat)
- **X:** [@prem_prabhat](https://x.com/prem_prabhat)

💌 Feedback and suggestions are welcome!