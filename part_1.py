#task 1
sample_bay = ["Basalt","Silica","Iron", "Dust"]
print (sample_bay[0])
print (sample_bay[-1])
print (len(sample_bay))

#task2
for i in range(len(sample_bay)):
    print ("transmitting sampla data for :" , sample_bay [i])

#task3
repeat=0
new_findings=[]
while repeat < 3:
    new_rock= input("New rock type: ").strip().lower().title()
    new_findings.append(new_rock)
    repeat=repeat+1
print (new_findings)

#task 4
if "Dust" in sample_bay :
    i=sample_bay.index("Dust")
    sample_bay.pop(i)
    print(sample_bay)
else:
    print("sample not found")
    
