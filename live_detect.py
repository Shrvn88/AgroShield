import numpy as np
import cv2
import os
import numpy as np


def live_detect():


    args = {"confidence": 0.5, "threshold": 0.3}
    flag = False

    labelsPath = "./yolo-coco/coco.names"
    LABELS = open(labelsPath).read().strip().split("\n")
    final_classes = ['bird', 'cat', 'dog', 'sheep', 'horse', 'cow', 'elephant', 'zebra', 'bear', 'giraffe', 'monkey']

    weightsPath = os.path.abspath("./yolo-coco/yolov3-tiny.weights")
    configPath = os.path.abspath("./yolo-coco/yolov3-tiny.cfg")

    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]

# vdo_path = "test.mp4"

    vs = cv2.VideoCapture(0)
    writer = None
    (W, H) = (None, None)

    flag = True

    while True:

        (grabbed, frame) = vs.read()

        if not grabbed:
            break

        if W is None or H is None:
            (H, W) = frame.shape[:2]

        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)

        layerOutputs = net.forward(ln)

        boxes = []
        confidences = []
        classIDs = []

        for output in layerOutputs:

            for detection in output:

                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]

                if confidence > args["confidence"]:
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")

                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        idxs = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"],
                            args["threshold"])

        if len(idxs) > 0:

            for i in idxs.flatten():

                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])

                if (LABELS[classIDs[i]] in final_classes):

                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
                    text = "{}: {:.4f}".format(LABELS[classIDs[i]],
                                           confidences[i])
                    cv2.putText(frame, text, (x, y - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 200, 0), 2)

                    global abc
                    abc = text[:-8]

                    if (flag):
                        flag = False



        else:
            flag = True

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

            # Yield the frame in byte format
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    