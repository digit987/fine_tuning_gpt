import json

training_data = []
validation_data = []

with open('emoji.json', 'r', encoding='utf-8') as emojis: 
    emojis = json.load(emojis)

training_size = int(len(emojis) * (2/3))

for emoji in range(len(emojis)):
    conversation = {}
    conversation["prompt"] = "Show the emoji with \"" + emojis[emoji]["description"] + "\" under category \"" + emojis[emoji]["category"] + "\""
    conversation["completion"] = emojis[emoji]["emoji"]
    if emoji <= training_size:
        training_data.append(conversation)
    else:
        validation_data.append(conversation)

print(len(validation_data), len(training_data))
print(training_data[0:3])

training_file_name = "training_data.jsonl"
validation_file_name = "validation_data.jsonl"

def prepare_data(dictionary_data, file_name):
    
    with open(file_name, 'w', encoding='utf-8') as outfile:
        for entry in dictionary_data:
            json.dump(entry, outfile)
            outfile.write('\n')

prepare_data(training_data, training_file_name)
prepare_data(validation_data, validation_file_name)
