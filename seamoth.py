import speech_recognition as sr
import keys as k
import time

def sleepcmd(coml):
    if len(coml) >= 2:
        try:
            if coml[1] == "one":
                duration = 1
            elif coml[1] == "two" or coml[1] == "to":
                duration = 2
            elif coml[1] == "three":
                duration = 3
            elif coml[1] == "four" or coml[1] == "for":
                duration = 4
            elif coml[1] == "five":
                duration = 5
            else:
                duration = int(coml[1])
            time.sleep(duration)
        except:
            pass
    else:
        time.sleep(1)

keys = k.Keys()

recog = sr.Recognizer()

more = True
while more:
    try:
        with sr.Microphone() as source:
            print("seamoth ready:")
            spoken = recog.listen(source,phrase_time_limit=5)
            #print("spoken = ",spoken)
            print("parsing sentence...")
            command = recog.recognize_google(spoken)
            print("I heard: ",command)

            coml = list(map(lambda x:x.lower(),command.split()))
            if coml[0] == "end" and coml[1] == "program":
                more = False
            else:
                if coml[0] == "left":
                    keys.directKey("a")
                    sleepcmd(coml)
                    keys.directKey("a", keys.key_release)
                elif coml[0] == "right" or coml[0] == "write":
                    keys.directKey("d")
                    sleepcmd(coml)
                    keys.directKey("d", keys.key_release)
                elif coml[0] == "forward":
                    keys.directKey("w")
                    sleepcmd(coml)
                    keys.directKey("w", keys.key_release)
                elif coml[0] == "back":
                    keys.directKey("s")
                    sleepcmd(coml)
                    keys.directKey("s", keys.key_release)
                elif coml[0] == "dive":
                    keys.directKey("c")
                    sleepcmd(coml)
                    keys.directKey("c", keys.key_release)
                elif coml[0] == "rise":
                    keys.directKey("space")
                    sleepcmd(coml)
                    keys.directKey("space", keys.key_release)
                elif coml[0] == "turn" or coml[0] == "Turn":
                    keys.directMouse(-5,0)
                    print("mouse command executed")
                #elif coml[0] == "stop":
                    #keys.directKey("space")
                    #keys.directKey("space", keys.key_release)
                else:
                    print("command not recognized")
    except:
        print("sorry, I didn't get that")