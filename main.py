import os
import sys
import logging
from pyrogram import Client
from config import Config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("AntiAIGuardian")

BANNER = r"""
   _____          __  .__    _____  .___ __________.__          __  
  /  _  \   _____/  |_|__|  /  _  \ |   |\______   \__| ____   |  | 
 /  /_\  \ /    \   __\  | /  /_\  \|   | |    |  _/  |/  _ \ _|  |_
/    |    \   |  \  | |  |/    |    \   | |    |   \  (  <_> )-_   _-
\____|__  /___|  /__| |__|\____|__  /___| |______  /__|\____/   |__|  
        \/     \/                 \/             \/                   
            Anti-AI Detection Guardian Bot — Team Inflex
"""

def main():
    print(BANNER)
    if not Config.BOT_TOKEN:
        logger.error("BOT_TOKEN is not configured! Please check your .env file.")
        sys.exit(1)
        
    os.makedirs(Config.DOWNLOAD_DIR, exist_ok=True)
    os.makedirs(Config.OUTPUT_DIR, exist_ok=True)
    
    app = Client(
        "AntiAIDetectionBot",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="handlers")
    )
    
    logger.info("Starting Anti-AI Detection Bot...")
    app.run()

if __name__ == "__main__":
    main()
