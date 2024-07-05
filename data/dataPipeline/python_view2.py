def read_first_lines(file_path, num_lines=10):
    with open(file_path, 'r') as file:
        for _ in range(num_lines):
            line = file.readline()
            if line:
                print(line.strip())
            else:
                break

# Usage
file_path1 = 'raw_texts.txt'
read_first_lines(file_path1, 10)

file_path2 = 'labels.txt'
read_first_lines(file_path2, 10)
