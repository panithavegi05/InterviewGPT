import cv2
import time

def monitor_attention():

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    cap = cv2.VideoCapture(0)

    face_frames = 0
    away_frames = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        faces = face_cascade.detectMultiScale(
            gray,
            1.3,
            5
        )

        if len(faces) > 0:

            face_frames += 1

            status = "Focused"

        else:

            away_frames += 1

            status = "Looking Away"

        cv2.putText(
            frame,
            status,
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow(
            "InterviewGPT Attention",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    return {
        "face_frames": face_frames,
        "away_frames": away_frames
    }