# im importing pyttsx3 libray to convert text into speech
import pyttsx3

if __name__ == "__main__":# this line is added so that it can execute only in this program as a module

    engine = pyttsx3.init() #this is initializing the text to speach engine

    print("Welcome to Robot Speaker!\nCreated by Rumaz Qureshi")
    # while loop so that it will gonna run continuously till we write exit or quit as input
    # also if user enter who created you it will give the answer that im created by Rumaz and again back to the loop
    while True:
        x = input("Enter what you want me to speak: ")
        if x=="who created you":
            print(engine.say("I am created by Rumaz"))
            engine.runAndWait()
        elif x.lower() in ["exit", "quit"]:
            break
        else:
            engine.say(x)
            engine.runAndWait()