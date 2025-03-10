# im importing pyttsx3 libray to convert text into speech
import pyttsx3
if __name__ == "__main__":# this line is added so that it can execute only in this program as a module
    engine = pyttsx3.init()#this is initializing the text to speach engine

    engine.setProperty("rate", 150)  #this will make the voice rate 140 which is normal human rate 120-150
    voices = engine.getProperty("voices")#voice can be of male as well as of female for male id is 0 and for female id is 1
    engine.setProperty("voice", voices[1].id)

    print("Welcome to Robot Speaker!\nCreated by Rumaz Qureshi")
    engine.say("Welcome to Robot Speaker!\nCreated by Rumaz Qureshi")#welcome the user by reading this text
    engine.runAndWait()
    # while loop so that it will gonna run continuously till we write exit or quit as input
    # also if user enter who created you it will give the answer that im created by Rumaz and again back to the loop
    while True:
        x = input("Enter what you want me to speak: ")
        
        if x.lower() in ["exit", "quit"]:
            print("Exiting... Goodbye!")
            engine.say("Goodbye!")
            engine.runAndWait()
            break
        
        elif x.lower() == "who created you":
            response = "I am created by Rumaz Qureshi."
            print(response)
            engine.say(response)
            engine.runAndWait()
        
        else:
            engine.say(x)
            engine.runAndWait()