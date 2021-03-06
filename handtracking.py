# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def handtrackingp():
    import cv2
    import mediapipe as mp
    import time


    cap = cv2.VideoCapture(0)
    mphands = mp.solutions.hands
    hands = mphands.Hands()
    mpdraw = mp.solutions.drawing_utils

    ptime = 0
    ctime = 0

    while True:

        success, img = cap.read()

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for handlms in results.multi_hand_landmarks:
                mpdraw.draw_landmarks(img, handlms, mphands.HAND_CONNECTIONS)

        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime

        cv2.putText(img, str(round(fps)), (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Hand-Tracking", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break