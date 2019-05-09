import json
import sys

if __name__ == "__main__":
    filepath = sys.argv[1]
    glove_file = open(filepath, 'r')
    contents = [line.rstrip('\n') for line in glove_file]
    glove_dict = {}
    for pair in contents:
        word, vec = pair.split(' ', 1)
        glove_dict[word] = vec
    json_file = json.dumps(glove_dict)
    f = open("glove_dict.json", 'w')
    f.write(json_file)
    f.close()
