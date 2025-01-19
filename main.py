imports_successful = True
missing_packages = []


try:
    import random
except ModuleNotFoundError:
    imports_successful = False
    missing_packages.append("random")
try:
    import os
except ModuleNotFoundError:
    imports_successful = False
    missing_packages.append("os")
try:
    import pygame
except ModuleNotFoundError:
    imports_successful = False
    missing_packages.append("pygame")
try:
    import time
except ModuleNotFoundError:
    imports_successful = False
    missing_packages.append("time")
try:
    import copy
except ModuleNotFoundError:
    imports_successful = False
    missing_packages.append("copy")
try:
    import datetime
except ModuleNotFoundError:
    imports_successful = False
    missing_packages.append("datetime")
try:
    import json
except ModuleNotFoundError:
    imports_successful = False
    missing_packages.append("json")
try:
    import requests
except ModuleNotFoundError:
    imports_successful = False
    missing_packages.append("requests")
try:
    import numpy as np
except ModuleNotFoundError:
    imports_successful = False
    missing_packages.append("numpy")
try:
    from mutagen.mp3 import MP3
    from mutagen.oggopus import OggOpus
except ModuleNotFoundError:
    imports_successful = False
    missing_packages.append("mutagen")
"""try:
    from matplotlib import pyplot as plt
except ModuleNotFoundError:
    imports_successful = False
    missing_packages.append("matplotlib")"""
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    imports_successful = False
    missing_packages.append("bs4")
try:
    from tinytag import TinyTag
except ModuleNotFoundError:
    imports_successful = False
    missing_packages.append("tinytag")

# import audioplayer


# checking to make sure all installed .txt and .json files exist
# i.e. so the program does not crash randomly
# then creating those files if they do not
try:
    with open("Analytics.txt", "r") as f:
        pass
except FileNotFoundError:
    with open("Analytics.txt", "w") as f:
        pass
try:
    with open("bugs.txt", "r") as f:
        pass
except FileNotFoundError:
    with open("bugs.txt", "w") as f:
        pass
try:
    with open("Input.txt", "r") as f:
        pass
except FileNotFoundError:
    with open("Input.txt", "w") as f:
        pass
try:
    with open("Output.txt", "r") as f:
        pass
except FileNotFoundError:
    with open("Output.txt", "w") as f:
        pass
try:
    with open("Playlists.txt", "r") as f:
        pass
except FileNotFoundError:
    with open("Playlists.txt", "w") as f:
        pass
try:
    with open("Settings.txt", "r") as f:
        pass
except FileNotFoundError:
    with open("Settings.txt", "w") as f:
        pass
try:
    with open("ShortTermAnalytics.txt", "r") as f:
        pass
except FileNotFoundError:
    with open("ShortTermAnalytics.txt", "w") as f:
        pass
'''try:
    with open("Songs.txt", "r") as f:
        pass
except FileNotFoundError:
    with open("Songs.txt", "w") as f:
        pass'''
try:
    with open("Songs.json", "r") as f:
        pass
except FileNotFoundError:
    with open("Songs.json", "w") as f:
        pass
try:
    with open("songlyrics.txt", "r") as f:
        pass
except FileNotFoundError:
    with open("songlyrics.txt", "w") as f:
        pass
try:
    with open("songsbackup.json", "r") as f:
        pass
except FileNotFoundError:
    with open("songsbackup.json", "w") as f:
        pass



def printLogo():
    print("     ___")
    print("  ,''   '',")
    print(" ,'  (o)  ',")
    print(" ≡` ==o== `≡")
    print(" |'U'|||'U'|" + " "*15 + "Welcome to the Jukebox!")
    print(" |\"U'XXX'U\"|")
    print(" |\"U'XXX'U\"|" + " "*15 + "Designed by Claudia >:3")
    print(" |\"U''X''U\"|")
    print(" |\"'U'\"'U'\"|" + " "*15 + "Version 1.4.2")
    print(" |\"''UUU''\"|")
    print(" ```````````")


