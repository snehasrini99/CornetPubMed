import chardet

# Detect the encoding first
with open('allMeSH_2022.json', 'rb') as file:
    raw_data = file.read(10000)  # Read a chunk of the file
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    print(f"Detected encoding: {encoding}")

# Read and print the first 100 lines of the file
line_limit = 100

with open('allMeSH_2022.json', 'r', encoding=encoding) as file:
    for i in range(line_limit):
        line = file.readline()
        if not line:
            break
        print(line.strip())  # Strip newline characters for cleaner output
