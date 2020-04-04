location = "test.hi-en.en"
location2 = "test.hi-en.hi"
file = open(location, 'r', encoding="utf-8")
file2 = open(location2, 'r', encoding="utf-8")
data = [line.rstrip() for line in file]
data2 = [line.rstrip() for line in file2]
#print(data[:100])

data = data[:77000]
data2 = data2[:77000]

def write(file, data):
    with open(file, 'w', encoding="utf-8") as f:
        for item in data:
            f.write("%s\n" % item)

write("en.txt", data)
write("hi.txt",data2)


