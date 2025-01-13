import time

if __name__ == "__main__":
    f = open("Output.txt", "w")
    f.write("")
    f.close()
    f = open("Input.txt", "w")
    f.write("")
    f.close()
    '''while main:
        with open("Output.txt") as f:
            for x in f:
                if x == "go":
                    main = False
    with open("Jukebox.txt") as g:
        for x in g:
            if bool:
                print(x)
                bool = False
            else:
                bool = True'''
    main = True
    clean = False
    with open("Output.txt", "w") as f:
        f.write("")
    while main:
        with open("Output.txt") as f:
            for x in f:
                if x == "done":
                    main = False

    time.sleep(0.25)
    main = True
    f = open("Output.txt", "w")
    f.write("")
    f.close()
    while main:
        time.sleep(.1)
        usr_input = input("")
        if usr_input == "dev.killall":
            main = False
            usr_input = "quit"
        f = open("Input.txt", "w")
        f.write(usr_input)
        f.close()
        time.sleep(.1)
        f = open("Output.txt", "r")
        for x in f:
            if "quit" in x:
                main = False
            '''if "clean" in x:
                clean = True
        if clean:
            clean = False'''
        f.close()

