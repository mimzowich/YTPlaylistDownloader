# Import necessary libraries
from pytube import Playlist
from moviepy.editor import *

def download_playlist(playlist_url):
    """
    Downloads and converts each video in a YouTube playlist to MP3 format.

    Parameters:
    playlist_url (str): URL of the YouTube playlist to download.
    """
    # Create a Playlist object using the given URL
    pl = Playlist(playlist_url)
    print(f'Downloading Playlist: {pl.title}')

    # Iterate over each video in the playlist
    for video in pl.videos:
        print(f'Downloading Video: {video.title}')
        # Select the first audio stream of the video (no video content)
        stream = video.streams.filter(only_audio=True).first()
        # Download the audio stream and save the path
        download_path = stream.download()

        print(f'Converting to MP3: {video.title}')
        # Path to the downloaded MP4 file
        mp4_file = download_path
        # Create a new path for the MP3 file
        mp3_file = download_path.split('.mp4', 1)[0] + '.mp3'
        # Load the audio from the downloaded file
        video_clip = AudioFileClip(mp4_file)
        # Write the audio to the new MP3 file
        video_clip.write_audiofile(mp3_file)
        # Close the clip to free up system resources
        video_clip.close()
        # Remove the original MP4 file as it's no longer needed
        os.remove(mp4_file)

def main():
    """
    Main function to execute the script.
    Prompts the user for the playlist URL and processes the playlist.
    """
    # Get YouTube playlist URL from user
    playlist_url = input("Enter the YouTube Playlist URL: ")
    # Call the function to download and convert the playlist
    download_playlist(playlist_url)

# Check if the script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Run the main function
    main()

