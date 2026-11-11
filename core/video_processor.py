import os
import subprocess
import json
import datetime
from config import Config

def probe_file(file_path: str) -> dict:
    cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_format", "-show_streams",
        file_path
    ]
    res = subprocess.check_output(cmd)
    return json.loads(res.decode("utf-8"))

def process_video_anti_ai(src_path: str, dest_path: str) -> str:
    """
    Applies multi-layered Anti-AI evasion to a video file:
    1. Audio: Restores spectral air (15.5k - 18k), injects -42dB room tone floor, applies 0.25% micro-pitch jitter.
    2. Video: Micro-resampling (100.25% bicubic), dynamic 60fps temporal PRNU film grain, micro-contrast.
    3. Container: Apple QuickTime / Core Media handler and realistic creation metadata.
    """
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    probe = probe_file(src_path)
    streams = probe.get("streams", [])
    has_audio = any(s.get("codec_type") == "audio" for s in streams)
    
    duration = float(probe.get("format", {}).get("duration", 60.0))
    now_iso = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000000Z")
    
    temp_dir = os.path.dirname(dest_path)
    temp_audio = os.path.join(temp_dir, f"temp_audio_{os.path.basename(dest_path)}.m4a")
    
    jitter = Config.PITCH_JITTER
    
    if has_audio:
        # Step 1: Process Audio
        dur_arg = int(duration) + 2
        audio_cmd = [
            "ffmpeg", "-y",
            "-i", src_path,
            "-f", "lavfi", "-i", f"anoisesrc=d={dur_arg}:c=pink:r=48000:a=0.0006",
            "-filter_complex",
            f"[0:a]asetrate=48000*{jitter},atempo=1/{jitter},equalizer=f=16000:width_type=h:width=2000:g=4,highshelf=f=15000:g=3.5[vocal];"
            "[1:a]lowpass=f=14000,highpass=f=80,volume=0.4[room];"
            "[vocal][room]amix=inputs=2:duration=first:dropout_transition=0.5,volume=1.0[aout]",
            "-map", "[aout]",
            "-c:a", "aac", "-b:a", "256k", "-ar", "48000",
            temp_audio
        ]
        subprocess.run(audio_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Step 2: Process Video with Enhanced Audio
        video_cmd = [
            "ffmpeg", "-y",
            "-i", src_path,
            "-i", temp_audio,
            "-filter_complex",
            "[0:v]scale=iw*1.0025:ih*1.0025:flags=bicubic,crop=in_w:in_h,noise=c0s=4:c0f=t+u:c1s=2:c2s=2,eq=contrast=1.01:saturation=1.01[vout]",
            "-map", "[vout]",
            "-map", "1:a",
            "-c:v", "libx264",
            "-preset", Config.VIDEO_PRESET,
            "-crf", str(Config.VIDEO_CRF),
            "-profile:v", "high",
            "-level", "4.2",
            "-pix_fmt", "yuv420p",
            "-c:a", "copy",
            "-movflags", "+faststart",
            "-brand", "mp42",
            "-metadata", f"creation_time={now_iso}",
            "-metadata", "handler_name=Core Media Video",
            "-metadata:s:v:0", "handler_name=Core Media Video",
            "-metadata:s:a:0", "handler_name=Core Media Audio",
            dest_path
        ]
        subprocess.run(video_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if os.path.exists(temp_audio):
            os.remove(temp_audio)
    else:
        # Silent video processing
        video_cmd = [
            "ffmpeg", "-y",
            "-i", src_path,
            "-filter_complex",
            "[0:v]scale=iw*1.0025:ih*1.0025:flags=bicubic,crop=in_w:in_h,noise=c0s=4:c0f=t+u:c1s=2:c2s=2,eq=contrast=1.01:saturation=1.01[vout]",
            "-map", "[vout]",
            "-c:v", "libx264",
            "-preset", Config.VIDEO_PRESET,
            "-crf", str(Config.VIDEO_CRF),
            "-profile:v", "high",
            "-level", "4.2",
            "-pix_fmt", "yuv420p",
            "-movflags", "+faststart",
            "-brand", "mp42",
            "-metadata", f"creation_time={now_iso}",
            "-metadata", "handler_name=Core Media Video",
            "-metadata:s:v:0", "handler_name=Core Media Video",
            dest_path
        ]
        subprocess.run(video_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    return dest_path
