import os
import time

def humanbytes(size: int) -> str:
    if not size:
        return "0 B"
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

last_update_time = {}

async def progress_bar(current: int, total: int, status_msg, action_text: str):
    now = time.time()
    msg_id = status_msg.id
    
    # Throttle updates every 3.5 seconds to avoid FloodWait
    if msg_id in last_update_time and (now - last_update_time[msg_id]) < 3.5:
        return
        
    last_update_time[msg_id] = now
    percentage = current * 100 / total
    speed = current / (now - status_msg.date.timestamp() + 1)
    
    filled_blocks = int(percentage // 10)
    bar = "▰" * filled_blocks + "▱" * (10 - filled_blocks)
    
    text = (
        f"⚡ **{action_text}**\n\n"
        f"[{bar}] `{percentage:.1f}%`\n"
        f"📊 **Progress:** `{humanbytes(current)} / {humanbytes(total)}`\n"
        f"🚀 **Speed:** `{humanbytes(speed)}/s`"
    )
    try:
        await status_msg.edit_text(text)
    except Exception:
        pass
