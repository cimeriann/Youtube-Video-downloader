from pytube import YouTube
from pytube.cli import on_progress

link = input('> Enter link: ')
print()
yt = YouTube(link, on_progress_callback=on_progress)

print(f'Video title: {yt.title}')
print(f'video has {yt.views} views')
