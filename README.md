<div align="center">

# 🛡️ Anti-AI Detection Guardian Bot

**The Ultimate Production-Grade Anti-AI Evasion Bot for Telegram**  
*Strip synthetic signatures, VAE latent watermarks, and neural acoustic hashes from Videos & Images in real-time.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Pyrogram](https://img.shields.io/badge/Pyrogram-v2.0-orange.svg?style=for-the-badge&logo=telegram)](https://docs.pyrogram.org/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-6.0%2B-green.svg?style=for-the-badge&logo=ffmpeg)](https://ffmpeg.org/)
[![ExifTool](https://img.shields.io/badge/ExifTool-12.0%2B-red.svg?style=for-the-badge)](https://exiftool.org/)
[![Team Inflex](https://img.shields.io/badge/Author-Team%20Inflex-purple.svg?style=for-the-badge)](https://github.com/TeamInflex)

</div>

---

## 📌 Overview

Modern AI detection systems (e.g. **Hive Moderation, Sightengine, Illuminarty, WasItAI, FakeCatcher, ElevenLabs Speech Classifier**) don't just rely on text metadata. They inspect **high-frequency Fourier transforms (FFT)**, **PRNU sensor patterns**, and **audio spectral cliffs**.

**Anti-AI Detection Guardian Bot** is a high-speed Telegram bot engineered to automate multi-layered evasion protocols. Whenever a user sends any video, photo, or document, the bot processes it through an advanced mathematical evasion engine and returns the clean media as an **uncompressed Document** with **identical visual & audio quality**.

---

## 🔬 How It Works (Bypass Architecture)

```
                       ┌────────────────────────────────────────────────────────┐
                       │                   INCOMING MEDIA                       │
                       └──────────────────────────┬─────────────────────────────┘
                                                  │
                         ┌────────────────────────┴────────────────────────┐
                         │                                                 │
                         ▼                                                 ▼
               📷 IMAGE PIPELINE                                 🎥 VIDEO PIPELINE
    ┌────────────────────────────────────────┐        ┌────────────────────────────────────────┐
    │ 1. 100.25% Bicubic Micro-Resample      │        │ 1. 100.25% Spatial Lattice Shift       │
    │ 2. Monochromatic PRNU Sensor Noise     │        │ 2. Dynamic 60 FPS Temporal Film Grain  │
    │ 3. Micro-Contrast & Color Tone Curve   │        │ 3. Audio 15kHz Spectral Shelf Exciter  │
    │ 4. Sony A7 IV (ILCE-7M4) Camera EXIF   │        │ 4. -42dB Studio Room Tone Floor        │
    │ 5. 4:4:4 Studio Color Space Export     │        │ 5. 0.25% Acoustic Pitch Jitter         │
    └───────────────────┬────────────────────┘        │ 6. Apple Core Media Container Profile  │
                        │                             └───────────────────┬────────────────────┘
                        │                                                 │
                        └────────────────────────┬────────────────────────┘
                                                 │
                                                 ▼
                       ┌────────────────────────────────────────────────────────┐
                       │          OUTGOING UNCOMPRESSED DOCUMENT                │
                       │    (100% Undetectable • Zero Quality Degradation)      │
                       └────────────────────────────────────────────────────────┘
```

### 1. Visual & Image Protection
* **PRNU Sensor Pattern Injection:** Diffusion models (Midjourney, Flux, DALL-E) leave a mathematical periodic checkerboard artifact during VAE latent decoding. Adding organic monochromatic camera sensor noise destroys this grid pattern in the Fourier frequency spectrum.
* **Bicubic Micro-Resampling:** Scaling the image by `100.25%` and center-cropping shuffles fixed-coordinate latent watermarks and forces fresh DCT block calculation without perceptible visual change.
* **Camera EXIF Injection:** Replaces blank/scrubbed metadata with authentic metadata from a **Sony Alpha 7 IV (`ILCE-7M4`)** camera with a **Sony FE 24-70mm F2.8 GM II** lens and Adobe Lightroom Classic export tags.

### 2. Audio & Video Protection
* **High-Frequency Spectral Shelf Restoration:** AI text-to-speech tools (like ElevenLabs, Edge-TTS) exhibit a sharp cutoff cliff above `15.2 kHz`. The bot applies a high-shelf parametric exciter (`15.5k - 18k`) to rebuild natural harmonic overtones.
* **Acoustic Studio Floor:** Synthesized voiceover features unnatural "dead digital zero silence" between spoken words. A low-level (`-42dB`) studio room tone floor eliminates this dead space.
* **Acoustic Hash Jitter:** Shifts pitch and tempo by `0.25%` (`asetrate` + `atempo`), defeating acoustic fingerprint hash matching algorithms.
* **Dynamic 60 FPS Temporal Grain:** Injects frame-by-frame analog grain at 60 FPS, defeating neural video classifiers like FakeCatcher.

---

## 🚀 Features

* ⚡ **High-Speed MTProto Engine:** Built on Pyrogram v2 for fast uploads/downloads up to 2GB.
* 📦 **Uncompressed Document Delivery:** Always sends back uncompressed documents to avoid Telegram's native compression.
* 📊 **Real-time Live Progress Bar:** Live percentage, speed, and time estimates during download and upload.
* 🧹 **Automatic Cleanup:** Immediate garbage collection of temporary files after delivery.
* 🐳 **Docker & Systemd Ready:** One-click deployment with Docker Compose or Linux Systemd.

---

## 🛠️ Installation & Setup

### Option 1: Bare Metal / Virtualenv

1. **Clone the repository:**
   ```bash
   git clone https://github.com/TeamInflex/AntiAIDetectionBot.git
   cd AntiAIDetectionBot
   ```

2. **Install system dependencies:**
   ```bash
   sudo apt update
   sudo apt install -y ffmpeg libimage-exiftool-perl python3 python3-pip python3-venv
   ```

3. **Set up Python Virtual Environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configure Environment:**
   ```bash
   cp .env.example .env
   nano .env
   ```
   Fill in your `API_ID`, `API_HASH`, and `BOT_TOKEN`.

5. **Run the bot:**
   ```bash
   python main.py
   ```

---

### Option 2: Docker Compose

1. **Configure `.env`:**
   ```bash
   cp .env.example .env
   nano .env
   ```

2. **Build and start container:**
   ```bash
   docker compose up -d --build
   ```

---

## ⚙️ Configuration Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `API_ID` | Telegram API ID from [my.telegram.org](https://my.telegram.org) | Mandatory |
| `API_HASH` | Telegram API Hash from [my.telegram.org](https://my.telegram.org) | Mandatory |
| `BOT_TOKEN` | Bot Token from [@BotFather](https://t.me/BotFather) | Mandatory |
| `OWNER_ID` | Telegram user ID of the owner | `1670303800` |
| `LOG_GROUP_ID` | Telegram group ID for logging errors / media | Optional |
| `IMAGE_SCALE_FACTOR` | Micro-scale factor for images | `1.0025` |
| `SENSOR_NOISE_STD` | Standard deviation for PRNU sensor noise | `1.75` |
| `JPEG_QUALITY` | Output JPEG quality level | `96` |
| `VIDEO_CRF` | Video Constant Rate Factor (18 = visually lossless) | `18` |
| `VIDEO_PRESET` | x264 encoder preset | `veryfast` |
| `PITCH_JITTER` | Micro-pitch shift ratio for voiceover | `1.0025` |

---

## 📜 Commands

* `/start` - Start the bot and view feature breakdown.
* `/help` - View technical specifications and usage guide.
* `/status` - Check server uptime, CPU, and RAM metrics.

---

## 👨‍💻 Developer & Credits

* **Developer:** [S H I V A](https://t.me/TheShivaxD)
* **Organization:** [Team Inflex](https://github.com/TeamInflex)
* **Community:** [Team Inflex Indonesia](https://t.me/TeamInflexIndonesia)

---

<div align="center">
<b>Made with ❤️ by Team Inflex</b>
</div>
