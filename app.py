from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/list-files', methods=['GET'])
def list_files():
    # Get the folder path from query parameter, default to current directory
    folder_path = request.args.get('folder', '.')
    
    if not os.path.isdir(folder_path):
        return jsonify({'error': 'Invalid folder path'}), 400

    try:
        # List all files in the directory
        files = os.listdir(folder_path)
        file_list = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
        return jsonify({'files': file_list})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
