from flask import jsonify

def handle_compression_error(error):
    error_message = str(error)
    response = jsonify({'error': error_message})
    response.status_code = 500  # Internal Server Error
    return response
