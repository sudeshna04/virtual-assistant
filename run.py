import multiprocessing  #Python’s built-in multiprocessing module to allow running multiple processes in parallel.

def startJarvis():
    print("Process 1 start")
    from main import start
    start()

def listenHotword():
    print("Process 2 start")
    from engine.features import hotword
    hotword()

if __name__ == '__main__': #Main Process (only runs when script is run directly):
    multiprocessing.freeze_support()  # Required for Windows
    p1 = multiprocessing.Process(target=startJarvis)
    p2 = multiprocessing.Process(target=listenHotword)

    p1.start()
    p2.start()

    # .join() tells the main program to wait until p1 finishes.
    # This means the main script will pause here and not continue until the startJarvis() process exits.
    # Meanwhile, p2 continues running in the background.
    p1.join()
    if p2.is_alive():
        p2.terminate() 
        p2.join()   #After terminating, .join() waits for the p2 process to properly shut down and clean up.

    print("System stopped.")
# It runs two separate processes using the multiprocessing module:
# One to start the main Jarvis function.
# Another to continuously listen for a hotword (like "Hey Jarvis").