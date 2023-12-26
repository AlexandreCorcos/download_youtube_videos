from pytube import YouTube


def download_video(url, output_path="."):
    try:
        yt = YouTube(url)

        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path)

        print(f"Video downloaded successfully to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


while True:
    video_url = input("Enter the YouTube video URL ('exit' to finish): ")
    if video_url == "exit":
        break

    output_folder = input("Enter the output folder (default is current directory): ") or "."
    download_video(video_url, output_folder)
