#with open("birthfile.txt","w+") as file:
 #   file.write("test"+","+"birthday app")
  #  file.write("\ntest2"+","+"birthday test")
import time
def find():
	name=input("Enter name: ")
	if name in birthdict:
		print(birthdict[name])
		return True
	elif name == "":
		return False
	else:
		print("Name not in records  choose add to update")

def add():
	name=input("Enter name to add: ")
	if name != "":
		birthday = input("Enter birthday of " + name + ":")
		with open("birthfile.txt","a") as file:
			file.write(name+","+birthday+"\n")
		print("Records succesfully updated")
		return True
	else:
		print("Cancelled!!!")
		return False

def change():
	name=input("Enter name to change:")
	if name != "":
		if name in birthdict:
			new_birth = input("Enter new birthday of " + name + ":")
			if new_birth != "":
				delete(name)
				with open("birthfile.txt","a") as file:
					file.write(name+","+new_birth+"\n")
				print("Records successfully updated")
				return True
			else:
				return False
		else:
			print("Name not in records!!!")
	else:
		print("Cancelled!!!")
		return False




def delete(Name=None):
	if Name == None:
		name=input("Enter name to delete: ")
	else:
		name=Name
	#confirmation

	if name is not "" and name in birthdict:
		with open("birthfile.txt", "r+") as file:
			lines = file.readlines()
			file.seek(0)
			for line in lines:
				if name not in line:
					file.write(line)
				else:
					file.truncate()
		#print("Records successfully updated")

	else:
		print("Cancelled!!!")
		return False

def admin():
	password=input("Enter Password!!! ")
	if password == "hitman":
		print("Access Granted")
		time.sleep(2)
		print("1. Display records\n2. Delete all records")
		choice=input("Enter choice: ")
		if choice == "1":
			if birthdict != {}:
				for key,value in birthdict.items():
					print(key+" - "+value)
			else:
				print("No records found!!!")
		elif choice == "2":
			with open("birthfile.txt","w") as file:
				file.truncate()
		else:
			print("Unavailable")
		return True
	else:
		print("Password incorrect!!")
		time.sleep(2)
		print("ACCESS DENIED!!!!!")
		return False

print("........BIRTHDAY APP........")
print("Select Using Numbers")
print("1. Find Birthday\n2. Add Birthday\n3. Change Birthday\n4. Delete birthday\n5. Admin")
print("Press enter for cancelling")

inloop=True
while inloop:
	birthdict={}
	file=open("birthfile.txt","r")
	lines=file.readlines()
	for line in lines:
		if line != "":
			cleanline=line.strip("\n")
			key,value=cleanline.split(",")
			birthdict[key]=value
			file.close()
		else:
			pass

	choice=input("Choose:(press enter to quit) ")
	if choice is "":
		break
	elif choice is "1":
		if find() == False:
			continue
	elif choice is "2":
		if add() == False:
			continue
	elif choice is "3":
		if change() == False:
			continue
	elif choice is "4":
		if delete() == False:
			continue
	elif choice is "5":
		if admin() == False:
			continue
	time.sleep(3)

