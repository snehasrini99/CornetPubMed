import json
# Load JSON data from a file with ISO-8859-1 encoding
with open("allMeSH_2022.json", "r", encoding="ISO-8859-1") as file:
    data = json.load(file)

# Extracting abstractText and meshMajor
abstract_texts = [article["abstractText"] for article in data["articles"]]
mesh_majors = [", ".join(article["meshMajor"]) for article in data["articles"]]

# Writing to text.txt
with open("raw_texts.txt", "w") as text_file:
    for abstract in abstract_texts:
        text_file.write(abstract + "\n")

# Writing to labels.txt
with open("labels.txt", "w") as labels_file:
    for mesh_major in mesh_majors:
        labels_file.write(mesh_major + "\n")
