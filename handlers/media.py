import os
import shutil
from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from core.image_processor import process_image_anti_ai
from core.video_processor import process_video_anti_ai
from core.utils import progress_bar, humanbytes

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".flv"}

@Client.on_message(filters.photo | filters.video | filters.document)
async def media_handler(client: Client, message: Message):
    # Determine media type
    is_image = False
    is_video = False
    file_name = None
    
    if message.photo:
        is_image = True
        file_name = f"photo_{message.photo.file_unique_id}.jpg"
    elif message.video:
        is_video = True
        file_name = message.video.file_name or f"video_{message.video.file_unique_id}.mp4"
    elif message.document:
        doc = message.document
        mime = (doc.mime_type or "").lower()
        ext = os.path.splitext(doc.file_name or "")[1].lower()
        
        if mime.startswith("image/") or ext in IMAGE_EXTENSIONS:
            is_image = True
            file_name = doc.file_name or f"image_{doc.file_unique_id}.jpg"
        elif mime.startswith("video/") or ext in VIDEO_EXTENSIONS:
            is_video = True
            file_name = doc.file_name or f"video_{doc.file_unique_id}.mp4"
            
    if not (is_image or is_video):
        return  # Ignore non-media documents (like txt, zip, pdf)
        
    status_msg = await message.reply_text("⚡ **Initializing Anti-AI Security Protocol...**")
    
    user_id = message.from_user.id if message.from_user else 0
    task_dir = os.path.join(Config.DOWNLOAD_DIR, f"{user_id}_{message.id}")
    out_dir = os.path.join(Config.OUTPUT_DIR, f"{user_id}_{message.id}")
    os.makedirs(task_dir, exist_ok=True)
    os.makedirs(out_dir, exist_ok=True)
    
    src_file = os.path.join(task_dir, file_name)
    
    try:
        # Step 1: Download Media
        await status_msg.edit_text("📥 **Downloading original file...**")
        downloaded_path = await message.download(
            file_name=src_file,
            progress=progress_bar,
            progress_args=(status_msg, "Downloading Media")
        )
        
        if not downloaded_path or not os.path.exists(downloaded_path):
            await status_msg.edit_text("❌ **Download failed! Please try again.**")
            return
            
        # Step 2: Anti-AI Processing
        await status_msg.edit_text(
            "⚙️ **Applying Anti-AI Evasion Engine...**\n\n"
            "• Stripping Latent Diffusion Patterns\n"
            "• Injecting Physical PRNU Sensor Noise\n"
            "• Restoring Audio Air & Acoustic Floor\n"
            "• Embedding Camera Metadata Profile"
        )
        
        base_name, ext = os.path.splitext(file_name)
        if is_image:
            dest_file = os.path.join(out_dir, f"AntiAI_{base_name}.jpg")
            processed_path = process_image_anti_ai(downloaded_path, dest_file)
            caption = (
                f"🛡️ **{os.path.basename(processed_path)}**\n\n"
                "✅ **100% Anti-AI Detected**\n"
                "• **PRNU Noise:** Authentic camera sensor grain (masks Fourier checkerboard).\n"
                "• **Bicubic Lattice Shift:** 100.25% coordinate micro-resample.\n"
                "• **Camera Profile:** Sony Alpha 7 IV (ILCE-7M4) + Lightroom Classic EXIF.\n"
                "• **Quality:** Pristine 4:4:4 Studio Color (Zero loss)."
            )
        else:
            dest_file = os.path.join(out_dir, f"AntiAI_{base_name}.mp4")
            processed_path = process_video_anti_ai(downloaded_path, dest_file)
            caption = (
                f"🛡️ **{os.path.basename(processed_path)}**\n\n"
                "✅ **100% Anti-AI Detected (60 FPS HD)**\n"
                "• **Audio Spectral Air:** 15.2kHz shelf cliff restored with natural high harmonics.\n"
                "• **Acoustic Floor:** -42dB studio ambience (removes dead digital silence).\n"
                "• **Acoustic Jitter:** 0.25% micro-pitch shift (defeats ElevenLabs classifier hashes).\n"
                "• **Visual PRNU:** Dynamic 60fps temporal grain + bicubic spatial lattice shift.\n"
                "• **Container:** Apple QuickTime / Core Media Profile."
            )
            
        # Step 3: Upload Document
        await status_msg.edit_text("📤 **Uploading uncompressed Anti-AI document...**")
        await client.send_document(
            chat_id=message.chat.id,
            document=processed_path,
            caption=caption,
            reply_to_message_id=message.id,
            progress=progress_bar,
            progress_args=(status_msg, "Uploading Document")
        )
        
        await status_msg.delete()
        
    except Exception as e:
        await status_msg.edit_text(f"❌ **Error during Anti-AI processing:**\n`{str(e)}`")
    finally:
        # Cleanup temp directories
        if os.path.exists(task_dir):
            shutil.rmtree(task_dir, ignore_errors=True)
        if os.path.exists(out_dir):
            shutil.rmtree(out_dir, ignore_errors=True)
