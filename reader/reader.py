import matplotlib.pyplot as plt



with open('results.csv','r') as d:
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

labels = cleantable.keys()
sizes = []
for item in labels:
    sizes.append(cleantable[item])

font = "Liberation Sans"

print("Using font: %s" % font)

plt.rcParams['font.sans-serif'] = [font, 'sans-serif']


fig1, ax1 = plt.subplots()

ax1.pie(sizes,labels=labels,autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title(title)
plt.show()


    
    
