<h1 align="center">Melodine</h1>

## Description
A command-line(for now) tool to play and download music from YouTube. Made mainly by an expert Python programmer and a novice Python programmer annoyed by Spotify Free's limitations.

## Features
-  Downloads or streams audio from YouTube using pafy.
- Autoplay feature using Spotify API recommendations basedon current song.
- Notifies of currently playing song.

## Planned Features
- Search function so users can search for the song instead of playing the top result.
- Search for lyrics.
- Fixing the countless bugs.
- Group listening.

## Usage
For android:
Enter Termux
Run this:

	pkg upgrade
	pkg install git

Then run this:

	git clone https://github.com/RNKnight1/Melodine-Android
	cd Melodine-Android
	sh setup.sh

This should download the code and set it up.

Run the program with
	python ~/Melodine-Android/hopidy.py

### Commands
- .play \<Song Name> - Plays the top result for the search term.
- .dload \<Song Name> - Downloads the top result for the search term.
- .addq \<Song Name> - Adds song to the end of the queue
- .showq - Displays queue
- .playnext - \<Song Name> - Plays the top search result after the currently playing song.
- .nowp - Displays currently playing song.
- .quit - Exits the program gracefully.
