import pytube
import json
import os

while True:
    try:
        playlist_url = input("Enter the playlist URL: ")
        playlist = pytube.Playlist(playlist_url)

        youtube_songs = {}

        for video_url in playlist.video_urls:
            try:
                video = pytube.YouTube(video_url)
                video_info = {
                    video.title: video_url,
                }
                youtube_songs.update(video_info)
            except Exception as e:
                print(f"Error processing video: {video_url}")
                print(f"Error message: {str(e)}")

        playlist_title = playlist.title
        log_folder = "logs"
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
        log_file = f"{log_folder}/{playlist_title}.json"  # Save logs in /logs/ directory

        if os.path.exists(log_file):
            replace = input("Playlist already exists. Do you want to replace it? (y/n): ")
            if replace.lower() == "y":
                with open(log_file, 'w') as f:
                    json.dump(youtube_songs, f, indent=4)
                print(json.dumps(youtube_songs, indent=4))
                print(f"{len(youtube_songs)} results fetched saved in {log_folder}/{playlist_title}.json")  # Print the number of results fetched
            else:
                print("Playlist not saved.")
        else:
            with open(log_file, 'w') as f:
                json.dump(youtube_songs, f, indent=4)
            print(json.dumps(youtube_songs, indent=4))
            print(f"{len(youtube_songs)} results fetched saved in {log_folder}/{playlist_title}.json")  # Print the number of results fetched
    except Exception as e:
        print(f"Error processing playlist: {playlist_url}")
        print(f"Error message: {str(e)}")
