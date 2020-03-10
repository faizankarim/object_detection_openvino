import cv2
import glob

image_paths = glob.glob("3_unzipped_data/**/*.*", recursive=True)
i = 0
# dsize
dsize = (369, 308)  # (0.3 * width, 0.3 * height)
for image in image_paths:
    src = cv2.imread(image, cv2.IMREAD_UNCHANGED)

    # resize image
    output = cv2.resize(src, dsize)

    print("image_name: ", image.split("/")[2], "image_num: ", i)
    i += 1

    cv2.imwrite("4_images_resized/" + image.split("/")[2], output)
