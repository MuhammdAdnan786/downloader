from pytube import YouTube#It is for one video
link='https://youtu.be/I5K9YEbn-h8?si=guExYZa5WbsE0E5L'#for playlist import Playlist.
youtube=YouTube(link)

# print(youtube.title)#this for the downloading the title of the given video.
# print(youtube.thumbnail_url)#this command for the downloading the video thumbnail.

videos=youtube.streams.all()#it mean how many of pixels you want to download the video.
# videos=youtube.streams.filter(only_audio=True) #this is for the downloading only the audio
vid=list(enumerate(videos))#it give you a list
for i in vid:
    print(i)
print()
strm=int(input('Enter-->:'))
videos[strm].download()
print('Successfully!')

# Gui for you tube video downloader
# import tkinter as tk
# from pytube import YouTube

# def download_video():
#     link = entry.get()
#     try:
#         yt = YouTube(link)
#         stream = yt.streams.get_highest_resolution()
#         stream.download()
#         status_label.config(text="Download successful!")
#     except Exception as e:
#         status_label.config(text="Download failed. Error: " + str(e))
# root = tk.Tk()
# root.title("YouTube Video Downloader")

# label = tk.Label(root, text="Enter YouTube link:")
# label.pack()

# entry = tk.Entry(root, width=40)
# entry.pack()

# download_button = tk.Button(root, text="Download", command=download_video)
# download_button.pack()

# status_label = tk.Label(root, text="")
# status_label.pack()

# root.mainloop()


