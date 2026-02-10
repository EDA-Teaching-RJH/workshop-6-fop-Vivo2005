sample_bay = ["silica","Basalt","Silica","Iron Dust"]
print (sample_bay[0])
print (sample_bay[-1])
print (len(sample_bay))

for i in range(len(sample_bay)):
    print ("transmitting sampla data for :" , sample_bay [i])

repeat=0
new_findings=[]
while repeat < 3:
    new_rock= input("New rock type: ")
    new_findings.append(new_rock)
    repeat=repeat+1
print (new_findings)