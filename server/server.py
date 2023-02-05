from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/classify_image', methods = ['GET','POST'] )
def classify_image():
    # When the UI calls this function it will send the image data in a request object
    # This request object is imported from Flask module
    image_data = request.form['image_data']
    # This image data will be base64 encoded string

    response = jsonify(util.classify_image(image_data))
    # jsonify converts it to json

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)