class JukeBox:
    def __init__(self, user):
        self.users = []
        #add install location stuff
        settingsNonempty = False
        with open("Settings.txt", "r") as f:
            for x in f:
                x = x.replace("\n", "")
                x = x.split(":")
                if x[0] == "users":
                    if len(x) > 1:
                        settingsNonempty = True
                        user_string_list = x[1].split(",")
                        for y in user_string_list:
                            while y[0] == " ":
                                y = y[1:]
                            while y[-1] == " ":
                                y = y[:-1]
                            self.users.append(y)
                elif x[0] == "directory":
                    if len(x) > 1:
                        settingsNonempty = True
                        while x[1][0] == " ":
                            x = x[1][1:]
                        while x[1][-1] == " ":
                            x = x[1][:-1]
                        self.Directory = x
                elif x[0] == "size":
                    if len(x) > 1:
                        settingsNonempty = True
                        self.terminal_length = int(x[1])
        if not settingsNonempty:
            user_one = input("Please enter a user name.")
            self.users = ["admin", user_one]
            self.Directory = input("Please enter the full path to the music directory.")
            self.terminal_length = input("Please enter the length, by count of characters, of your terminal.")
            user_string_list = ""
            for i in range(0,len(self.users)):
                user_string_list += self.users[i] + ", "

            with open("Settings.txt", "w") as f:
                f.write("users: " + user_string_list + "\n" + "directory: " + self.Directory + "\n" + "size: " + self.terminal_length + "\n")


        if user.lower() in self.users:
            self.user = user.lower()
            print(buffer+f"Hello, {self.user.lower()}! I have some music for you!")
        else:
            self.user = "guest"
            print(buffer+f"Hello, {self.user}! I don't know you, but I hope you have fun!")
        print(buffer+ "... loading, please wait ...")
        self.queue = []
        self.songs = []
        self.songnames = []
        self.playlistnames = []
        self.playlistInhalts = []
        self.playedsongs = []
        self.artistnames = []
        #self.playing = False


        #checking .json file integrity
        # if only one is empty, the other is copied over immediately. This should prevent
        # the .json files from being deleted by quitting the program at an inoppurtune time
        jsonNonempty = False
        backupjsonNonempty = False
        with open("Songs.json", "r") as f:
            for x in f:
                if x != "":
                    jsonNonempty = True

        with open("songsbackup.json", "r") as f:
            for x in f:
                if x != "":
                    backupjsonNonempty = True

        if jsonNonempty ^ backupjsonNonempty:
            if jsonNonempty:
                with open("Songs.json", "r") as f:
                    out_dict = json.load(f)
                with open("songsbackup.json", "w") as f:
                    json_obj = json.dumps(out_dict, indent=4)
                    f.write(json_obj)
            else:
                with open("songsbackup.json", "r") as f:
                    out_dict = json.load(f)
                with open("Songs.json", "w") as f:
                    json_obj = json.dumps(out_dict, indent=4)
                    f.write(json_obj)


        #updating the songs directory to not break anything if names get changed or songs get added/
        #removed, etc
        directory = os.fsencode(self.Directory)
        t = time.time()
        song_count = 0
        song_bytes = 0

        with open("Playlists.txt", "r") as f:
            for x in f:
                split_names = x.split("±")
                self.playlistInhalts.append([x.split("±")[2:]])
                self.playlistnames.append(x.split("±")[1])
        with open("Input.txt", "w") as f:
            f.write("")

        #as fast as i can get this rn. still unfortunately slow - it takes 6 seconds to read in 1200 songs.
        jsonNonempty = False
        with open("Songs.json", "r") as f:
            for x in f:
                if x != "":
                    jsonNonempty = True
        if jsonNonempty:
            with open("Songs.json", "r") as f:
                out_dict = json.load(f)
        else:
            out_dict = {}
        with open("songsbackup.json", "w") as f:
            json_obj = json.dumps(out_dict, indent=4)
            f.write(json_obj)
        song_count = 0
        for file in os.listdir(directory):
            song_bytes += os.stat(directory+file).st_size
            song_count += 1
            file = str(file, "utf-8")
            if file not in out_dict.keys():
                split_file = file.split("-")
                if split_file != [".DS_Store"]:
                    if split_file[0][-1] == " ":
                        artist = split_file[0][:-1]
                    else:
                        artist = split_file[0]
                    if len(split_file) == 0:
                        print(file, split_file, "!!!!!")
                    elif len(split_file) == 2:
                        alblum = " "
                        track = split_file[1].replace(".mp3", "").replace(".opus", "").replace("___", ":").replace("__",
                                                                                                                   "/")
                    elif len(split_file) == 1:
                        # alblum = split_file[1]
                        alblum = " "
                        track = split_file[0].replace(".mp3", "").replace(".opus", "").replace("___", ":").replace("__",
                                                                                                                   "/")
                    elif len(split_file) == 3:
                        alblum = split_file[1]
                        track = split_file[2].replace(".mp3", "").replace(".opus", "").replace("___", ":").replace("__",
                                                                                                                   "/")
                    else:
                        alblum = split_file[1]
                        track = ""
                        for i in range(2, len(split_file) - 1):
                            track += split_file[2]
                        track += split_file[-1].replace(".mp3", "")
                    if track[0] == " ":
                        track = track[1:]
                    out_dict.update({file:{"song": track, "artist":artist, "album":alblum, "filename":file, "genre":[], "lyrics":{}, "notes": ""}})
                    self.artistnames.append(artist)
                    self.songnames.append(track)
                    self.songs.append(file)
            else:
                self.artistnames.append(out_dict[file]["artist"])
                self.songnames.append(out_dict[file]["song"])
                self.songs.append(file)

            with open("Songs.json", "w") as f:
                json_obj = json.dumps(out_dict, indent=4)
                f.write(json_obj)
        print(buffer + f"Song library ({song_count} songs!) up-to-date in only {np.round(time.time() - t, 6)} seconds!")

        # code for rendering bytes into something vaguely readable
        if song_bytes / 10 ** 9 > 1:
            size_unit_songs = "Gigabytes"
            song_bytes = np.round(song_bytes / 10 ** 9, 3)
        elif song_bytes / 10 ** 6 > 1:
            size_unit_songs = "Megabytes"
            song_bytes = np.round(song_bytes / 10 ** 6, 3)
        elif song_bytes / 10 ** 3 > 1:
            size_unit_songs = "Kilobytes"
            song_bytes = np.round(song_bytes / 10 ** 3, 3)
        else:
            size_unit_songs = "Bytes"
        print(buffer + f"The size of the current library is {song_bytes} {size_unit_songs}!")
        print(buffer + f"Please type 'help' or 'help COMMAND_NAME' for command information.")


    def printSong(self, song):
        song = song.replace(".mp3", "").replace(".opus", "").replace(".wav", "").replace("___", ":").replace("__","/")
        artist, name = song.split("-")[0], song.split("-")[1]
        if name[-1] == " ":
            name = name[0:-1]
        if artist[-1] == " ":
            artist = artist[0:-1]
        if name[0] == " ":
            name = name[1:]
        if artist[0] == " ":
            artist = artist[1:]
        return f"{name}, by {artist}"

    def loglen(self, song, time):
        if ".mp3" in song:
            try:
                pygame.mixer.music.load(self.Directory + song)
                song = MP3(self.Directory + song)
                songLength = song.info.length
                pygame.mixer.music.unload()
                return float(time)/songLength*np.log(songLength)
            except pygame.error:
                return 0
        elif ".opus" in song:
            pygame.mixer.music.load(self.Directory + song)
            song = OggOpus(self.Directory + song)
            songLength = song.info.length
            pygame.mixer.music.unload()
            return float(time) / songLength * np.log(songLength)
        else:
            return 0

    def numlistens(self, song, time):
        if ".mp3" in song:
            try:
                pygame.mixer.music.load(self.Directory + song)
                song = MP3(self.Directory + song)
                songLength = song.info.length
                pygame.mixer.music.unload()
                return float(time) / songLength
            except pygame.error:
                return 0
        elif ".opus" in song:
            pygame.mixer.music.load(self.Directory + song)
            song = OggOpus(self.Directory + song)
            songLength = song.info.length
            pygame.mixer.music.unload()
            return float(time) / songLength
        else:
            return 0

    def run(self):
        pygame.mixer.init()
        main = True
        paused = False
        EradicateFile = False
        usr_input = ""
        saved_usr_input = ""
        prev_print = ""
        while main:
            t = time.time()
            time.sleep(.01)
            with (open("Input.txt") as f):
                for x in f:
                    if x != saved_usr_input:
                        saved_usr_input = x
                        usr_input = x
                        prev_print = ""
                        EradicateFile = True
                    else:
                        usr_input = ""
            if EradicateFile:
                with open("Input.txt", "w") as f:
                    f.write("@@@")
                EradicateFile = False

            #start of the input parser code. input is drawn from userInput.py as usr_input, and parsed
            #via the following wall of code if the beginning characters match the key words
            if usr_input == "":
                pass
            elif "add" in usr_input[0:3]:
                playlist_name = usr_input.split(" ")[1]
                f = open("Playlists.txt", "r")
                playlists = []
                count_playlists = 0
                for x in f:
                    playlists.append(x.split("±"))
                    count_playlists += 1
                f.close()
                while ['\n'] in playlists:
                    playlists.remove(['\n'])
                    count_playlists -= 1
                names = [playlists[i][1] for i in range(0, len(playlists))]
                if playlist_name in names:
                    main = True
                    fix = True
                    playlist = ""
                    for x in playlists[names.index(playlist_name)]:
                        if x != "\n":
                            playlist += x + "±"
                    '''else:
                        main = False
                        print(buffer + "I found it but the wrong person is signed in :((")
                        fix = False'''
                else:
                    main = False
                    print(buffer + "oops. can't find that one. Try again?")
                    fix = False
                _song = usr_input.replace("add " + playlist_name + " ", "")
                print(buffer + _song)
                if _song in self.songnames:
                    if _song not in playlist:
                        playlist += _song + "±"
                    else:
                        print(buffer + "Already there you fool. Use the full playlist editor to override.")
                else:
                    print(buffer + "Didn't recognise song :((")

                if fix:
                    #print(playlist)
                    f = open("Playlists.txt", "r")
                    rewrite = []
                    for x in f:
                        count_playlists -= 1
                        if count_playlists >= 1:
                            if x.split("±")[0] != self.user or x.split("±")[1] != playlist_name:
                                rewrite.append(copy.deepcopy(x))
                            else:
                                rewrite.append(playlist + "\n")
                        else:
                            if x.split("±")[0] != self.user or x.split("±")[1] != playlist_name:
                                rewrite.append(copy.deepcopy(x))
                            else:
                                rewrite.append(playlist.replace("±±", "±"))
                    f.close()
                    f = open("Playlists.txt", "w")
                    for x in rewrite:
                        f.write(x)
                    f.close()
                    self.playlistnames = []
                    self.playlistInhalts = []
                    with open("Playlists.txt", "r") as f:
                        for x in f:
                            split_names = x.split("±")
                            self.playlistInhalts.append([x.split("±")[2:]])
                            self.playlistnames.append(x.split("±")[1])
                    usr_input = ""
            elif "qadd" in usr_input[0:4]:
                playlist_name = usr_input.split(" ")[1]
                f = open("Playlists.txt", "r")
                playlists = []
                count_playlists = 0
                for x in f:
                    playlists.append(x.split("±"))
                    count_playlists += 1
                f.close()
                while ['\n'] in playlists:
                    playlists.remove(['\n'])
                    count_playlists -= 1
                names = [playlists[i][1] for i in range(0, len(playlists))]
                if playlist_name in names:
                    #print(playlists[names.index(playlist_name.lower())])
                    if playlists[names.index(playlist_name)][0] == self.user:
                        main_one = True
                        fix = True
                        playlist = ""
                        for x in playlists[names.index(playlist_name)]:
                            if x != "\n":
                                playlist += x + "±"
                    else:
                        main_one = False
                        print(buffer + "I found it but the wrong person is signed in :((")
                        fix = False
                else:
                    main_one = False
                    print(buffer + "oops. can't find that one. Try again?")
                    fix = False
                if main_one:
                    print(song)
                    if song[-1] == " ":
                        _song = song[-1]
                    else:
                        _song = song
                    if _song[0] == " ":
                        _song = _song[1:]
                    if _song in self.songnames:
                        playlist += _song + "±"
                    else:
                        print(buffer + "Didn't recognise song :((")
                    print(_song)
                    print(song)

                if fix:
                    #print(playlist)
                    f = open("Playlists.txt", "r")
                    rewrite = []
                    for x in f:
                        count_playlists -= 1
                        if count_playlists >= 1:
                            if x.split("±")[0] != self.user or x.split("±")[1] != playlist_name:
                                rewrite.append(copy.deepcopy(x))
                            else:
                                rewrite.append(playlist + "\n")
                        else:
                            if x.split("±")[0] != self.user or x.split("±")[1] != playlist_name:
                                rewrite.append(copy.deepcopy(x))
                            else:
                                rewrite.append(playlist.replace("±±", "±"))
                    f.close()
                    f = open("Playlists.txt", "w")
                    for x in rewrite:
                        f.write(x)
                    f.close()
                    self.playlistnames = []
                    self.playlistInhalts = []
                    with open("Playlists.txt", "r") as f:
                        for x in f:
                            split_names = x.split("±")
                            self.playlistInhalts.append([x.split("±")[2:]])
                            self.playlistnames.append(x.split("±")[1])
                    usr_input = ""
            elif "pause" in usr_input[0:5] or "stop" in usr_input[0:4]:
                pygame.mixer.music.pause()
                paused = True
            elif "shuffle" in usr_input[0:7]:
                random.shuffle(self.queue)
                queue_print_flush = [x.replace(".mp3", "").replace(".opus","") for x in self.queue]
                if len(queue_print_flush) > 10:
                    prev_print = self.prontSquare(
                        queue_print_flush[0:10] + ["... and " + str(len(self.queue) - 10) + " more ..."], prev_print)
                else:
                    prev_print = self.prontSquare(queue_print_flush, prev_print)
            elif "play" in usr_input[0:4] and "playlist" not in usr_input[0:8]:
                if " " not in usr_input:
                    if not paused:
                        if not pygame.mixer.music.get_busy():
                            if len(self.queue) > 0:
                                song = self.queue.pop(0)
                                pygame.mixer.music.load(self.Directory + song)
                                pygame.mixer.music.play()
                                prev_print = self.pront(self.printSong(song), prev_print)
                                self.playedsongs.append(song)
                            else:
                                prev_print = self.pront("no songs in queue", prev_print)
                    else:
                        pygame.mixer.music.unpause()
                        paused = False
                elif "-p " in usr_input.replace("play", ""):
                    if usr_input.replace("play -p", "").replace(" ", "") != "":
                        if usr_input.replace("play -p ", "") in self.playlistnames:
                            for x in self.playlistInhalts[self.playlistnames.index(usr_input.replace("-play -p ", ""))][0]:
                                if x != "":
                                    self.queue.append(self.songs[x])
                                    #self.playedsongs.append(song)
                        #prev_print = self.pront(self.queue, prev_print)
                elif "-ps" in usr_input:
                    if usr_input.replace("play -ps", "").replace(" ", "") != "":
                        if usr_input.replace("play -ps ", "") in self.playlistnames:
                            for x in self.playlistInhalts[self.playlistnames.index(usr_input.replace("play -ps ", ""))][0]:
                                if x != "":
                                    self.queue.append(self.songs[x])
                                    self.playedsongs.append(x)
                            random.shuffle(self.queue)
                            #prev_print = self.pront(self.queue, prev_print)
                elif "-s" in usr_input:
                    if usr_input.replace("play -s ", "") in self.songs:
                        song = usr_input.replace("play -s ", "")
                        pygame.mixer.music.load(self.Directory + song)
                        pygame.mixer.music.play()
                        prev_print = self.pront(self.printSong(song), prev_print)
                        self.playedsongs.append(song)
            elif "rewind" in usr_input[0:6]:
                pygame.mixer.music.rewind()
            elif "songs" in usr_input[0:5]:
                prev_print = self.prontSquare(self.songs, prev_print)
            elif "loop" in usr_input[0:4]:
                num = usr_input.replace("loop ", "")
                if num[2] in ["0","1","2","3","4","5","6","7","8","9"] and num[1] != " ":
                    num = num[0:2]
                elif num[1] in ["0","1","2","3","4","5","6","7","8","9"]:
                    num = num[0:1]
                else:
                    num = num[0]
                if usr_input.replace("loop ", "").replace(num+" ", "") in self.songs:
                    for i in range(0, int(num)):
                        self.queue.insert(0, usr_input.replace("loop ", "").replace(num+" ", ""))
            elif "back" in usr_input[0:4] or "prev" in usr_input[0:4]:
                pygame.mixer.music.unload()
                self.queue.insert(0, self.playedsongs[-1])
                self.playedsongs.remove(self.playedsongs[-1])
                self.queue.insert(0, self.playedsongs[-1])
                song = self.queue.pop(0)
                pygame.mixer.music.load(self.Directory + song)
                pygame.mixer.music.play()
                prev_print = self.pront(self.printSong(song), prev_print)
            elif "next" in usr_input[0:4] or "skip" in usr_input[0:4]:
                if len(self.queue) > 0:
                    pygame.mixer.music.pause()
                    pygame.mixer.music.unload()
                    song = self.queue.pop(0)
                    pygame.mixer.music.load(self.Directory + song)
                    pygame.mixer.music.play()
                    prev_print = self.pront(self.printSong(song), prev_print)
                    self.playedsongs.append(song)
                else:
                    prev_print = self.pront("Nothing to skip to :((", prev_print)
                    pygame.mixer.music.pause()
            elif "kill" in usr_input[0:4] or "quit" in usr_input[0:4]:
                main = False
                pygame.mixer.music.pause()
                paused = True
                f = open("Output.txt", "w")
                f.write("quit")
                f.close()
            elif "playlist" in usr_input[0:8]:
                if "-c" in usr_input:
                    self.create_playlist()
                elif "-e" in usr_input:
                    self.update_playlist(usr_input.replace("playlist -e ", ""))
                elif "-v" in usr_input:
                    for x in self.playlistnames:
                        print(buffer + x)
                elif "-vs" in usr_input:
                    if usr_input.replace("playlist -vs ", "") in self.playlistnames:
                        index = self.playlistnames.index(usr_input.replace("playlist -vs ", ""))
                        for x in self.playlistInhalts[index][0]:
                            print(buffer + x)
                elif "-r" in usr_input:
                    if usr_input.replace("playlist -r ", "") in self.playlistnames:
                        f = open("Playlists.txt", "r")
                        replace = []
                        for x in f:
                            if usr_input.replace("playlist -r ", "") in x[:min(len(x), 10+len(usr_input.replace("playlist -r ", "")))]:
                                pass
                            else:
                                replace.append(x)
                        f.close()
                        f = open("Playlists.txt", "w")
                        for x in replace:
                            f.write(x)
                        f.close()
                        self.playlistnames = []
                        self.playlistInhalts = []
                        with open("Playlists.txt", "r") as f:
                            for x in f:
                                split_names = x.split("±")
                                self.playlistInhalts.append([x.split("±")[2:]])
                                self.playlistnames.append(x.split("±")[1])
            elif "queue" in usr_input[0:5]:
                if "-artist" in usr_input:
                    if usr_input.split("queue -artist ")[1]+" " in self.artistnames:
                        for x in range(0,len(self.songs)):
                            if self.artistnames[x] == usr_input.split("queue -artist ")[1]+" ":
                                self.queue.append(self.songs[x])
                            random.shuffle(self.queue)
                            random.shuffle(self.queue)
                elif "-p" in usr_input and "-ps" not in usr_input:
                    if usr_input.split("-p ")[1] in self.playlistnames:
                        for x in self.playlistInhalts[self.playlistnames.index(usr_input.split("-p ")[1])][0]:
                            if x in self.songs:
                                self.queue.append(self.songs[x])
                elif "-ps" in usr_input:
                    if usr_input.split("-ps ")[1] in self.playlistnames:
                        for x in self.playlistInhalts[self.playlistnames.index(usr_input.split("-ps ")[1])][0]:
                            if x in self.songs:
                                self.queue.append(x)
                        random.shuffle(self.queue)
                        random.shuffle(self.queue)
                elif "-a" in usr_input:
                    for x in self.songs:
                        self.queue.append(x)
                    random.shuffle(self.queue)
                    random.shuffle(self.queue)
                    queue_print_flush = [x for x in self.queue]
                    if len(queue_print_flush) > 10:
                        prev_print = self.prontSquare(
                            queue_print_flush[0:10] + ["... and " + str(len(self.queue) - 10) + " more ..."],
                            prev_print)
                    else:
                        prev_print = self.prontSquare(queue_print_flush, prev_print)
                elif "-v" in usr_input:
                    queue_print_flush = [x for x in self.queue]
                    if len(queue_print_flush) > 10:
                        prev_print = self.prontSquare(queue_print_flush[0:10]+["... and " + str(len(self.queue)-10) + " more ..."], prev_print)
                    else:
                        prev_print = self.prontSquare(queue_print_flush, prev_print)
                elif "-va" in usr_input:
                    queue_print_flush = [x for x in self.queue]
                    prev_print = self.prontSquare(queue_print_flush, prev_print)
                elif "-f" in usr_input:
                    if usr_input.replace("queue -f ", "") in self.songs:
                        self.queue.insert(0, usr_input.replace("queue -f ", ""))
                        print("Aye Aye!")
                        queue_print_flush = [x for x in self.queue]
                        if len(queue_print_flush) > 10:
                            prev_print = self.prontSquare(queue_print_flush[0:10] + ["... and " + str(len(self.queue)-10) + " more ..."], prev_print)
                        else:
                            prev_print = self.prontSquare(queue_print_flush, prev_print)
                elif "-i" in usr_input:
                    if usr_input.replace("queue -i ", "").split(" ")[1:][0] in self.songs:
                        position = usr_input.replace("queue -i ", "").split(" ")[0]
                        _song = usr_input.replace("queue -i ", "").split(" ")[1:][0]
                        self.queue.insert(int(position)-1, _song)
                else:
                    if usr_input.replace("queue ", "") in self.songs:
                        self.queue.append(usr_input.replace("queue ", ""))
            elif "empty" in usr_input[0:5]:
                if usr_input.replace("empty", "").replace(" ", "") != "":
                    while len(self.queue) > int(usr_input.replace("empty", "").replace(" ", "")):
                        self.queue.pop(0)
                else:
                    while len(self.queue) > 0:
                        self.queue.pop(0)
            elif "search" in usr_input[0:6]:
                if "-a" in usr_input and "-not-latin" not in usr_input and "-as" not in usr_input:
                    term = usr_input.replace("search -a ", "")
                    for x in self.artistnames:
                        if term in x:
                            prev_print = self.pront(x, prev_print)
                elif "-as" in usr_input and "-not-latin" not in usr_input:
                    term = usr_input.replace("search -as ", "")
                    print(term)
                    for x in self.songs:
                        if term in x:
                            prev_print = self.pront(x, prev_print)
                elif "-a" in usr_input and "-not-latin" in usr_input:
                    chars = [chr(i) for i in range(97, 97 + 26 + 1)] + [chr(i) for i in range(65, 65 + 26)]
                    for x in self.artistnames:
                        dont_print = False
                        for art_char in x:
                            if art_char in chars:
                                dont_print = True
                        if not dont_print:
                            prev_print = self.pront(x, prev_print)
                elif "-not-latin" in usr_input:
                    chars = ([chr(i) for i in range(97, 97 + 26 + 1)] + [chr(i) for i in range(65, 65 + 26)]
                             + [str(i) for i in range(0,10)]
                             + [" ", ",", ".", "'", "(", ")", "$", "#", "&", "!", "?", ":", ";", "_", "/", "[", "]"]
                             + ["á", "é", "ó", "í", "ú", "ä", "ë", "ü", "ö", "å", "ß"])
                    for x in self.songnames:
                        dont_print = True
                        for song_char in x:
                            if song_char not in chars:
                                dont_print = False
                                break
                        if not dont_print:
                            prev_print = self.pront(x, prev_print)
                elif "-not-english" in usr_input:
                    chars = ([chr(i) for i in range(97, 97 + 26 + 1)] + [chr(i) for i in range(65, 65 + 26)]
                             + [str(i) for i in range(0,10)]
                             + [" ", ",", ".", "'", "(", ")", "$", "#", "&", "!", "?", ":", ";", "_", "/", "[", "]"])
                    for x in self.songnames:
                        dont_print = True
                        for song_char in x:
                            if song_char not in chars:
                                dont_print = False
                                break
                        if not dont_print:
                            prev_print = self.pront(x, prev_print)
                else:
                    term = usr_input.replace("search ", "")
                    for x in self.songs:
                        if term in x:
                            prev_print = self.pront(x, prev_print)
            elif "help" in usr_input[0:4]:
                if usr_input.replace("help", "").replace(" ", "") == "":
                    self.printGeneralHelp()
                else:
                    self.printSpecificHelp(usr_input.replace("help ", ""))
            elif "monthly" in usr_input[0:7]:
                if usr_input.replace("monthly", "").replace(" ","") == "":
                    self.MonthlyListeningStats(10, "de")
                else:
                    if "-log" in usr_input:
                        if usr_input.replace("monthly -log", "").replace(" ","") != "":
                            self.MonthlyListeningStats(int(usr_input.replace("monthly -log ", "")), "ln")
                        else:
                            self.MonthlyListeningStats(10, "ln")
                if "-clear" in usr_input:
                    if self.user != "guest":
                        current_stats = []
                        with open("ShortTermAnalytics.txt", "r") as file:
                            for x in file:
                                current_stats.append(x)
                        for i in range(0,len(current_stats)):
                            if self.user in current_stats[i][0:20]:
                                user_index = copy.deepcopy(i)
                        with open("ShortTermAnalytics.txt", "w") as file:
                            #f.write(" ")
                            for i in range(0, len(current_stats)):
                                if i != user_index:
                                    file.write(current_stats[i])
                    else:
                        prev_print = self.pront("Sorry!! I don't know who you are :(( So I can't get rid of your listening data", prev_print)
            #anything labelled dev.____ is meant only for the developer, me!
            #and i guess you too if you took the time to read through this code <3
            #these do things like check randomness (qallanalytics), add to internal bug repots, etc
            elif "dev.bugs" in usr_input[0:8]:
                with open("bugs.txt", "r") as f:
                    for x in f:
                        prev_print = self.pront(x, prev_print)
            elif "dev.qallanalytics" in usr_input[0:17]:
                pass
                """pygame.mixer.music.stop()
                self.queue = []
                self.artistnames = []
                self.songnames = []
                self.songs = []
                with open("Songs.txt", "r") as f:
                    for x in f:
                        self.artistnames.append(x.split("±")[1][0:])
                        self.songnames.append(x.split("±")[3][1:])
                        self.songs.append(x.split("±")[:-1])
                song_places = [(self.songs[i], []) for i in range(0, len(self.songs))]
                song_places_places = [self.songs[i] for i in range(0, len(self.songs))]
                LOOP_C = 2000
                for i in range(0,LOOP_C):
                    self.queue = []
                    self.artistnames = []
                    self.songnames = []
                    self.songs = []
                    print(i)
                    with open("Songs.txt", "r") as f:
                        for x in f:
                            self.artistnames.append(x.split("±")[1][0:])
                            self.songnames.append(x.split("±")[3][1:])
                            self.songs.append(x.split("±")[:-1])
                    for x in self.songs:
                        self.queue.append(x)
                    random.shuffle(self.queue)
                    random.shuffle(self.queue)
                    for j in range(0,len(self.queue)):
                        song_places[song_places_places.index(self.queue[j])][1].append(j)
                xs = []
                xs_m = []
                for i in range(0,min(1000, len(song_places_places))):
                    xs_m.append(i)
                    for j in range(0, LOOP_C):
                        xs.append(i)
                ys = []
                ys_m = []
                for i in range(0,min(1000, len(song_places))):
                    ys_m.append(sum(song_places[i][1])/LOOP_C)
                    for j in range(0, len(song_places[i][1])):
                        ys.append(song_places[i][1][j])

                plt.scatter(xs,ys)
                plt.plot(xs_m, ys_m, color="red")
                plt.show()"""
            elif "dev.bugs" in usr_input[0:8]:
                self.updateBugs(usr_input.replace("dev.bugs ", ""))
            elif "dev.to-add" in usr_input[0:11]:
                if "-v" in usr_input:
                    with open("To_Add.txt", "r") as f:
                        for x in f:
                            prev_print = self.pront(x, prev_print)
                else:
                    self.updateToAdd(usr_input.replace("dev.to-add ", ""))
            elif "dev.version" in usr_input[0:11]:
                self.shittyInternalVersionControl()
            elif "complete" in usr_input[0:8]:
                self.HowCompleteLibrary()
            elif "new-user" in usr_input[0:8]:
                print(self.users)
                if usr_input.replace("new-user ", "").lower() in self.users:
                    self.user = usr_input.replace("new-user ", "").lower()
                    prev_print = self.pront(f"Hello there, {self.user.lower()}!", prev_print)
                else:
                    print(f"Sorry! I don't recognise you!!, User is still {self.user}")
            elif "stats" in usr_input[0:5]:
                if "-clear" in usr_input:
                    if self.user != "guest":
                        current_stats = []
                        with open("Analytics.txt", "r") as file:
                            for x in file:
                                current_stats.append(x)
                        for i in range(0, len(current_stats)):
                            if self.user in current_stats[i][0:20]:
                                user_index = copy.deepcopy(i)
                        with open("Analytics.txt", "w") as file:
                            # f.write(" ")
                            for i in range(0, len(current_stats)):
                                if i != user_index:
                                    file.write(current_stats[i])
                    else:
                        prev_print = self.pront(
                            "Sorry!! I don't know who you are :(( So I can't get rid of your listening data",
                            prev_print)
                else:
                    self.AnalyseItAll()
            elif "update-lyrics" in usr_input[0:13]:
                if "-ua" in usr_input:
                    self.Lyrics(is_spoof_agents=True)
                elif "-n" in usr_input:
                    self.Lyrics(none_lyrics=True)
                else:
                    self.Lyrics()
                self.HowCompleteLibrary()
            elif "text-to-lyrics" in usr_input[0:14]:
                l_track = usr_input.replace("text-to-lyrics ", "")
                self.TxtToLyrics(l_track, "songlyrics.txt")
            elif "genres" in usr_input[0:6]:
                self.find_genres()
            elif "lyrics" in usr_input[0:6]:
                self.printLyrics(song)
            elif "settings" in usr_input[0:8]:
                self.updateSettings()
            elif "done" in usr_input[0:4]:
                prev_print = self.pront("Menu Exited!", prev_print)
            elif usr_input == "@@@":
                pass
                #this keeps the program from printing 'sorry bestie!...' consistently
                #idk why its load bearing :[
                # i know why its load bearing actually. its because usr_input is initialised to this
                # if its nonzero
            else:
                prev_print = self.pront("Sorry bestie!! I didn't get that command!", prev_print)
            if self.user != "guest":
                if pygame.mixer.music.get_busy():
                    self.analytics(self.user, song, time.time()-t, "Analytics.txt")
                    self.analytics(self.user, song, time.time() - t, "ShortTermAnalytics.txt")
            if not pygame.mixer.music.get_busy() and not paused:
                if len(self.queue) > 0:
                    song = self.queue.pop(0)
                    pygame.mixer.music.load(self.Directory + song)
                    pygame.mixer.music.play()
                    self.playedsongs.append(song)
                    prev_print = self.pront(self.printSong(song), prev_print)
                    #print(">> ", end="")
    def create_playlist(self):
        if self.user != "guest":
            name = ""
            print("What do you want to name it?")
            with open("Input.txt", "w") as f:
                f.write("")
            while name == "" or name == "playlist -c":
                with open("Input.txt", "r") as f:
                    for x in f:
                        if x != "" and x != "playlist -c":
                            name = x
            f = open("Playlists.txt", "a")
            f.write(self.user + "±" + name + "±" + "\n")
            f.close()
            self.playlistnames = []
            self.playlistInhalts = []
            with open("Playlists.txt", "r") as f:
                for x in f:
                    print("x: ", x)
                    if x.replace(" ", "").replace("\n", "") != "":
                        split_names = x.split("±")
                        self.playlistInhalts.append([x.split("±")[2:]])
                        self.playlistnames.append(x.split("±")[1])
        else:
            print("Sorry bestie, I can't let you do that :(( You're a guest, and I don't have that much memory space.")

    def update_playlist(self, name):
        f = open("Playlists.txt", "r")
        playlists = []
        count_playlists = 0
        for x in f:
            playlists.append(x.split("±"))
            count_playlists += 1
        f.close()
        while ['\n'] in playlists:
            playlists.remove(['\n'])
            count_playlists -= 1
        names = [playlists[i][1] for i in range(0,len(playlists))]
        if name in names:
            #print(buffer + str(playlists[names.index(name.lower())]))
            if playlists[names.index(name)][0] == self.user:
                main = True
                fix = True
                playlist = ""
                for x in playlists[names.index(name)]:
                    if x != "\n":
                        playlist += x + "±"
            else:
                main = False
                print(buffer + "I found it but the wrong person is signed in :((")
                fix = False
        else:
            main = False
            print(buffer + "oops. can't find that one. Try again?")
            fix = False

        while main:
            self.prontSquare(playlist.split("±")[2:], "")
            print(buffer + "<playlist actions?>")
            action = ""
            with open("Input.txt", "w") as f:
                f.write("")
            while action == "":
                with open("Input.txt", "r") as f:
                    for x in f:
                        if x != "":
                            action = x
            if action.lower().replace(" ","") == "add":
                #print(self.songnames)
                print(buffer + "What song? >> ")
                song = ""
                with open("Input.txt", "w") as f:
                    f.write("")
                while song == "":
                    with open("Input.txt", "r") as f:
                        for x in f:
                            if x != "":
                                song = x
                if song in self.songs:
                    if song in playlist:
                        print(buffer + "It's already here. Type 'yes' or 'y' to add it again. >> ")
                        confirm = ""
                        with open("Input.txt", "w") as f:
                            f.write("")
                        while confirm == "":
                            with open("Input.txt", "r") as f:
                                for x in f:
                                    if x != "":
                                        confirm = x
                        if confirm.lower() in ["yes", "y"]:
                            playlist += song + "±"
                    else:
                        playlist += song + "±"
                else:
                    print(buffer + "Sorry I can't find that song")
            elif "add" in action.lower()[0:3]:
                song = action.replace("add ","")
                if song in self.songs:
                    playlist += song + "±"
                else:
                    print(buffer + "Didn't recognise song :((")
            elif action.lower().replace(" ","") == 'remove':
                print(buffer + "What song?")
                song = ""
                with open("Input.txt", "w") as f:
                    f.write("")
                while song == "":
                    with open("Input.txt", "r") as f:
                        for x in f:
                            if x != "":
                                song = x
                if song in playlist:
                    playlist = playlist.replace(song+"±", "")
            elif "remove" in action[0:6].lower():
                song = action.replace("remove ", "")
                if song in playlist:
                    playlist = playlist.replace(song+"±", "")
                else:
                    print(buffer+"no such song exists")
            elif action.lower().replace(" ","") == "reorder":
                print(buffer + playlist)
                print(buffer + "What is song one?")
                with open("Input.txt", "w") as f:
                    f.write("")
                while song1 == "":
                    with open("Input.txt", "r") as f:
                        for x in f:
                            if x != "":
                                song1 = x
                with open("Input.txt", "w") as f:
                    f.write("")
                print(buffer + "What is song two?")
                while song2 == "":
                    with open("Input.txt", "r") as f:
                        for x in f:
                            if x != "":
                                song2 = x
                if song1 in playlist and song2 in playlist:
                    playlist.replace(song1, "aaa123654hkjlasdjkhfieqwryp,namxvTEMPORARYPLACEHOLDER")
                    playlist.replace(song2, song1)
                    playlist.replace("aaa123654hkjlasdjkhfieqwryp,namxvTEMPORARYPLACEHOLDER", song2)
                else:
                    print(buffer + "Sorry! Didn't recognise one or both of the names!")
            elif action.lower().replace(" ","") == "search":
                print(buffer + "Search terms?")
                terms = ""
                with open("Input.txt", "w") as f:
                    f.write("")
                while terms == "":
                    with open("Input.txt", "r") as f:
                        for x in f:
                            if x != "":
                                terms = x
                for x in self.songs:
                    if terms in x:
                        print(buffer + x)
                print(buffer + "---")
            elif "search" in action[0:6]:
                if "-as" in action:
                    for x in self.songs:
                        if action.replace("search -as ", "") in x:
                             self.pront(x, "")

                else:
                    search_term = action.replace("search ", "")
                    for x in self.songs:
                        if search_term in x:
                            print(buffer + x)
                print(buffer + "---")
            elif action.lower().replace(" ","") == "done" or action.lower().replace(" ","") == "quit":
                main = False
            else:
                print(buffer + "Sorry, I don't understand that. I understand: 'add', 'remove', 'search', '"
                               "reorder', 'done'. and 'quit'")
        if fix:
            print(buffer + playlist)
            f = open("Playlists.txt", "r")
            rewrite = []
            for x in f:
                count_playlists -= 1
                if count_playlists >= 1:
                    if x.split("±")[0] != self.user or x.split("±")[1] != name:
                        rewrite.append(copy.deepcopy(x))
                    else:
                        rewrite.append(playlist + "\n")
                else:
                    if x.split("±")[0] != self.user or x.split("±")[1] != name:
                        rewrite.append(copy.deepcopy(x))
                    else:
                        rewrite.append(playlist.replace("±±", "±"))
            f.close()
            f = open("Playlists.txt", "w")
            for x in rewrite:
                f.write(x)
            f.close()
            self.playlistnames = []
            self.playlistInhalts = []
            with open("Playlists.txt", "r") as f:
                for x in f:
                    split_names = x.split("±")
                    self.playlistInhalts.append([x.split("±")[2:]])
                    self.playlistnames.append(x.split("±")[1])
            usr_input = ""

    def shuffle(self, playlist):
        random.shuffle(playlist)

    def pront(self, thing, check):
        terminal_length = self.terminal_length
        if thing != check:
            if len(thing)+len(buffer) <=terminal_length:
                print(buffer+thing)
            else:
                thinglist = thing.split(" ")
                printflush = ""
                for i in range(0, len(thinglist)):
                    if len(printflush+buffer+thinglist[i]) <= terminal_length:
                        printflush += thinglist[i] + " "
                    else:
                        print(buffer+printflush)
                        printflush = thinglist[i]
                print(buffer+printflush)

            return thing
        else:
            return check

    def prontSquare(self, things, check):
        terminal_length = self.terminal_length
        internal_buffer = 10
        print_flush = ""
        if things != check:
            for thing in things:
                if len(thing)+len(print_flush)+internal_buffer+len(buffer) <= terminal_length:
                    print_flush += thing + " "*internal_buffer
                else:
                    print(buffer+print_flush)
                    if len(thing)+ len(buffer) + internal_buffer <= terminal_length:
                        print_flush = thing + " "*internal_buffer
                    elif len(thing)+ len(buffer) <= terminal_length:
                        print_flush = thing
                    else:
                        print_flush = ""
                        thingys = thing.split(" ")
                        for thingy in thingys:
                            if len(thingy) + len(print_flush) + len(buffer) <= terminal_length:
                                print_flush += thingy + " "
                            else:
                                print(buffer + print_flush)
                                print_flush = thingy
                        if len(print_flush) + len(buffer) + internal_buffer <= terminal_length:
                            print_flush += " "*internal_buffer
                        else:
                            print(buffer+print_flush)
                            print_flush = ""
            if print_flush != "":
                print(buffer+print_flush)
            return things
        else:
            return check

    def printSpecificHelp(self, command):
        print(buffer + "STR and INT refer to a user-specified string or integer, respectively")
        format = 5
        help_list = [["add"], ["STR STR_"], ["If playlist owner is the current user, then adds the song STR to the playlist STR_"],
                     [["back", "prev"], [""],
                      ["shunts current song to the front of the queue, and then plays the previous song."]],
                     [["complete"], [""], ["Loops through the songs.json file, counting which songs have non-empty lyrics and genres."]],
                     [["done"], [""], ["If in a menu (settings, playlists, etc), quits that menu."]],
                     [["empty"], ["No args", "INT"],
                      ["Empties the queue.", "Empties the queue from the front until there are INT songs remaining."]],
                     [["genres"], [""], ["Updates the song genres in songs.json by reading the song metadata, for each song in the library."]],
                     [["help"], ["no args", "STR"],
                      ["Prints summary of commands.", "Prints specific description of command STR, including usage and arguments."]],
                     [["kill", "quit"], [""], ["quits music player and parser."]],
                     [["loop"], ["INT<10"], ["queues the following song INT number of times."]],
                     [["lyrics"], [""], ["Prints lyrics of song currently in player. If no lyrics exist, prints nothing."]],
                     [["monthly"], ["No args", "-log", "-clear"],
                      ["Returns recent listening stats, styled like a receipt, by time listened to each song.",
                       "Returns recent listening stats, styled like a receipt, by the log of the number of listens.",
                       "Clears current user's recent listening stats. Fails if user is a guest."]],
                     [["new-user"], ["STR"], ["If STR in the list of users, switches to that user, updating analytics essentially immediately"]],
                     [["next", "skip"], [""], ["skips the current song, plays the next one from the queue."]],
                     [["pause", "stop"], [""], ["Pauses internal music player. Does not unload current song."]],
                     [["play"], ["No args", "-p STR", "-ps STR", "-s STR"],
                      ["Plays or unpauses the music player. Loads it as necessary from the queue. If there are no songs in queue, prints that.",
                       "Plays a playlist (STR) by appending it to the queue, and then shuffling the queue.",
                       "Plays a song (STR) without appending to the queue. Will not autoplay."]],
                     [["playlist"], ["", "-c", "-e STR", "-r STR", "-v"],
                      ["Command for working with playlists. Saves them to a text file as a string of local song paths.",
                       "Creates new playlist. Will prompt for a name.", "Edits the playlist specified after the argument (STR).",
                       "Removes the playlist specified playlist in the argument (STR).", "Displays all current playlists, without editing access."]],
                     [["qadd"], ["STR"], ["Adds the song currently in the player (playing or paused) to the playlist STR,"
                                          "if the current user is the owner of that playlist."]],
                     [["queue"], ["", "STR", "-a", "-f STR", "-i INT", "-p STR", "-v", "-va", "-artist STR"],
                      ["Command for queueing songs. Requires args.",
                       "If followed by a song (STR), queues that song.",
                       "Puts every song in the library in the queue, randomly, and prints queue",
                       "Puts the following song (STR) in the front of the queue.",
                       "Puts the following song at the place specified in the queue by the INT.",
                       "Queues the playlist (STR) specified.",
                       "Prints first 10 songs of current queue.", "Prints ALL of current queue.",
                       "Queues every song by STR in library and shuffles queue."
                       ]],
                     [["rewind"], [""], ["Rewinds internal music player. Does not unload current song or change queue."]],
                     [["search"], ["STR", "-a STR", "-as STR", "-not-latin", "-not-english"],
                      ["Searches through the song library for the specified string STR",
                       "Searches through the song library artists' for the string STR",
                       "Searches through the song library artists' for STR, prints their songs.",
                       "Searches through the song library for any song containing a character not in the english alphabet + characters with fadas or umlauts.",
                       "Searches through the song library for any song containing a character not easily found on a US keyboard layout"]],
                     [["settings"], [""], ["Opens the settings menu. Allows user to update the settings file."]],
                     [["shuffle"], [""], ["Shuffles current queue using random.shuffle()."]],
                     [["songs"], [""], ["prints the entirety of the songs library in the working directory."]],
                     [["stats"], ["No args", "-clear"],
                      ["Returns long-term listening stats, including time listened to songs, number of listens to songs, most listened to artist, and most listened to genre",
                       "Clears current user's long-term listening stats (stored in Analytics.txt). Fails if user is a guest."]],
                     [["text-to-lyrics"], ["STR"], "Turns the contents of the songlyrics.txt file into song lyrics for the song STR, stored in Songs.json. Does some minor formatting to make it more readable"],
                     [["update-lyrics"], ["no args", "-ua", "-n"],
                      ["The only part of this code that requires an active internet connection. And a vpn is HIGHLY SUGGESTED"
                       "for running this code. This scours various lyrics websites to find the lyrics for songs in the library, and saves those lyrics to"
                       "songs.json.",
                       "Runs the same code, but spoofs the user-agent of the client. Slightly more consistent in avoiding 403 errors.",
                       "Runs the same code, but if a song's lyrics are stored as 'None :((', it attempts to update them."]]]
        if self.terminal_length > len(buffer + format * " ") + 15:
            print(command+".")
            for i in range(0,len(help_list)):
                for j in range(0,len(help_list[i][0])):
                    if command==help_list[i][0][j]:
                        print_flush = buffer + help_list[i][0][j] + format*" "
                        for k in range(0,len(help_list[i][1])):
                            print_flush += help_list[i][1][k] + " "
                            if len(print_flush + help_list[i][2][k]) < self.terminal_length:
                                print_flush += help_list[i][2][k]
                                print(print_flush)
                            else:
                                split_help_list = help_list[i][2][k].split(" ")
                                for l in range(0, len(split_help_list)):
                                    if len(print_flush + split_help_list[l]) < self.terminal_length:
                                        print_flush += split_help_list[l] + " "
                                    else:
                                        print(print_flush)
                                        print_flush = buffer + format*" " + split_help_list[l] + " "
                                print(print_flush)
        else:
            print("Terminal Size too small to make this look nice")
            for i in range(0,len(help_list)):
                for j in range(0,len(help_list[i][0])):
                    if command==help_list[i][0][j]:
                        print(buffer + help_list[i][0][j])
                        for k in range(help_list[i][1]):
                            print(buffer + help_list[i][1][k] + " " + help_list[i][2][k])



    def printGeneralHelp(self):
        format = 5 + 14 #buffer + max.len
        help_list = [("add", "Adds a song to a playlist. Playlist owner must be signed in."),
                     ("back", "Goes to previous song."),
                     ("complete", "Prints the number of songs with lyrics and genres in Library."),
                     ("done", "Quits all submenus."),
                     ("empty", "Clears queue."),
                     ("genres", "Scours song metadata for genre information."),
                     ("help", "Yields command information. Rather useless. <3"),
                     ("kill", "Quits the jukebox."),
                     ("loop", "Plays the following song n times. Requires args."),
                     ("lyrics", "Prints lyrics of current song, if available."),
                     ("monthly", "Returns short-term listening stats."),
                     ("new-user", "requires args. switches to a new user."),
                     ("next", "Skips to next song."),
                     ("pause", "Pauses music."),
                     ("play", "Plays music, or resumes playing."),
                     ("playlist", "Command for editing playlists. Requires args."),
                     ("prev", "Identical to 'back'."),
                     ("qadd", "Quick adds a song to a playlist. Playlist owner must be signed in."),
                     ("queue", "Command for queueing songs. Requires args."),
                     ("quit", "Identical to 'kill'."),
                     ("rewind", "Rewinds current song to its beginning."),
                     ("search", "Searches through songs library. Requires args."),
                     ("settings", "Opens the settings menu."),
                     ("shuffle", "Shuffles the current queue."),
                     ("skip", "Identical to 'next'."),
                     ("songs", "Prints the full name of every song in the library."),
                     ("stats", "Prints long-term analytics."),
                     ("stop", "Identical to 'pause'."),
                     ("text-to-lyrics", "Turns the contents of the songlyrics.txt file into song lyrics. requires args."),
                     ("update-lyrics", "Scours the web for song lyrics in batches of 20.")]
        dev_help_list = [("bugs", "Appends following args to the bugs file."),
                         ("to-add", "Add following args to the to_add file."),
                         ("version", "Prints various versions and their changes.")]
        if self.terminal_length > len(buffer + format*" ") + 10:
            for i in range(0, len(help_list)):
                if len(buffer + help_list[i][0] + " "*(format-len(help_list[i][0])) + help_list[i][1]) < self.terminal_length:
                    print(buffer + help_list[i][0] + " "*(format-len(help_list[i][0])) + help_list[i][1])
                else:
                    m = self.terminal_length - len(buffer + help_list[i][0] + " "*(format-len(help_list[i][0])))
                    print_flush = buffer + help_list[i][0] + " "*(format-len(help_list[i][0]))
                    split_help_list = help_list[i][1].split(" ")
                    for j in range(0,len(split_help_list)):
                        if len(print_flush + split_help_list[j]) < self.terminal_length:
                            if j != 0:
                                print_flush += " " + split_help_list[j]
                            else:
                                print_flush += split_help_list[j]
                        else:
                            print(print_flush)
                            print_flush = buffer+format*" "+ split_help_list[j]
                    if print_flush.replace(" ", "") != "":
                        print(print_flush)

        else:
            print("Terminal size is too small to print nicely.")
            for i in range(0, len(help_list)):
                print(buffer + help_list[i][0] + " "*(format-len(help_list[i][0])) + help_list[i][1])
        print()
        print(buffer + "For more specific instructions and arg./kwarg details,")
        print(buffer + "type 'help COMMAND' for any given COMMAND.")
    def analytics(self, user, song, time, analyticsfile):
        f = open(analyticsfile, "r")
        user_in_list = False
        rewriteList = []
        for x in f:
            if user in x:
                analyticsList = x.split("±")
                user_in_list = True
            else:
                if "\n" not in x:
                    x += "\n"
                    rewriteList.append(x)
                else:
                    rewriteList.append(x)
        f.close()
        if not user_in_list:
            f = open(analyticsfile, "a")
            f.write(user)
            f.close()
        else:
            if song in analyticsList:
                analyticsList[analyticsList.index(song)+1] = float(analyticsList[analyticsList.index(song)+1]) + time
            else:
                analyticsList.append(song)
                analyticsList.append(time)
            f = open(analyticsfile, "w")
            for x in rewriteList:
                f.write(x)
            rewrite = ""
            for i in range(0, len(analyticsList)-1):
                rewrite += str(analyticsList[i]) + "±"
            rewrite += str(analyticsList[-1])
            rewrite = rewrite.replace("\n", "")
            if rewrite[-2:-1] != "\n":
                rewrite += "\n"
            f.write(rewrite)
            f.close()

    def AnalyseItAll(self):
        console_size = self.terminal_length
        NUM = 10
        print("-" * console_size)
        top_ten = self.metric_maths("de", NUM, is_full=True)
        self.metric_print(top_ten, console_size, is_full=True)
        print("-"*console_size)
        top_ten = self.metric_maths("num", NUM, is_full=True)
        self.metric_print(top_ten, console_size, is_full=True, in_hms=False)
        print("-" * console_size)
        top_ten_artists = self.artist_maths(10, is_full=True)
        self.metric_print(top_ten_artists, console_size, is_full=True)
        print("-" * console_size)
        top_ten_genres = self.genre_maths(NUM, is_full=True)
        self.metric_print(top_ten_genres, console_size, is_full=True)
        print("-" * console_size)
        self.total_minutes_listened(is_full=True)
        print("-" * console_size)


    def MonthlyListeningStats(self, NUM, METRIC):
        console_size = self.terminal_length
        for i in range(0, 10):
            print()
        print(" "*(int(console_size/2)-int(len("*** KITCHEN ***")/2))+"*** KITCHEN ***")
        print("="*(console_size))
        print("Server: "+self.user)
        print()
        print(" "*(int(console_size/2)-int(len("MUSIC TASTE TEST")/2))+"MUSIC TASTE TEST")
        print()
        print(datetime.datetime.now())
        print("QTY. " + buffer +"NAME." + " "*(console_size-len(buffer)-14) + "AMT.")
        print("=" * (console_size))
        if METRIC == "ln":
            print(2 * buffer + "-log time")
        print()
        top_ten = self.metric_maths(METRIC, NUM)
        self.metric_print(top_ten, console_size, is_full=False)

    def metric_maths(self, METRIC, NUM, is_full=False):
        songslist = []
        top_ten = []
        if is_full:
            with open("Analytics.txt") as f:
                for x in f:
                    songslist.append(x)
        else:
            with open("ShortTermAnalytics.txt") as f:
                for x in f:
                    songslist.append(x)
        if self.user != "guest":
            for i in range(0, len(songslist)):
                if self.user in songslist[i][0:20]:
                    splitsongs = songslist[i].split("±")
                    for i in range(2, len(splitsongs), 2):
                        if "\\n" in splitsongs[i]:
                            splitsongs[i].replace("\\n", "")
                        if METRIC == "de":
                            if top_ten == []:
                                top_ten.append((splitsongs[i - 1], splitsongs[i]))
                            elif len(top_ten) < NUM:
                                vals = [x[1] for x in top_ten]
                                j = 0
                                looping = True
                                while looping:
                                    if float(splitsongs[i]) <= float(vals[j]):
                                        j += 1
                                        if j >= len(vals):
                                            looping = False
                                            top_ten.append((splitsongs[i - 1], splitsongs[i]))
                                    else:
                                        looping = False
                                        top_ten.insert(j, (splitsongs[i - 1], splitsongs[i]))


                            elif len(top_ten) >= NUM:
                                vals = [x[1] for x in top_ten]
                                j = 0
                                looping = True
                                while looping:
                                    if float(splitsongs[i]) <= float(vals[j]):
                                        j += 1
                                        if j >= len(vals):
                                            looping = False
                                            # top_ten.append((splitsongs[i - 1], splitsongs[i]))
                                    else:
                                        # print("ping", j)
                                        looping = False
                                        # top_ten.insert(j, (splitsongs[i - 1], splitsongs[i]))
                                # print(top_ten)
                                if j < len(vals):
                                    top_ten.insert(j, (splitsongs[i - 1], splitsongs[i]))
                                    top_ten.pop(-1)
                        elif METRIC == "ln":
                            if top_ten == []:
                                top_ten.append((splitsongs[i - 1], self.loglen(splitsongs[i - 1], splitsongs[i])))
                            elif len(top_ten) < NUM:
                                vals = [x[1] for x in top_ten]
                                j = 0
                                looping = True
                                while looping:
                                    if self.loglen(splitsongs[i - 1], splitsongs[i]) <= float(vals[j]):
                                        j += 1
                                        if j >= len(vals):
                                            looping = False
                                            top_ten.append((splitsongs[i - 1], self.loglen(splitsongs[i - 1], splitsongs[i])))
                                    else:
                                        looping = False
                                        top_ten.insert(j, (splitsongs[i - 1], self.loglen(splitsongs[i - 1], splitsongs[i])))
                            elif len(top_ten) >= NUM:
                                vals = [x[1] for x in top_ten]
                                j = 0
                                looping = True
                                while looping:
                                    if self.loglen(splitsongs[i - 1], splitsongs[i]) <= float(vals[j]):
                                        j += 1
                                        if j >= len(vals):
                                            looping = False
                                    else:
                                        looping = False
                                if j < len(vals):
                                    top_ten.insert(j, (splitsongs[i - 1], self.loglen(splitsongs[i - 1], splitsongs[i])))
                                    top_ten.pop(-1)
                        elif METRIC == "num":
                            if top_ten == []:
                                top_ten.append((splitsongs[i - 1], self.numlistens(splitsongs[i-1], splitsongs[i])))
                            elif len(top_ten) < NUM:
                                vals = [x[1] for x in top_ten]
                                j = 0
                                looping = True
                                while looping:
                                    if self.numlistens(splitsongs[i-1], splitsongs[i]) <= float(vals[j]):
                                        j += 1
                                        if j >= len(vals):
                                            looping = False
                                            top_ten.append((splitsongs[i - 1], self.numlistens(splitsongs[i-1], splitsongs[i])))
                                    else:
                                        looping = False
                                        top_ten.insert(j, (splitsongs[i - 1], self.numlistens(splitsongs[i-1], splitsongs[i])))
                            elif len(top_ten) >= NUM:
                                vals = [x[1] for x in top_ten]
                                j = 0
                                looping = True
                                while looping:
                                    if self.numlistens(splitsongs[i-1], splitsongs[i]) <= float(vals[j]):
                                        j += 1
                                        if j >= len(vals):
                                            looping = False
                                    else:
                                        looping = False
                                if j < len(vals):
                                    top_ten.insert(j, (splitsongs[i - 1], self.numlistens(splitsongs[i-1], splitsongs[i])))
                                    top_ten.pop(-1)
                else:
                    pass

            return top_ten

    def metric_print(self, top_songs, console_size, is_full=False, in_hms=True):
        if self.user != "guest":
            for j in range(0, len(top_songs)):
                if in_hms:
                    min_sec_print = datetime.timedelta(seconds=np.round(float(top_songs[j][1]),0))
                    end_buff = console_size-len(str(j+1)+"x" + 2*buffer + str(min_sec_print))
                else:
                    min_sec_print = str(np.round(top_songs[j][1],3))
                    end_buff = console_size - len(str(j + 1) + "x" + 2 * buffer + str(min_sec_print))
                if len(top_songs[j][0].replace(".mp3","").replace(".opus","")) <= end_buff:
                    line_one = top_songs[j][0].replace(".mp3","").replace(".opus","")
                    line_two = ""
                    line_three = ""
                else:
                    splitline = top_songs[j][0].replace(".mp3","").replace(".opus","").split(" ")
                    line_one = ""
                    line_two = ""
                    line_three = ""
                    k = 0
                    oops = True
                    while oops:
                        if k < len(splitline):
                            if len(line_one)+len(splitline[k]) + 1 <= end_buff:
                                line_one += splitline[k] + " "
                                k += 1
                            else:
                                oops = False
                                line_one = line_one[0:-1]
                        else:
                            oops = False
                    oops = True
                    while oops:
                        if k < len(splitline):
                            if len(line_two)+len(splitline[k]) + 1 <= end_buff:
                                line_two += splitline[k] + " "
                                k += 1
                            else:
                                oops = False
                        else:
                            oops = False
                    oops = True
                    while oops:
                        if k < len(splitline):
                            if len(line_three)+len(splitline[k]) + 1 <= end_buff:
                                line_three += splitline[k] + " "
                                k += 1
                            else:
                                oops = False
                        else:
                            oops = False
                if not is_full:
                    print(str(j+1)+"x" + " "*(2-len(str(j+1))) + buffer + line_one + buffer + " "*(console_size-len(str(min_sec_print))-2*len(buffer)-len(line_one)-3) + str(min_sec_print))
                else:
                    print(str(j+1)+":" + " "*(2-len(str(j+1))) + buffer + line_one + buffer + " "*(console_size-len(str(min_sec_print))-2*len(buffer)-len(line_one)-3) + str(min_sec_print))
                if line_two != "":
                    print(buffer + " "*(j+1)+"  " + line_two)
                if line_three != "":
                    print(buffer + " " * (j + 1) + "  " + line_three)

    def artist_maths(self, NUM, is_full=False):
        songslist = []
        artistslist = {}
        if is_full:
            with open("Analytics.txt") as f:
                for x in f:
                    songslist.append(x)
        else:
            with open("ShortTermAnalytics.txt") as f:
                for x in f:
                    songslist.append(x)
        for i in range(0, len(songslist)):
            if self.user in songslist[i][0:20]:
                splitsongs = songslist[i].split("±")
                for j in range(2, len(splitsongs), 2):
                    if splitsongs[j-1].split("-")[0] not in artistslist:
                        artistslist[splitsongs[j-1].split("-")[0]] = float(splitsongs[j])
                    else:
                        artistslist[splitsongs[j-1].split("-")[0]] += float(splitsongs[j])
        top_artists = []
        while len(top_artists) < NUM and len(artistslist) > 0:
            max_time = max(artistslist.values())
            top_artists.append((list(artistslist.keys())[list(artistslist.values()).index(max_time)], max_time))
            artistslist.pop(list(artistslist.keys())[list(artistslist.values()).index(max_time)])
        return top_artists

    def total_minutes_listened(self, is_full=False):
        songslist = []
        time = 0
        if is_full:
            with open("Analytics.txt") as f:
                for x in f:
                    songslist.append(x)
        else:
            with open("ShortTermAnalytics.txt") as f:
                for x in f:
                    songslist.append(x)
        if self.user != "guest":
            for i in range(0, len(songslist)):
                if self.user in songslist[i][0:20]:
                    splitsongs = songslist[i].split("±")
                    for i in range(2, len(splitsongs), 2):
                        time += float(splitsongs[i])
        print(f"Total listening time: {datetime.timedelta(seconds=time)}")

    def genre_maths(self, NUM, is_full=False):
        genreslist = {}
        songslist = []
        with open("Songs.json", "r") as f:
            songsjson = json.load(f)
        if is_full:
            with open("Analytics.txt") as f:
                for x in f:
                    songslist.append(x)
        else:
            with open("ShortTermAnalytics.txt") as f:
                for x in f:
                    songslist.append(x)
        for i in range(0,len(songslist)):
            if self.user in songslist[i][0:20]:
                splitsongs = songslist[i].split("±")
                for j in range(2, len(splitsongs), 2):
                    try:
                        if songsjson[splitsongs[j-1]]["genre"] is not None and songsjson[splitsongs[j-1]]["genre"] != []:
                            #print(songsjson[splitsongs[j-1]]["genre"])
                            if songsjson[splitsongs[j-1]]["genre"] not in genreslist:
                                genreslist[songsjson[splitsongs[j-1]]["genre"]] = float(splitsongs[j])
                            else:
                                genreslist[songsjson[splitsongs[j - 1]]["genre"]] += float(splitsongs[j])
                    except KeyError:
                        pass
        top_genres = []
        while len(top_genres) < NUM and len(genreslist) > 0:
            max_time = max(genreslist.values())
            top_genres.append((list(genreslist.keys())[list(genreslist.values()).index(max_time)], max_time))
            genreslist.pop(list(genreslist.keys())[list(genreslist.values()).index(max_time)])
        return top_genres

    def shittyInternalVersionControl(self):
        self.pront("1.0: plays songs. basic play pause rewind functionality", "")
        self.pront("1.1: playlist, queue, and display songs functionality.", "")
        self.pront("1.2: search, help, and empty queue functionality added.", "")
        self.pront("1.2.1: bug fixes. loop functionality added. fixed songs skipping in autoplay. "
                   "Updated help function.", "")
        self.pront("1.2.2: Added version control. Fixed playlist queuing. Added desktop app.", "")
        self.pront("1.2.3: Added bugs file to track errors. Fixed crashes when -shuffle was called. "
                   "-queue -f now does not remove the first song in the queue. Updated help function.", "")
        self.pront("1.3.0: Added monthly listening stats feature.", "")
        self.pront("1.3.1: Bug fixes. Added song library and byte size to opening outputs. "
                   "Song library now updates automatically."
                   "-search -not-latin now searches for any non-latin characters, not exclusively them"
                   "added ability to clear monthly listening stats. Created basic yearly analytics structure", "")
        self.pront("1.4.0: Whole bunch of stuff that should have been in smaller updates. Added lyrics"
                   "functionality, genres functionality, redesigned the architecture to use .json files instead"
                   "of .txt ones. Finally set up github repo. Started to make this program easily installable."
                   "(obv. not finished yet) Added settings.txt functionality, users and such are stored in that"
                   "file and is editable upon install. (not after - that needs to be fixed). Added internal tools"
                   "for checking completness of library and randomness of shuffle ability. fixed parser to be more"
                   "like a bash style script. Added backup .json files to help shield against crashes and"
                   "other such errors without destroying ones library.", "")
        self.pront("1.4.1: Fixed search -as. Updated queue, songs, play, playlists to take new song identifiers (filepaths)"
                   "instead of the old ones (self.songnames index). Made settings changable via the program. "
                   "Updated README.md. Fixed self.terminal_length (size setting) being set to 80 in various"
                   "function definitions. Automated install - now all that needs to happen is to run the main.py file."
                   "updated help function.", "")
        self.pront("1.4.2: Fixed install errors (not creating songs.json file, settings.txt not being prompted)"
                   "depreciated Songs.txt", "")

    def updateBugs(self, str):
        with open("bugs.txt","a") as f:
            f.write(str+"\n")

    def updateToAdd(self, str):
        with open("To_Add.txt","a") as f:
            f.write(str+"\n")

    def updateSettings(self):
        settingslist = []
        with open("Settings.txt", "r") as f:
            for x in f:
                settingslist.append(x)
        print(settingslist)
        print("Type 'done' to exit settings menu. Type 'quit' to exit program. Type 'users NEW, LIST, OF, USERS',"
              "'directory /path/to/new/directory', or 'size NEW_TERMINAL_LENGTH' to update any of the current settings")
        with open("Input.txt", "w") as f:
            f.write("")
        main = True
        while main:
            usr_list = ""
            dir_path = ""
            size = ""
            #getting user input
            with open("Input.txt", "r") as f:
                for x in f:
                    if x != "":
                        if x == "done":
                            main = False
                        elif "users" in x[0:5]:
                            x = x[5:]
                            usr_list = x.split(",")
                        elif "directory" in x[0:9]:
                            dir_path = x[9:]
                        elif "size" in x[0:4]:
                            size = x[4:]
            #actually updating the settings file
            if usr_list != "" or dir_path != "" or size != "":
                if usr_list != "":
                    settingslist[0] = "users: " + usr_list + "\n"
                elif dir_path != "":
                    settingslist[1] = "directory: " + dir_path + "\n"
                elif size != "":
                    settingslist[2] = "size: " + size + "\n"
                write_flush = ""
                for i in range(0,len(settingslist)):
                    write_flush += settingslist[i]
                with open("Settings.txt", "w") as f:
                    f.write(write_flush)

    def Lyrics(self, is_spoof_agents=False, none_lyrics=False):
        with open("Songs.json", "r") as f:
            songsjson = json.load(f)
        successes = 0
        cap = 0
        print("read in songs.json")
        for j in songsjson.keys():
            if none_lyrics:
                bool = True
            else:
                bool = False
            if songsjson[j]["lyrics"] == {} or bool*(songsjson[j]["lyrics"] == "None. :(("):
                failedmxm = False
                failedgns = False
                failedbndcmp = False
                song, artist = songsjson[j]["song"], songsjson[j]["artist"]
                old_song, old_artist = songsjson[j]["song"], songsjson[j]["artist"]
                if "," in artist:
                    artist = artist.split(",")[0]
                for i in ["01 ", "02 ", "03 ", "04 ", "05 ", "06 ", "07 ", "08 ", "09 ", "10 "]:
                    if i in song:
                        song = song.replace(i, "")
                if song[0] in [chr(i) for i in range(97, 97 + 26 + 1)]+[chr(i) for i in range(65, 65 + 26)]:
                    song = str(
                        song.replace(" ", "-").replace("!", "").replace(",", "").replace("(", "")
                        .replace(")","").replace("[", "").replace("]", "").replace(".", "").replace("--", "-")
                        .replace("'", "").replace("&","and").replace("/", "-").replace("--", "-").replace("#", ""))
                else:
                    song = str(
                        song[1:].replace(" ", "-").replace("!", "").replace(",", "").replace("(", "")
                        .replace(")", "").replace("[", "").replace("]", "").replace(".", "").replace("--", "-")
                        .replace("'", "").replace("&", "and").replace("/", "").replace("--", "-").replace("#", ""))
                if artist[-1] in [chr(i) for i in range(97, 97 + 26 + 1)]+[chr(i) for i in range(65, 65 + 26)]:
                    artist = str(artist.replace(" ", "-").replace(".", "").replace("'", ""))
                else:
                    artist = str(artist[0:-1].replace(" ", "-").replace(".", "").replace("'", ""))
                link = "https://www.musixmatch.com/lyrics/"+artist+"/"+song
                agents = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0',
                          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.3",
                          "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.",
                          "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/26.0 Chrome/122.0.0.0 Safari/537.3",
                          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.1",
                          "Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1 Ddg/17.",
                          "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.3",
                          "Mozilla/5.0 (Linux; Android 11; moto e20 Build/RONS31.267-94-14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.70 Mobile Safari/537.3",
                          "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.3"]
                if is_spoof_agents:
                    agent = agents[random.randint(0, len(agents) - 1)]
                else:
                    agent = agents[0]
                r = requests.get(link, headers={'User-Agent': agent})
                #print(link)
                print(r, song, artist, "mxm")
                #print(link)
                if str(r) == "<Response [200]>":
                    #print("mxm")
                    successes += 1
                    cap += 1
                    soup = BeautifulSoup(r.content, 'html.parser')
                    old_lyrics = soup.get_text()
                    if "Unfortunately we're not authorized" not in soup.get_text():
                        lyrics = soup.get_text().split("Writer(s):")[0]
                        if old_artist in old_lyrics or old_song in old_lyrics:
                            if "Unfortunately we're not authorized" not in lyrics:
                                try:
                                    lyrics = lyrics.split(str(old_artist[0:-1])+"verse")[1]
                                except IndexError:
                                    try:
                                        lyrics = lyrics.split(str(old_artist[0:-1]) + "chorus")[1]
                                    except IndexError:
                                        try:
                                            lyrics = lyrics.split(str("Lyrics of"+old_song+ "by "+old_artist[0:-1]))[1]
                                            #print(lyrics)
                                        except IndexError:
                                            try:
                                                lyrics = lyrics.split(old_artist[:-1])[3]
                                            except IndexError:
                                                try:
                                                    lyrics = lyrics.split("Translations")[2]
                                                except IndexError:
                                                    try:
                                                        lyrics = lyrics.split("Translations")[1]
                                                        #this is almost always a fail case, but very occasionally
                                                        #it works
                                                    except IndexError:
                                                        lyrics = "None. :(("
                                                        successes -= 1
                                                        failedmxm = True
                                #print("updated:", lyrics)
                                if "no lyrics here" in lyrics or "Share/These Lyrics are" in lyrics:
                                    lyrics = "None. :(("
                                for k in range(0,len(lyrics)-1):
                                    if lyrics[k] in [chr(i) for i in range(97, 97 + 26 + 1)] and lyrics[k+1] in [chr(i) for i in range(65, 65 + 26)]:
                                        #print("pwong", lyrics[k], lyrics[k+1])
                                        lyrics = lyrics.replace(lyrics[k]+lyrics[k+1], lyrics[k]+"/"+lyrics[k+1])
                                songsjson[j]["lyrics"] = lyrics
                            else:
                                successes -= 1
                                failedmxm = True
                        else:
                            successes -= 1
                            failedmxm = True
                    else:
                        successes -= 1
                        failedmxm=True
                else:
                    failedmxm=True
                if failedmxm:
                    artist = artist[0].upper() + artist.lower()[1:]
                    link = "https://genius.com/" + artist + "-" + song.lower() + "-lyrics"
                    if is_spoof_agents:
                        agent = agents[random.randint(0,len(agents)-1)]
                    else:
                        agent = agents[0]
                    r = requests.get(link, headers={'User-Agent': agent, "referer":"https://genius.com/"})
                    print(r, song, artist, "gns")
                    #print(link)
                    #print("!", r)
                    if str(r) == "<Response [200]>":
                        #print("gns")
                        successes += 1
                        cap+= 1
                        soup = BeautifulSoup(r.content, 'html.parser')

                        try:
                            lyrics = soup.get_text().split(song[1:] + " Lyrics")[2]
                            #print("gns separator ", lyrics)
                            lyrics = lyrics.split("EmbedCancelHow")[0]
                            #print("gns separated ", lyrics)
                        except IndexError:
                            try:
                                lyrics = soup.get_text().split(song[1:] + " Lyrics")[1]
                                lyrics = lyrics.split("EmbedCancelHow")[0]
                                #print("sda")
                            except IndexError:
                                try:
                                    lyrics = soup.get_text().split(song[-2:] + " Lyrics")[2]
                                    lyrics = lyrics.split("EmbedCancelHow")[0]
                                except IndexError:
                                    lyrics = "None. :(("
                                    #print("oopsie")
                                    failedgns = True
                        for k in range(0, len(lyrics) - 1):
                            if lyrics[k] in [chr(i) for i in range(97, 97 + 26 + 1)] and lyrics[k + 1] in [chr(i) for i
                                                                                            in range(65,65 + 26)]:
                                # print("pwong", lyrics[k], lyrics[k+1])
                                lyrics = lyrics.replace(lyrics[k] + lyrics[k + 1], lyrics[k] + "/" + lyrics[k + 1])
                        #print(lyrics)
                        songsjson[j]["lyrics"] = lyrics
                    else:
                        failedgns=True
                        successes -= 1
                    if failedgns:
                        link = "https://"+ artist.lower().replace(" ", "").replace("-","")+".bandcamp.com/track/" + song.lower()
                        #print(link)
                        try:
                            r = requests.get(link, headers={
                            'User-Agent': agent})
                        except requests.exceptions.SSLError:
                            r = -1
                        print(r, song, artist, "bndcmp")
                        # print("!", r)
                        if str(r) == "<Response [200]>":
                            soup = BeautifulSoup(r.content, 'html.parser')
                            lyrics = soup.get_text()
                            #print(lyrics)
                            try:
                                lyrics = lyrics.split("Send as Gift")[1]
                                lyrics = lyrics.split("\nlyrics")[1]
                                lyrics = lyrics.split("credits")[0]
                                #print("1,", lyrics)
                            except IndexError:
                                try:
                                    lyrics = lyrics.split("///lyrics")[1]
                                    print("2, ", lyrics)
                                    lyrics = lyrics.split("credits")[0]
                                except IndexError:
                                    print("failed")
                                    lyrics = ""
                                    failedbndcmp = True
                            lyrics = lyrics.replace("\n","/")
                            #print("bndcmp", lyrics)


                            songsjson[j]["lyrics"] = lyrics
                        else:
                            failedbndcmp = True
                        if failedbndcmp:
                            link = "https://www.azlyrics.com/lyrics/" + artist.lower().replace(" ", "").replace("-","")+"/"+song.lower().replace(" ", "").replace("-", "") + ".html"
                            r = requests.get(link, headers={"User-Agent":agent})
                            print(r, song, artist, "az")
                            if str(r) == "<Response [200]>":
                                soup = BeautifulSoup(r.content, 'html.parser')
                                lyrics = soup.get_text()
                                #print(lyrics)
                                try:
                                    lyrics = lyrics.split("\""+old_song+"\"")[2]
                                    lyrics = lyrics.split("Submit Corrections")[0]
                                except IndexError:
                                    try:
                                        lyrics = lyrics.split("lyrics")[1]
                                        lyrics = lyrics.split("Submit Corrections")[0]
                                        lyrics = lyrics.split("Lyrics")[1]
                                    except IndexError:
                                        try:
                                            lyrics = lyrics.split("Submit Corrections")[0]
                                            #lyrics = lyrics.split("Lyrics")[1]
                                            print("Lyrics" in lyrics)
                                        except IndexError:
                                            pass
                                while "\n\n" in lyrics:
                                    lyrics = lyrics.replace("\n\n", "\n")
                                lyrics = lyrics.replace("\n", "/")
                                if "Our systems have detected unusual activity from your IP address" not in lyrics:
                                    #print([lyrics])
                                    songsjson[j]["lyrics"] = lyrics




            if cap >= 10:
                break

        print(successes)
        with open("Songs.json", "w") as f:
            json_obj = json.dumps(songsjson, indent=4)
            f.write(json_obj)

    def HowCompleteLibrary(self, lyrics=True):
        if lyrics:
            with open("Songs.json", "r") as f:
                songsjson = json.load(f)
            successes_lyrics = 0
            successes_genres = 0
            nones_lyrics = 0
            nones_genres = 0
            all = 0
            for j in songsjson.keys():
                all += 1
                if songsjson[j]["lyrics"] != {}:
                    successes_lyrics += 1
                if songsjson[j]["lyrics"] == "None. :((":
                    nones_lyrics += 1
                if songsjson[j]["genre"] != None:
                    successes_genres += 1
                else:
                    nones_genres += 1

        print(f"Lyrics: {np.round(successes_lyrics / all*100, 3)}% ({successes_lyrics}), None lyrics: {np.round(nones_lyrics / successes_lyrics*100, 3)}% ({nones_lyrics})")
        print(
            f"Genres: {np.round(successes_genres / all * 100, 3)}% ({successes_genres}), None Genres: {np.round(nones_genres / all * 100, 3)}% ({nones_genres})")
    def TxtToLyrics(self, track_name, file):
        with open("Songs.json", "r") as f:
            songsjson = json.load(f)
        with open(file, "r") as f:
            songlyrics = f.read()
        text = songlyrics.replace("\n", "/")
        songsjson[track_name]["lyrics"] = text
        with open("Songs.json", "w") as f:
            json_obj = json.dumps(songsjson, indent=4)
            f.write(json_obj)

    def find_genres(self):
        with open("Songs.json", "r") as f:
            songsjson = json.load(f)
        for track_filepath in songsjson:
            if songsjson[track_filepath]["genre"] is None or songsjson[track_filepath]["genre"] == []:
                try:
                    genre = TinyTag.get(self.Directory + track_filepath).genre
                    if genre != "null" and genre != "None":
                        songsjson[track_filepath]["genre"] = genre
                    else:
                        pass
                        '''link = ""
                        r = requests.get(link, headers={})
                        if str(r) == "<Response [200]>":
                            soup = BeautifulSoup(r.content, 'html.parser')'''
                except FileNotFoundError:
                    pass
            else:
                pass
        with open("Songs.json", "w") as f:
            json_obj = json.dumps(songsjson, indent=4)
            f.write(json_obj)
        print("done!")

    def printLyrics(self, song):
        #print(song)
        with open("Songs.json", "r") as f:
            songsjson = json.load(f)
        if songsjson[song[0]]["lyrics"] != {}:
            #print(songsjson[song[0]]["lyrics"])
            lyrics = songsjson[song[0]]["lyrics"].split("/")
            for x in lyrics:
                self.pront(x, "")




if __name__ == "__main__":
    if imports_successful:
        buffer = " "*10
        printLogo()
        print()
        with open("Output.txt", "w") as f:
            f.write("done")
        print("⇓⇓ Your input goes here!")
        print(buffer+"      ⇓⇓ and what I say goes here! ⇓⇓")
        print(buffer + "Hiya! Who are you?")
        user = ""
        while user == "":
            with open("Input.txt", "r") as f:
                for x in f:
                    if x != "":
                        user = x

        JukeBox(user).run()
    else:
        print_flush = ""
        for x in missing_packages:
            print_flush += x + ", "
        print(f"Missing Required Packages. Please install {print_flush}")
        with open("Output.txt", "w") as f:
            f.write("done. failed.")

