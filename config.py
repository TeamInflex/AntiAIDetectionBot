import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID", "19584198"))
    API_HASH = os.getenv("API_HASH", "0ed81ce2babcf61c880d2b49c2dee9f1")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    OWNER_ID = int(os.getenv("OWNER_ID", "1670303800"))
    LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0")) if os.getenv("LOG_GROUP_ID") else None
    
    DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR", "./downloads")
    OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./outputs")
    
    # Anti-AI Parameters
    IMAGE_SCALE_FACTOR = float(os.getenv("IMAGE_SCALE_FACTOR", "1.0025"))
    SENSOR_NOISE_STD = float(os.getenv("SENSOR_NOISE_STD", "1.75"))
    JPEG_QUALITY = int(os.getenv("JPEG_QUALITY", "96"))
    
    VIDEO_CRF = int(os.getenv("VIDEO_CRF", "18"))
    VIDEO_PRESET = os.getenv("VIDEO_PRESET", "veryfast")
    PITCH_JITTER = float(os.getenv("PITCH_JITTER", "1.0025"))
