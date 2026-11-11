import os
import subprocess
import datetime
import numpy as np
from PIL import Image, ImageEnhance
from config import Config

def process_image_anti_ai(src_path: str, dest_path: str) -> str:
    """
    Applies multi-layered Anti-AI evasion to an image:
    1. Bicubic non-integral micro-resampling (breaks diffusion latent coordinates).
    2. Monochromatic PRNU sensor pattern noise injection (masks Fourier checkerboard artifacts).
    3. Micro-contrast & tonal dither.
    4. Authentic Camera EXIF injection (Sony A7 IV + Lightroom Classic).
    """
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    img = Image.open(src_path).convert("RGB")
    orig_w, orig_h = img.size
    
    # 1. Micro-resample
    scale = Config.IMAGE_SCALE_FACTOR
    scaled_w = int(round(orig_w * scale))
    scaled_h = int(round(orig_h * scale))
    img_scaled = img.resize((scaled_w, scaled_h), Image.Resampling.BICUBIC)
    
    # Center crop back to original resolution
    left = (scaled_w - orig_w) // 2
    top = (scaled_h - orig_h) // 2
    img_cropped = img_scaled.crop((left, top, left + orig_w, top + orig_h))
    
    # 2. Add subtle physical sensor noise (PRNU simulation)
    arr = np.array(img_cropped, dtype=np.float32)
    noise = np.random.normal(loc=0.0, scale=Config.SENSOR_NOISE_STD, size=(orig_h, orig_w, 1))
    arr_noisy = np.clip(arr + noise, 0, 255).astype(np.uint8)
    
    img_final = Image.fromarray(arr_noisy)
    
    # 3. Micro-contrast adjustment (1.01)
    enhancer = ImageEnhance.Contrast(img_final)
    img_final = enhancer.enhance(1.01)
    
    # 4. Save with high quality (4:4:4 subsampling)
    img_final.save(dest_path, "JPEG", quality=Config.JPEG_QUALITY, optimize=True, subsampling=0)
    
    # 5. Inject camera EXIF using exiftool if available
    try:
        now_str = datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
        exif_cmd = [
            "exiftool", "-overwrite_original",
            "-Make=Sony",
            "-Model=ILCE-7M4",
            "-LensModel=FE 24-70mm F2.8 GM II",
            "-FocalLength=50.0 mm",
            "-FocalLengthIn35mmFormat=50 mm",
            "-FNumber=2.8",
            "-ExposureTime=1/160",
            "-ISO=160",
            "-ExposureProgram=Manual",
            "-MeteringMode=Multi-segment",
            "-LightSource=Fine Weather",
            "-Software=Adobe Photoshop Lightroom Classic 13.2 (Macintosh)",
            "-ColorSpace=sRGB",
            "-ExifVersion=0232",
            "-ComponentsConfiguration=Y, Cb, Cr, -",
            "-SceneCaptureType=Standard",
            "-ExposureMode=Manual",
            "-WhiteBalance=Auto",
            f"-DateTimeOriginal={now_str}",
            f"-CreateDate={now_str}",
            f"-ModifyDate={now_str}",
            "-OffsetTime=+05:30",
            "-OffsetTimeOriginal=+05:30",
            dest_path
        ]
        subprocess.run(exif_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Warning: EXIF injection skipped or failed: {e}")
        
    return dest_path
