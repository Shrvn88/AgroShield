import os
from flask import Flask, render_template, Response
from Animal_detect import detection
from alert import alert
from live_detect import live_detect
from volumecontrol import set_volume
from decimal import Decimal


app = Flask(__name__)

@app.route('/history')
def imgshow():
    image_files = [f for f in os.listdir("static") if f.endswith((".jpg", ".jpeg", ".png", ".gif"))]
    return render_template("abc.html", image_files=image_files)

@app.route('/vol/<volume>')
def vol1(volume):
    v = Decimal(volume)
    return set_volume(v)

@app.route('/play')
def play():
    return alert()

@app.route('/detect')
def detect():
    return detection()

@app.route('/live')
def index():
    return render_template('horizontalView.html')

@app.route('/rotated')
def reouted():
    return render_template('rotated.html')

@app.route('/video_feed')
def video_feed():
    return Response(live_detect(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

