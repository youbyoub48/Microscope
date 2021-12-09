import cv2

def Video():
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)

    while True:
        try:
            check, frame = webcam.read()
            print(check) #prints true as long as the webcam is running
            print(frame) #prints matrix values of each framecd
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()
                cv2.imread('saved_img.jpg')
                #img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                print("Processing image...")
                cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                print("Resizing image to 28x28 scale...")
                print("Resized...")
                print("Image saved!")
            
                return "save"
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
            
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    Video()