import cv2
import pyttsx3
import time

# Initialize the TTS engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait() #This starts the speech engine and processes the voice queue, speaking out the text.It blocks the program until all speech is done.

def capture_smile_photo():
    # Load Haar cascades
# Haar Cascades are pre-trained models to detect faces and smiles.
# face_cascade: detects faces in the frame.
# smile_cascade: detects smiles within detected faces.
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

    cap = cv2.VideoCapture(1) #cap is the camera object used to read frames.
    captured = False

    speak("Looking for your smile. Please smile at the camera.")

    while not captured:
        ret, frame = cap.read() #frame is captured from the webcam
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #gray is the grayscale version used for detection (Haar cascades work on grayscale).
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            face_roi = gray[y:y+h, x:x+w]
            smiles = smile_cascade.detectMultiScale(face_roi, scaleFactor=1.8, minNeighbors=20)

            if len(smiles) > 0:
                speak("Say cheese!")
                time.sleep(1)  # slight delay before capturing
                img_name = "captured_photo.png"
                cv2.imwrite(img_name, frame) #A function in OpenCV that writes (saves) an image to a file.
                captured = True
                speak("Photo captured successfully.")
                break

        cv2.imshow("Smile Detector - Press 'q' to quit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release() #It releases the webcam resource when you're done using it.
    cv2.destroyAllWindows() #Frees up the webcam and closes all OpenCV windows.

    if captured: 
        img = cv2.imread("captured_photo.png")
        cv2.imshow("Your Captured Photo", img) #displays photo and window freeze
        cv2.waitKey(0) #window freeze until key is pressed
        cv2.destroyAllWindows()

# Run the function
capture_smile_photo()
