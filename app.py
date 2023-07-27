import os, glob
from flask import Flask, request, jsonify
from image2vec import image2vec

app = Flask(__name__)

@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def static_file(path):
    return app.send_static_file(path)

@app.route("/images", methods=["GET"])
def get_image_names():
    image_file_paths = [os.path.basename(p) for p in glob.glob('static/images/*.jpg')]
    return jsonify({'imageFileNames': image_file_paths}), 200

@app.route("/vector", methods=["GET"])
def get_image_vector():
    image_file_name = request.args['name']
    image_file_path = f'static/images/{image_file_name}'
    image_vector = image2vec(image_file_path)
    return jsonify({'vector': image_vector}), 200

if __name__ == "__main__":
    app.run()