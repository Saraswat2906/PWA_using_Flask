from flask import Flask, render_template, request, jsonify, send_file
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sw.js')
def serve_sw():
    return send_file('sw.js', mimetype='application/javascript')

@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')

@app.route('/upload_photo', methods=['POST'])
def upload_photo():
    if 'photo' not in request.files:
        return jsonify(success=False, message="No photo part")
    file = request.files['photo']
    if file.filename == '':
        return jsonify(success=False, message="No selected photo")
    if file:
        filename = "input_image.jpg"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        # Perform image processing or detection here if needed
        return jsonify(success=True, image_url=f"/{app.config['UPLOAD_FOLDER']}/{filename}")

@app.route('/upload_video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify(success=False, message="No video part")
    file = request.files['video']
    if file.filename == '':
        return jsonify(success=False, message="No selected video")
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify(success=True, video_url=f"/{app.config['UPLOAD_FOLDER']}/{filename}")

if __name__ == '__main__':
    app.run(debug=True)
