from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder=".")


@app.get("/")
def home():
    return send_from_directory(".", "index.html")


@app.post("/verify")
def verify():
    file = request.files.get("image")
    if not file:
        return jsonify({"error": "No image uploaded"}), 400

    return jsonify({
        "status": "suspicious",
        "confidence": 0.75,
        "source": "Demo placeholder",
        "similarity": 0.82,
    })


if __name__ == "__main__":
    app.run(debug=True)
