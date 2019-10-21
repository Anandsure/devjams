import csv
import senti
import time
x=[]
text=[]
y=[]
with open('/Users/anand/Desktop/devJAMS/material/reviews.csv','rt')as f:
    data = csv.reader(f)
    i=0
    for row in data:
        i+=1
        if i <=80 and i!=1:
            #print(row)
            x.append(row[0][0])
            text.append(row[1])
            #print('no of stars:',row[0][0])
        elif i == 1:
            print('i=1')
        else:
            break
#print(text)
#print(x)
print(len(text), len(x))
su=0
for i in x:
    g = int(i)
    su+=g
oor = su/len(x)
print('or', oor)

for i in range(79):
    sentiment = senti.get_senti(text[i])
    temp = int(x[i])*sentiment['score']
    #print(temp)
    time.sleep(0.2)
    y.append(temp)

s=0
for i in y:
    s+=i
nr = s/len(y)
print(nr)
