import cv2
import tkinter as tk

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

def detect_faces_from_image(image_path):
    image=cv2.imread(image_path)
    if image is None:
        result_label.config(text="please enter the correct image location")
        return

    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("face detection app",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_faces_from_video():

    cap=cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    while True:
        ret,frame=cap.read()

        if not ret:
            break

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imshow("face detection app",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def handle_choice():
    value=entry_choice.get()
    if value=="1":
        path = entry_image_path.get()
        if path=="":
            result_label.config(text="please enter the image loaction")
        else:
            detect_faces_from_image(path)
            entry_choice.delete(0,tk.END)
            entry_image_path.delete(0,tk.END)
            result_label.config(text="")
    elif value=="2":
        detect_faces_from_video()
        entry_choice.delete(0,tk.END)
        result_label.config(text="")
    else:
        result_label.config(text="please choose 1 or 2")




root=tk.Tk()
root.title("face detection app")
root.geometry("500x500")

title=tk.Label(root,text="face detection app")
title.pack(pady=10)

choice=tk.Label(root,text="choose option\n-------------")
choice.pack(pady=5)

choice1=tk.Label(root,text="1-detect face in picture ( enter the file location)")
choice1.pack(pady=5)

choice2=tk.Label(root,text="2-detect face in video")
choice2.pack(pady=5)

entry_choice=tk.Entry(root,width=4)
entry_choice.pack(pady=10)

entry_image_path=tk.Entry(root,width=40)
entry_image_path.pack(pady=10)

button=tk.Button(root,text="submit",command=handle_choice)
button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()


