import cv2

def play_video(source):
    if source == 'camera':
        cap = cv2.VideoCapture(0) 
    elif source == 'phone':
        cap = cv2.VideoCapture('http://192.168.0.107:8080/video') 
    else:
        cap = cv2.VideoCapture(source) 

    if not cap.isOpened():
        print("Помилка. Не вдалося відкрити відео або камеру.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Роботу завершено.")
            break

        cv2.imshow('Video', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break 

    cap.release()
    cv2.destroyAllWindows()


play_video('phone')

