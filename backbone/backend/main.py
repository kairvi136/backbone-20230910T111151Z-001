from flask import Flask, request, jsonify
from compression import compress_data, decompress_data
from serialization import serialize_data, deserialize_data
from error_handling import handle_compression_error
from config import NETWORK_ADDRESS, PORT

app = Flask(__name__)

@app.route('/compress', methods=['POST'])
def compress():
    try:
        data = request.json.get('data')
        
        # Compress and serialize data
        compressed_data = compress_data(serialize_data(data))
        
        return jsonify({'compressed_data': compressed_data.decode()})
    except Exception as e:
        return handle_compression_error(e)

@app.route('/decompress', methods=['POST'])
def decompress():
    try:
        compressed_data = request.json.get('compressed_data')
        
        # Decompress and deserialize data
        data = deserialize_data(decompress_data(compressed_data.encode()))
        
        return jsonify({'data': data})
    except Exception as e:
        return handle_compression_error(e)

if __name__ == '__main__':
    app.run(host=NETWORK_ADDRESS, port=PORT)
