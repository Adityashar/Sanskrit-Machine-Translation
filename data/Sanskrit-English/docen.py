import re

location = "./data/Sanskrit-English/en-sa.en.bped"
req = open(location, 'r', encoding="utf-8").read()

#req = [re.sub(r'\(.*\)', '', line.rstrip()) for line in file]

text = re.sub('<[^<]+>', "", req)
text1=text.split('\n')[:-1]
non_empty_lines = text1#[line for line in text1 if line.strip() != ""]
print(len(text1))
#text1=""
article=""
list1=text1
#for i in range(len(non_empty_lines)):
#    ans=non_empty_lines[i]
#    article = re.sub(r'\([^)]*\)', r'', ans)
#    article = re.sub(r'\[[^\]]*\]', r'', article)
#    article = re.sub(r'<[^>]*>', r'', article)
#    article = re.sub(r'^https?:\/\/.*[\r\n]*', '', article)
#    article = article.replace(u'\ufeff','')
#    article = article.replace(u'\xa0', u' ')
#    article = article.replace('  ', ' ')
#    article = article.replace(' , ', ', ')
#    
#    text1+=article+'\n'
#    article = re.sub('[0-9]', '', article)
#    list1.append(article.lstrip())

#print(data[:100])



train = list1[:int(0.85*len(list1))]
valid = list1[int(0.85*len(list1)) + 1: int(0.9*len(list1))]
test = list1[int(0.9*len(list1)) + 1:]

print(len(train), len(valid), len(test))


def write(file, data):
    with open(file, 'w', encoding="utf-8") as f:
        for item in data:
            f.write("%s\n" % item)

write("data/en-sa.en.train", train)
write("data/en-sa.en.valid", valid)
write("data/en-sa.en.test", test)
#write("en-sa.en.all", list1)
