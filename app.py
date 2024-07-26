from flask import Flask, render_template, request, jsonify,send_file
import cv2
import base64
import numpy as np
from ultralytics import YOLO

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sw.js')
def serve_sw():
    return send_file('sw.js', mimetype='application/javascript')

@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')
    

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    result_img = process_image(img)
    _, buffer = cv2.imencode('.jpg', result_img)
    result_img_str = base64.b64encode(buffer).decode('utf-8')
    return jsonify({'result': result_img_str})

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json['image']
    img_data = base64.b64decode(data.split(',')[1])
    img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
    result_img = process_image(img)
    _, buffer = cv2.imencode('.jpg', result_img)
    result_img_str = base64.b64encode(buffer).decode('utf-8')
    return jsonify({'result': result_img_str})

def process_image(img):
    trained_model = YOLO('./Test_Model/trained model.pt')
    results = trained_model.predict(img)
    
    for result in results:
        boxes = result.boxes
        for box in boxes:
            xyxy = box.xyxy[0]
            confidence = box.conf[0]
            cls = box.cls[0]
            
            # Convert tensor to numpy array
            xyxy = xyxy.numpy()
            confidence = confidence.numpy()
            cls = cls.numpy()
            
            # Bounding box
            x_min, y_min, x_max, y_max = map(int, xyxy)
            cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            
            label = f'Pothole: {confidence:.2f}'
            cv2.putText(img, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    
    return img

if __name__ == '__main__':
    app.run(debug=True)