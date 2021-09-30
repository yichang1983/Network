data = []
with open('my_switches.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
#print (data)

for line in data:
    print("Configuring Switch:" + line )
