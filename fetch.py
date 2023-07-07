import pytube
import json

playlist_url = input("Enter the playlist URL: ")
playlist = pytube.Playlist(playlist_url)

youtube_jingles = {}

for video_url in playlist.video_urls:
    video = pytube.YouTube(video_url)
    video_info = {
        video.title: video_url,
    }
    youtube_jingles.update(video_info)

print(json.dumps(youtube_jingles, indent=4))
