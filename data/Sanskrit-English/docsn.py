#from cltk.tokenize.sentence import TokenizeSentence as TS
import re
#from indicnlp.tokenize import indic_tokenize  


#tokenizer = TS('sanskrit')

location = "./data/Sanskrit-English/en-sa.sa.bped"

req = open(location, 'r', encoding="utf-8").read()

#req = [re.sub(r'\(.*\)', '', line.rstrip()) for line in file]

text = re.sub('<[^<]+>', "", req)
text1=text.split('\n')[:-1]
non_empty_lines = [line for line in text1 if line.strip() != ""]
text1=""
article=""
list1=[]
for i in range(len(non_empty_lines)):
    ans=non_empty_lines[i]
    article = re.sub(r'\([^)]*\)', r'', ans)
    article = re.sub(r'\[[^\]]*\]', r'', article)
    article = re.sub(r'<[^>]*>', r'', article)
    article = re.sub(r'^https?:\/\/.*[\r\n]*', '', article)
    article = article.replace(u'\ufeff','')
    article = article.replace(u'\xa0', u' ')
    article = article.replace('  ', ' ')
    article = article.replace(' , ', ', ')
    devanagari_nums = ('०','१','२','३','४','५','६','७','८','९')
    for c, n in enumerate(devanagari_nums):
        article = re.sub(n, str(c), article)
    text1+=article+'\n'
    article = re.sub('[0-9]', '', article)
    article = article.lstrip()
    #print(type(article))	
   # tok_line = indic_tokenize.trivial_tokenize(article)
    #string = ' '.join(tok_line)	
    list1.append(article)
    

tokenized_data = list1

#for line in data[:100]:
 #   print(line)
  #  tok_line = tokenizer.tokenize(line)
   # tokenized_data.append(tok_line)

train = tokenized_data[:int(0.85*len(tokenized_data))]
valid = tokenized_data[int(0.85*len(tokenized_data)) + 1: int(0.9*len(tokenized_data))]
test = tokenized_data[int(0.9*len(tokenized_data)) + 1:]

print(len(train), len(valid), len(test))


def write(file, data):
    with open(file, 'w', encoding="utf-8") as f:
        for item in data:
            f.write("%s\n" % item)

write("data/en-sa.sa.train", train)
write("data/en-sa.sa.valid", valid)
write("data/en-sa.sa.test", test)
#write("en-sa.sa.all", tokenized_data)
