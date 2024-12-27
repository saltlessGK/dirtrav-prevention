import os
from flask import Flask, request, Response

app = Flask(__name__)
BASE_DIR = os.path.abspath("./resources/files") #Only meant to access test3.txt

@app.route('/view', methods=['GET'])
def view_file():
    filename = request.args.get('file')
    
    if not filename:
        return "No file specified.", 400

    file_path = os.path.abspath(os.path.join(BASE_DIR, filename))
    print(file_path)

    if not file_path.startswith(BASE_DIR):
        return "Access denied.", 403

    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return Response(content, mimetype='text/plain')
        except Exception as e:
            return f"Error reading file: {e}", 500
    else:
        return "File not found.", 404

if __name__ == "__main__":
    app.run(debug=True)
