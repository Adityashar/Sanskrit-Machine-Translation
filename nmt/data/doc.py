location = "data/englishdatasupervised.txt"
file = open(location, 'r', encoding="utf-8")

data = [line.rstrip() for line in file]

#print(data[:100])

train = data[:int(0.6*len(data))]
valid = data[int(0.6*len(data)) + 1: int(0.8*len(data))]
test = data[int(0.8*len(data)) + 1:]

print(len(train), len(valid), len(test))

def write(file, data):
    with open(file, 'w', encoding="utf-8") as f:
        for item in data:
            f.write("%s\n" % item)

write("train.sn-en.en", train)
write("valid.sn-en.en", valid)
write("test.sn-en.en", test)


