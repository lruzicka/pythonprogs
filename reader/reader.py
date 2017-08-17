import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from textwrap import wrap


with open('resteam.csv','r') as d:
    data = d.readlines()

print("Parsing the data file.")

header = data.pop(0)
header = header.split(';')

rawtable = []

for line in data:
    row = line.split(';')
    rawtable.append(row)

print("Correct data found in %s columns." % len(header))
choice = int(input("Which column to display?: "))

title = header[choice]
answers = []
for row in rawtable:
    answers.append(row[choice])

cleantable = {}

for item in answers:
    if item not in cleantable.keys():
        cleantable[item] = 0
        print('Unique choice found.')
    else:
        pass


for key in cleantable.keys():
    count = answers.count(key)
    cleantable[key] = count
       
print(cleantable)

tmplabels = cleantable.keys()
labels = []
for lab in tmplabels:
    lab = "\n".join(wrap(lab, 25))
    labels.append(lab)

sizes = []
for item in tmplabels:
    sizes.append(cleantable[item])

font = "Liberation Sans"
print("Using font: %s" % font)
plt.rcParams['font.sans-serif'] = [font, 'sans-serif']

fig1, ax1 = plt.subplots()
colors = ('yellow', 'lime','red','cyan','orange')


patches, texts, autotexts = ax1.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# změna stylu písma
proptease = fm.FontProperties()
proptease.set_size('xx-large')
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)
plt.title(title)
ax1.title.set_fontsize(25)
plt.show()


   
    
