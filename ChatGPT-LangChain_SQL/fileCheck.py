import chardet

# Replace 'path_to_your_file.sql' with the actual file path
file_path = 'E:\\3_Research_Development\\GenAI\\ChatGPT-Tabular-Data-main\\Chinook_Sqlite.sql'

# Read a portion of the file to detect the encoding
with open(file_path, 'rb') as file:
    raw_data = file.read(50000000)  # Adjust the number of bytes read as necessary
    result = chardet.detect(raw_data)

# Print the detected encoding
print('encoding-' +result['encoding'])
