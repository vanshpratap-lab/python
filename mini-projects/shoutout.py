# import pyttsx3

# engine = pyttsx3.init()
# names = ["rahul","ritika","preeti"]
# for name in names:
#     engine.say(f" shoutout to {name}")
# engine.runAndWait()
# del engine

# import pyttsx3
# import os

# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
#     del engine

# speak("Welcome back. Please select an option.")

# while True:
#     print("\n--- VOICE MENU ---")
#     print("1. Say Hello")
#     print("2. Tell a Joke")
#     print("3. Exit")
    
    # choice = input("Enter your choice (1-3): ")
    
    # if choice == "1":
    #     speak("Hello User! I hope you are having an amazing day.")
    # elif choice == "2":
    #     speak("Why do programmers wear glasses?")
    #     speak("Because they can't C sharp!")
    # elif choice == "3":
    #     speak("Goodbye! Shutting down system.")
    #     break
    # else:
    #     speak("Invalid option, please try again.")

# --------oops aprooach for above code-----------

import pyttsx3

class speaker:
    def __init__(self):
        self.engine = pyttsx3.init()

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


class voicemenu:
    def __init__(self):
        self.speaker = speaker()    

    def show_menu(self):
        print("\n------VOICE MENU-----")
        print("1. say hello")
        print("2. tell a joke")
        print("3. exit")

    def run(self):
        self.speaker.say("Welcome back. Please select an option.")
        while True:                          
            self.show_menu()
            choice = input("Enter your choice (1-3): ")  

            if choice == "1":
                self.speaker.say("hello user! i hope you are having a nice day")
            elif choice == "2":
                self.speaker.say("why do programmers wear glasses")
                self.speaker.say("because they can't c sharp")
            elif choice == "3":
                self.speaker.say("goodbye! shutting down system")
                break
            else:
                self.speaker.say("invalid option please try again")


menu = voicemenu()
menu.run()
