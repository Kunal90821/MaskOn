
def without_mask_data():
    import cv2
    import numpy as np
    haar_data = cv2.CascadeClassifier('E:/project/face_mask_detection/face_mask/data.xml')

    capture = cv2.VideoCapture(0)
    data = []
    while True:
        flag, img = capture.read()
        if flag:
            faces = haar_data.detectMultiScale(img)
            for x,y,w,h in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 4)
                face = img[y:y+h, x:x+w, :]
                face = cv2.resize(face,(50,50))
                print(len(data))
                if len(data) < 200:
                    data.append(face)
            cv2.imshow('Recording Data Wihtout Mask', img)

            if cv2.waitKey(2) == 27 or len(data) >= 200:
                break
    capture.release()
    cv2.destroyAllWindows() 
    np.save('without_mask.npy',data)

def with_mask_data():
    import cv2
    import numpy as np
    haar_data = cv2.CascadeClassifier('E:/project/face_mask_detection/face_mask/data.xml')

    capture = cv2.VideoCapture(0)
    mask_data = []
    while True:
        flag, img = capture.read()
        if flag:
            faces = haar_data.detectMultiScale(img)
            for x,y,w,h in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 4)
                face = img[y:y+h, x:x+w, :]
                face = cv2.resize(face,(50,50))
                print(len(mask_data))
                if len(mask_data) < 200:
                    mask_data.append(face)
            cv2.imshow('Recording Data With Mask', img)
            
            if cv2.waitKey(2) == 27 or len(mask_data) >= 200:
                break

    capture.release()
    cv2.destroyAllWindows() 

    np.save('with_mask.npy',mask_data)

   