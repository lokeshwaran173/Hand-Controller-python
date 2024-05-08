import cv2
import mediapipe as mp
from pynput.keyboard import Controller as KController

mp_hands = mp.solutions.hands.Hands()
keyboard = KController()

cp = cv2.VideoCapture(0)
x1, x2, y1, y2 = 0, 0, 0, 0

while 1:
    _, image = cp.read()

    image_height, image_width, _ = image.shape
    image = cv2.flip(image, 1)
    rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output_hands = mp_hands.process(rgb_img)
    all_hands = output_hands.multi_hand_landmarks

    if all_hands:
        hand = all_hands[0]
        one_hand_landmark = hand.landmark

        for id, lm in enumerate(one_hand_landmark):
            x = int(lm.x * image_width)
            y = int(lm.y * image_height)

            if id == 12:
                x1, y1 = x, y
            if id == 0:
                x2, y2 = x, y

        distX = x1 - x2
        distY = y1 - y2

        if distY > -140 and distY != 0:
            keyboard.release('d')
            keyboard.release('a')
            keyboard.release('w')
            keyboard.press('s')
            print("S")

        if distY < -200 and distY != 0:
            keyboard.release('s')
            keyboard.release('d')
            keyboard.release('a')
            keyboard.press('w')
            print("W")

        if distX < -100 and distX != 0:
            keyboard.release('s')
            keyboard.release('d')
            keyboard.press('w')
            keyboard.press('a')
            print('A')

        if distX > 55 and distX != 0:
            keyboard.release('a')
            keyboard.release('s')
            keyboard.press('w')
            keyboard.press('d')
            print('D')

    else:
        print('none')
        keyboard.release('d')
        keyboard.release('a')
        keyboard.release('w')
        keyboard.release('s')

    wait = cv2.waitKey(1)
    if wait == ord("q"):
        break

cv2.destroyAllWindows()
