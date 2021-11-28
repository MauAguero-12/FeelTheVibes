import csv


lyrics = []

with open('lyrics_a.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # print(csv_reader)
    try:
        for row in csv_reader:
            if line_count != 0:
                lyrics.append(row[5])
            line_count += 1
    except:
        pass

with open('lyrics_b.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # print(csv_reader)
    try:
        for row in csv_reader:
            if line_count != 0:
                lyrics.append(row[5])
            line_count += 1
    except:
        pass

with open('lyrics_c.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # print(csv_reader)
    try:
        for row in csv_reader:
            if line_count != 0:
                lyrics.append(row[5])
            line_count += 1
    except:
        pass

with open('lyrics_d.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # print(csv_reader)
    try:
        for row in csv_reader:
            if line_count != 0:
                lyrics.append(row[5])
            line_count += 1
    except:
        pass



f = open('all-words.txt', 'r')
all = f.readlines()
f.close()
for i in range(len(all)):
    all[i] = all[i][:-1]

f = open('positive-words.txt', 'r')
positive = f.readlines()
f.close()
for i in range(len(positive)):
    positive[i] = positive[i][:-1]

f = open('negative-words.txt', 'r')
negative = f.readlines()
f.close()
for i in range(len(negative)):
    negative[i] = negative[i][:-1]

f_pos = []
f_neg = []

for word in all:
    w = " " + word + " "
    in_lyrics = False
    for lyric in lyrics:
        if w in lyric:
            in_lyrics = True
            break
    
    if word in positive:
        f_pos.append(word)

    if word in negative:
        f_neg.append(word)



with open('words.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #writer.writerow(['Palabra', 'Sentimiento'])

    for word in f_pos:
        writer.writerow([word, 'Positivo', '|'])

    for word in f_neg:
        writer.writerow([word, 'Negativo', '|'])
















'''
file = open("lyrics_a.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()
'''
