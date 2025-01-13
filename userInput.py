import time

if __name__ == "__main__":
    f = open("Output.txt", "w")
    f.write("")
    f.close()
    f = open("Input.txt", "w")
    f.write("")
    f.close()
    main = True
    clean = False
    with open("Output.txt", "w") as f:
        f.write("")
    while main:
        with open("Output.txt") as f:
            for x in f:
                if x == "done":
                    main = False
                    kill = False
                if x == "done. failed.":
                    main = False
                    kill = True

    if not kill:
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
    else:
        time.sleep(2)

