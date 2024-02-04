import os
import cv2
from datetime import datetime
import random

cap=cv2.VideoCapture(0)

fps = cap.get(cv2.CAP_PROP_FPS)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

path=os.path.join(os.getcwd(),"vedio_save")

i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow("video",frame)
    font = cv2.FONT_HERSHEY_PLAIN 
    cv2.putText(frame, str(datetime.now()), (20, 40), 
                font, 2, (255, 255, 255), 2, cv2.LINE_AA) 
    filename=datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f")
    imgpath=str(os.path.join(path,str(random.randint(1,10000))))+".jpg"
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
    print(imgpath)
    cv2.imwrite(imgpath,frame)
    i+=1
'''
while True:
    ret , frame=cap.read()
    cv2.imshow("video",frame)
    filename=str(datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f")) +".jpg"
    imgpath=os.path.join(path,filename)
    print(imgpath)
    cv2.imwrite(imgpath,frame)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
'''
    


#writer=cv2.VideoWriter("recording.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
#recording=False

'''
while True:
    ret , frame=cap.read()
    if ret:
        cv2.imshow("video",frame)
        if recording:
            writer.write(frame)
            print(fps,w,h)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
    elif key==ord('r'):
        recording=not recording
        print(f'Recoeding: {recording}')
'''
cap.release()
#writer.release()
cv2.destroyAllWindows()
