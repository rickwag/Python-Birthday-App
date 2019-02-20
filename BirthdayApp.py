#with open("birthfile.txt","w+") as file:
#    file.write("test"+","+"birthday app")
#    file.write("\ntest2"+","+"birthday test")
while True:
	birthdict={}
	file=open("birthfile.txt","r")
	lines=file.readlines()
	for line in lines:
	    cleanline=line.strip("\n")
	    key,value=cleanline.split(",")
	    birthdict[key]=value
	    file.close()
	name=input("Enter name to get birthday:(press enter to quit) ")
	if name in birthdict:
		print(birthdict[name])
	elif name == "":
		break
	else:
		print(name,"not in the records, enter",name,"birthday's below")
		birthday=input()
		if birthday == "":
			break
		else:
			 with open("birthfile.txt","a") as file:
			        file.write("\n"+name+","+birthday)
#birthdict.update(key:value)

