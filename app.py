from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    file.save(f"./uploads/{file.filename}")
    return jsonify({"message": f"{file.filename} uploaded successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
