from pytube import YouTube
from pytube.cli import on_progress

link = input('> Enter link: ')
print()
yt = YouTube( link, on_progress_callback=on_progress)

print(f'Video title: {yt.title}')
print(f'video has {yt.views} views')
print()

save_path = "C:\\Users\\Hp Folio\\Desktop"
video = yt.streams.get_highest_resolution()
video.download(output_path=save_path)

print('Video successfully downloaded')