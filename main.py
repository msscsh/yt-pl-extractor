import yt_dlp

playlist_url = 'https://www.youtube.com/playlist?list=PLfvgsz0FyyCAbuM0vZ9Z-HvmQbCAScfbe'

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
