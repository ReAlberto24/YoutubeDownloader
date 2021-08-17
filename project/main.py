import pytube, os, shutil
from moviepy.editor import VideoFileClip
from getpass import getuser

def DownloadMusic(link):
	''' Download music.'''
	try:
		try:
			os.mkdir('YoutubeDownloaderDir')

		except:
			pass
	
		video = youtube.streams.get_lowest_resolution()
		video.download('YoutubeDownloaderDir')

		vdn = os.listdir('YoutubeDownloaderDir')
		vdn = vdn[0]
		vdn = vdn.replace('.mp4', '')

		vdn_mp4 = f'YoutubeDownloaderDir\\{vdn}.mp4'
		vdn_mp3 = f'YoutubeDownloaderDir\\{vdn}.mp3'
	
		videoclip = VideoFileClip(vdn_mp4, verbose=False)
		audioclip = videoclip.audio
		audioclip.write_audiofile(vdn_mp3, logger=None)
		audioclip.close()
		videoclip.close()

		os.remove(vdn_mp4)

		fns = os.listdir('YoutubeDownloaderDir')

		for file_name in fns:
			
			shutil.move(f'YoutubeDownloaderDir\\{file_name}', f'C:\\Users\\{getuser()}\\Downloads')

		os.rmdir('YoutubeDownloaderDir')

		return video.title

	except:
		return False
	
def DownloadVideo(link):
	''' Download video.'''
	try:
		video = youtube.streams.get_highest_resolution()
		video.download(f'C:\\Users\\{getuser()}\\Downloads')

		return video.title

	except:
		return False




url = input('URL or VideoID: ')

if len(url) == 11:

	url = f'https://www.youtube.com/watch?v={url}'

try:

	youtube = pytube.YouTube(url)
	print('Video found!')

except:

	print('Video not found.')
	print(':(')
	input('Press enter to close...')
	exit()
	

justA = input('Just audio? [Y for Yes, anything else for No] ')

print('Downloading it...')

if justA.upper() == 'Y':
	vt = DownloadMusic(url)
	mode = '.mp3'
	
else:
	vt = DownloadVideo(url)
	mode = '.mp4'

if vt == False:
	print(f'Error to download {url}...')

else:
	print(f'Downloaded video as "{vt}{mode}"')

input('Press enter to close...')
