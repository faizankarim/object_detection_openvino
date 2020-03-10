import json
import csv

csvs = (["5_csvs/train.csv", "2_jsons/boxy_labels_train.json"], ["5_csvs/valid.csv", "2_jsons/boxy_labels_valid.json"])

width = 369
height = 308
class_name = "car"
rescale = 0.15  #rescale value same as for images.

for csv_name in csvs:
    with open(csv_name[0], 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["filename", "width", "height", "class", "xmin", "ymin", "xmax", "ymax"])
    output_json = json.load(open(csv_name[1]))
    for car_name in output_json:
        print(output_json[car_name])
        for car in output_json[car_name]["vehicles"]:
            with open(csv_name[0], 'a', newline='') as file:
                writer = csv.writer(file)
                xmin = int(car["AABB"]['x1'] * rescale)
                ymin = int(car["AABB"]['y1'] * rescale)
                xmax = int(car["AABB"]['x2'] * rescale)
                ymax = int(car["AABB"]['y2'] * rescale)
                writer.writerow(
                    [car_name.split('/')[2], width, height, class_name, xmin, ymin, xmax, ymax])
