import gzip

def compress_data(data):
    return gzip.compress(data)

def decompress_data(compressed_data):
    return gzip.decompress(compressed_data)
