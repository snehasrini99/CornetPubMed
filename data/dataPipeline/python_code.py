import json

# Load JSON data from a file with ISO-8859-1 encoding
with open("allMeSH_2022.json", "r", encoding="ISO-8859-1") as file:
    data = json.load(file)

# Initialize lists to hold text and labels
title_abstract_texts = []
mesh_majors = []

# Track mismatches
missing_abstract = 0
missing_title = 0
missing_mesh_major = 0

# Define the maximum number of lines to process
max_articles = 10000
total_articles = 0

# Process the first 100,000 articles to extract title_abstract_texts and mesh_majors
for article in data["articles"]:
    if total_articles >= max_articles:
        break
    
    if "abstractText" in article and "title" in article and "meshMajor" in article:
        # Concatenate abstractText and title
        title_abstract_text = f'{article["abstractText"]} /SEP/ {article["title"]}'
        title_abstract_texts.append(title_abstract_text)
        
        # Format each term in meshMajor appropriately
        formatted_mesh_major = []
        for term in article["meshMajor"]:
            # Replace spaces with underscores, remove commas, keep hyphens
            formatted_term = term.replace(' ', '_').replace(',', '').replace('-', '_')
            formatted_mesh_major.append(formatted_term)
        
        # Join terms with spaces
        formatted_mesh_major_str = ' '.join(formatted_mesh_major)
        mesh_majors.append(formatted_mesh_major_str)
    else:
        if "abstractText" not in article:
            missing_abstract += 1
        if "title" not in article:
            missing_title += 1
        if "meshMajor" not in article:
            missing_mesh_major += 1

    total_articles += 1

# Ensure both lists have the same length
assert len(title_abstract_texts) == len(mesh_majors), "Mismatch in lengths of texts and labels"

# Write to raw_texts.txt
with open("raw_texts.txt", "w", encoding="utf-8") as text_file:
    for title_abstract in title_abstract_texts:
        text_file.write(title_abstract + "\n")

# Write to raw_labels.txt
with open("raw_labels.txt", "w", encoding="utf-8") as labels_file:
    for mesh_major in mesh_majors:
        labels_file.write(mesh_major + "\n")

# Check the length of the labels and texts
def count_lines(file_path):
    with open(file_path, 'r') as file:
        count = sum(1 for _ in file)
    return count

# Check the length of the labels and texts
input_file = 'raw_labels.txt'
length_labels = count_lines(input_file)
print(f"The file {input_file} has {length_labels} lines.")
input_file = 'raw_texts.txt'
length_texts = count_lines(input_file)
print(f"The file {input_file} has {length_texts} lines.")

# Print missing counts and total articles processed
print(f"Total articles processed: {total_articles}")
print(f"Articles missing abstract: {missing_abstract}")
print(f"Articles missing title: {missing_title}")
print(f"Articles missing meshMajor: {missing_mesh_major}")
