import cv2
from datetime import datetime
def main():
    video = cv2.VideoCapture(r"C:\Users\hp\Desktop\video.mp4")
    frame_per_second= video.get(cv2.CAP_PROP_FPS)
    initial_time = datetime.strptime("00:00:00","%H:%M:%S")
    video_start = datetime.strptime("00:00:30","%H:%M:%S")
    video_end = datetime.strptime("00:00:35","%H:%M:%S")
 
    video_start_frame=frame_per_second*(video_start-initial_time).total_seconds()  #get the start frame
    video_end_frame=frame_per_second*(video_end-initial_time).total_seconds()
    output = cv2.VideoWriter(
        "output.avi", cv2.VideoWriter_fourcc(*'XVID'),
      frame_per_second, (1366, 768))
    counter = 1
 
    while(True):
        ret, frame = video.read()
        if(ret):
            frame=cv2.resize(frame, (1366,768))
            if counter>=video_start_frame and counter<=video_end_frame:
                cv2.rectangle(frame, (600, 300), (700, 400),
                          (0, 0, 255), -1)
                output.write(frame)
            cv2.imshow("output", frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
            counter+=1
        else:
            break
    cv2.destroyAllWindows()
    output.release()
    video.release()
 
 
if __name__ == "__main__":
    main()