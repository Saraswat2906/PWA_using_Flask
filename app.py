from flask import Flask, render_template, request, send_file, redirect, url_for
import os
import importlib
import predictions

app = Flask(__name__, static_folder='static', template_folder='templates')
importlib.reload(predictions)

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
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        file_path = os.path.join('static', 'input_image.jpg')
        file.save(file_path)
        result = predictions.detect_in_image(file_path)
        
        return send_file('static/output.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
