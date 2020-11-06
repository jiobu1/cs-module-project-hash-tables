import re
import matplotlib.pyplot as plt

file = open("/Users/jisha/Desktop/Lambda_Course_Work/Coursework/Work/2. Computer Science/5. Hash Tables /cs-module-project-hash-tables/applications/histo/robin.txt", "r+")
text = file.read()



text = text.lower()
words = re.split(r"[^\w']+",text)

print(f"Number of words in text file:  {len(words)}")

for word in words:
    if word in d:
        d[word] +=1
    else:
        d[word] = 1

print(d)

len(d.keys())

d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

plt.figure(figsize=(20,70))
plt.barh(list(d.keys()), d.values(), height=0.5, color='g')
plt.ylim(-1, 411)
plt.show()


