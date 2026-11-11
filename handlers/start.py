import time
import platform
import psutil
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

START_TIME = time.time()

@Client.on_message(filters.command(["start"]))
async def start_handler(client: Client, message: Message):
    user_name = message.from_user.first_name if message.from_user else "Friend"
    text = (
        f"👋 **Hey {user_name}! Welcome to Anti-AI Guardian Bot** 🛡️\n\n"
        "Main aapki kisi bhi **AI-Generated Image** ya **Video** ko **100% Anti-AI Detected** bana sakta hoon — "
        "chahe kitna bhi powerful AI detector ho (Hive Moderation, Sightengine, WasItAI, ElevenLabs Classifier, etc.)!\n\n"
        "✨ **What I Do:**\n"
        "• 📷 **Images:** PRNU camera sensor pattern noise inject karta hoon, latent Fourier checkerboard grid mask karta hoon, "
        "micro-resample karta hoon, aur authentic Sony Alpha 7 IV camera EXIF inject karta hoon.\n"
        "• 🎥 **Videos:** High-frequency audio cliff (15.2kHz) restore karta hoon, -42dB studio room tone add karta hoon, "
        "micro-pitch jitter lagata hoon, aur 60 FPS temporal film grain ke sath deliver karta hoon.\n\n"
        "📤 **Bas koi bhi Image ya Video bhejo (Photo, Video, ya Document ke roop me) — baaki kaam main khud sambhal lunga!**"
    )
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/TheShivaxD"),
            InlineKeyboardButton("📢 Channel", url="https://t.me/TeamInflexIndonesia")
        ],
        [
            InlineKeyboardButton("ℹ️ Help & Technical Specs", callback_data="help_callback")
        ]
    ])
    await message.reply_text(text, reply_markup=buttons)

@Client.on_message(filters.command(["help"]))
async def help_handler(client: Client, message: Message):
    text = (
        "📖 **Anti-AI Guardian — How to Use & Technical Specs**\n\n"
        "1️⃣ **Send Any Video:**\n"
        "• Support: MP4, MOV, MKV up to 2GB.\n"
        "• Fixes: ElevenLabs 15kHz cutoff, removes artificial zero-silence, applies 60fps dynamic temporal grain.\n\n"
        "2️⃣ **Send Any Image:**\n"
        "• Support: JPG, PNG, WEBP.\n"
        "• Fixes: Strips AI latent markers, injects Sony A7 IV EXIF, outputs pristine 4:4:4 color.\n\n"
        "3️⃣ **Return Format:**\n"
        "• Always returns an **uncompressed Document** with identical visual and audio quality.\n\n"
        "⚡ Powered by **Team Inflex**"
    )
    await message.reply_text(text)

@Client.on_message(filters.command(["status"]))
async def status_handler(client: Client, message: Message):
    uptime_sec = int(time.time() - START_TIME)
    uptime_str = time.strftime("%Hh %Mm %Ss", time.gmtime(uptime_sec))
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    
    text = (
        "📊 **Anti-AI Guardian — System Status**\n\n"
        f"⏱️ **Uptime:** `{uptime_str}`\n"
        f"🖥️ **CPU Usage:** `{cpu}%`\n"
        f"🧠 **RAM Usage:** `{ram}%`\n"
        f"🐧 **OS:** `{platform.system()} {platform.release()}`\n"
        "🛡️ **Engine:** FFmpeg + ExifTool + PRNU Noise Core"
    )
    await message.reply_text(text)

@Client.on_callback_query(filters.regex("help_callback"))
async def help_callback_handler(client: Client, query):
    text = (
        "📖 **Anti-AI Guardian — Technical Bypass Architecture**\n\n"
        "🔬 **1. Fourier (FFT) Masking:**\n"
        "Diffusion models VAE checkerboard patterns leave high-frequency spikes. Our PRNU sensor engine neutralizes this completely.\n\n"
        "🔬 **2. Audio Spectral Extension:**\n"
        "TTS models cut off strictly at 15-16kHz. Our harmonic exciter and -42dB room air floor rebuild natural mic presence.\n\n"
        "🔬 **3. Camera Fingerprint:**\n"
        "Injects authentic Sony Alpha 7 IV / Adobe Lightroom Classic metadata tags.\n\n"
        "Send any media file now to test!"
    )
    await query.message.edit_text(text)
