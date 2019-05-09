glove_file = open("glove.6B.50d.txt", 'r')
contents = [line.rstrip('\n') for line in glove_file]
for pair in contents:
    word, vec = pair.split(' ', 1)
    glove_dict[word] = vec
# get complete vocabulary from stimuli construction
# vocab = []
glove_dict = {key: val for key, val in glove_dict.items() if key in vocab}
json_file = json.dumps(glove_dict)
f = open("glove_dict.json", 'w')
f.write(json_file)
f.close()
