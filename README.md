# JukeBox
A Python-based Shell script-style audio player.<br>
Note: While the install process has been tested, it is likely unforeseen bugs will appear in this code. Having an understanding of python is recommended, although not required.
 
 ## Installation
Ensure that all of the following python packages and their dependencies are installed, as well as python 3.9 (or later!). The package versions listed here are known to work; however, earlier versions of the packages may also be compatible.
* random 3 or later
* os 3.13 or later
* pygame 2.5.2 or later
* time
* copy 3.3 or later
* datetime
* json 2.0.9 or later
* requests 2.32.3 or later
* numpy 1.26.4 or later
* mutagen 1.47.0 or later
* bs4 4.12.3 or later
* tinytag 1.10.1 or later


Download main.py and userInput.py. Set up a directory for your music files. Then run both python files. The program should prompt you to set up a username,  the absolute path to your music directory, and the length of your output terminal window. The program should automatically create all of the files it needs to run as well.

## The Music Directory
Currently, this music player fully supports .mp3 and .opus files, and supports playing .wav files, but does not support extra functionality with .wav files. For this player to function correctly, all music files must be in one of the following forms:
* Artist - Song name.mp3
* Artist - Album - Song name.mp3
* Song name.mp3

If the song title, album name, or artist name contains a dash (-), replace it with an underscore (\_). If they contain a backslash (/), replace them with two underscores (\_\_). If they contain a colon (:), replace them with three underscores (\_\_\_). Song titles may not contain a \pm symbol (±).
	
## Running the program
In a terminal shell, run "python3 \path\to\main.py & \path\to\userInput.py"

## Features
This program is light on memory storage. It is very plurality-friendly, as switching between users/headmates can be done with one command 'new-user USERNAME'. Almost all of the program can be run without an internet connection, excepting the code for updating lyrics. This program runs has an analytics feature - with both a short term and a long term document saving user metrics. While these documents cannot yet be disabled, they are both stored on-site in the program files and can be deleted at the user's convenience, both inside and outside the program. This jukebox supports playlists, and has a basic playlist editing feature, and also has a robust queue function.
