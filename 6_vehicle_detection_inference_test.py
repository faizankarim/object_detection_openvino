import cv2
from utils.inference import run_inference_for_single_image, get_bounding_box_on_image
from PIL import Image

video_src = 'utils/input.mp4'
score = 0.4
output_path = '9_inference_test/output.avi'
W, H = None, None
writer = None
cap = cv2.VideoCapture(video_src)
while True:
    ret, frame = cap.read()
    if W is None or H is None:
        (H, W) = frame.shape[:2]
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        writer = cv2.VideoWriter(output_path, fourcc, 30, (W, H), True)
    if type(frame) == type(None):
        break
    im_pil = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(im_pil)

    output_dict = run_inference_for_single_image(image=im_pil)
    for i in range(int(output_dict['num_detections'])):
        if output_dict['detection_scores'][i] > score:
            left, right, top, bottom = get_bounding_box_on_image(im_pil, output_dict['detection_boxes'][i][0],
                                                                 output_dict['detection_boxes'][i][1],
                                                                 output_dict['detection_boxes'][i][2],
                                                                 output_dict['detection_boxes'][i][3])
            cv2.rectangle(frame, (left, top), (right, bottom),
                          (0, 255, 0), 2)

    cv2.imshow('video', frame)
    writer.write(frame)
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
