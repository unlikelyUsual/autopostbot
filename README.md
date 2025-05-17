# 📲 Reddit to Instagram Auto Uploader

A Python application that automatically fetches top video posts from specified subreddits, downloads the videos (and merges audio if needed), and prepares them for upload to Instagram. Perfect for meme pages, content curators, or digital marketers looking to automate content flow.

---

## 🚀 Features

- ✅ Fetch top posts from multiple subreddits
- ✅ Filter and download only video posts (Reddit-hosted)
- ✅ Handle Reddit's separate video/audio stream architecture
- ✅ Sanitize filenames for cross-platform compatibility
- ✅ Scheduled automation-ready (cron, Task Scheduler, etc.)
- 📦 Upload-ready for Instagram via [instagrapi](https://github.com/adw0rd/instagrapi)

---

## 🧰 Tech Stack

- Python 3.8+
- `praw` – Reddit API Wrapper
- `requests` – HTTP client for downloading media
- `ffmpeg` – To merge separate video and audio streams
- (Optional) `instagrapi` – For uploading to Instagram

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/reddit-to-instagram.git
cd reddit-to-instagram
```
