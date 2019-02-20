with open("birthfile.txt","w+") as file:
    file.write("test"+","+"birthday app")
    file.write("\ntest2"+","+"birthday test")
import time
def find():
	name=input("Enter name: ")
	if name in birthdict:
		print(birthdict[name])

	else:
		print("Name not in records  select add to update")
	return name
def add():
	name=input("Enter name to add: ")
	birthday=input("Enter birthday of "+name+":")
	if birthday is not "":
		with open("birthfile.txt","a") as file:
			file.write("\n"+name+","+birthday)
		print("Records succesfully updated")
	else:
		inloop=False
def change():
	name=input("Enter name to change:")
	new_birth=input("Enter new birthday of "+name+":")
	if new_birth is not "":
		with open("birthfile.txt","a") as file:
			file.write("\n"+name+","+new_birth)

	else:
		inloop=False
def delete():
	name=input("Enter name to delete: ")
	confirm=input("Do you really wanna delete the records about"+name+"? (press enter to accept or type no")
	file=open("birthfile.txt","r")
	lines=file.readlines()
	file.close()
	for line in lines:
		if name in line:
			pass
		else:
			with open("birthfile.txt","w") as file:
				file.write(line) 

print("........BIRTHDAY APP........")
print("Select Using Numbers")
print("1. Find Birthday\n2. Add Birthday\n3. Change Birthday\n4. Delete birthday")


inloop=True
while inloop:
	time.sleep(3)
	birthdict={}
	file=open("birthfile.txt","r")
	lines=file.readlines()
	for line in lines:
	    cleanline=line.strip("\n")
	    key,value=cleanline.split(",")
	    birthdict[key]=value
	    file.close()

	choice=input("Choose:(press enter to quit) ")
	if choice is "":
		inloop=False
	elif choice is "1":
		find()
	elif choice is "2":
		add()
	elif choice is "3":
		change()
	elif choice is "4":
		delete()


