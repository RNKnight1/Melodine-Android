from utils import *
def get_music(search_term, save_as, out_dir, sleep_val = 0, part = True):
	alpha_list = list(string.printable)[: -6]
	alpha_list.remove('/')
	alpha_list.remove('\\')
	alpha_list.remove('"')
	alpha_list.append(' ')
	global song_path
	song_path = ""
	filter_search_term = ''.join(
	    [char for char in search_term if char in alpha_list])
	try:
		status_dir[search_term] = 'downloading'

		time.sleep(sleep_val)

		if save_as == None:
			save_as = search_term

		melodine_dir = os.path.join(os.path.expanduser('~'), '.melodine')

		music_dir = os.path.join(melodine_dir, out_dir)
		formatted_search_term = filter_search_term.replace(' ', '+')

		html = urllib.request.urlopen(
		    "https://www.youtube.com/results?search_query=" + formatted_search_term)
		video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

		yt_url_thingy = 'https://www.youtube.com/watch?v='
		le_url = yt_url_thingy + video_ids[0]
		song = pafy.new(le_url)
		best = song.getbestaudio(preftype="m4a")
		song_path = f"{music_dir}/{formatted_search_term}.{best.extension}"
		print(song_path)
		best.download(filepath=song_path)

		status_dir[search_term] = 'downloaded'
	except Exception as e:
		status_dir[search_term] = 'downloaded'
		print('errorr in downloading')
		#traceback.print_exc()
		print(e)
		pass