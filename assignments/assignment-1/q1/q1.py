##the code will be wrong if user_id is not a string and is a int


import time

Users = {
		1: ("anurag","vizag","112233"),
		2: ("aditya","jodhpur","112234"),
		3: ("sarthak","jaipur","325532"),
		4: ("shubham","udaipur","233222"),
	}
Acquaintances = {
		1: [],
		2: [],
		3: [],
		4: [],
		}
Messages = {
		1:[],
		2:[],
		3:[],
		4:[],									}

def add_friend(user_id , friend_id):
	if user_id in Users.keys():
		if user_id in Acquaintances.keys():
			if friend_id not in Acquaintances[user_id]:
				Acquaintances[user_id].append(friend_id)
		else:
			a=[]
			a.append(friend_id)
			Acquaintances[user_id]=a
			print Acquaintances[user_id]
	else:
		return False




def add_friends(user_id , friends_id):
	a=[]
	for i in range(len(friends_id)):
		#problem when len==1
		a.append(friends_id[i])
	if user_id in Acquaintances.keys():
		for i in range(len(a)):
			if a[i] not in Acquaintances[user_id]:
				Acquaintances[user_id].append(a[i])
	else:
		Acquaintances[user_id]=a



def remove_user(user_id):
	if user_id in Users.keys():
		Users.pop(user_id)
		return True
	else:
		return False



def get_friends(user_id):
	#problem in forming a tuple
	if user_id in Acquaintances.keys():
		a=tuple(Acquaintances[user_id])
		return a
	else:
		print None


#global message_id
message_id=1

def send_message(sender_id,receiver_id,msg):
	if sender_id in Users.keys():
		if receiver_id in Users.keys():
			if receiver_id not in Messages.keys():
				msg[1]=message_id
				message_id=message_id+1
				time1=time.localtime()
				date=str(time1[2])+"."+str(time1[1])+"."+str(time1[0])	
				times=str(time1[3])+":"+str(time1[4])+":"+str(time1[5])
				msg[3]=date
				msg[4]=times
				a=[]
				a.append(msg)
				Messages[receiver_id]=a
				return True
			else:
				msg[1]=message_id
				message_id=message_id+1
				time1=time.localtime()
				date=str(time1[2])+"."+str(time1[1])+"."+str(time1[0])	
				times=str(time1[3])+":"+str(time1[4])+":"+str(time1[5])
				msg[3]=date
				msg[4]=times
				Messages[receiver_id].append(msg)
				#print Messages[receiver_id]
				return True
		else:
			return False
	else:
		return False




def send_group_message(sender_id,receivers_id,msg):
	a=[]
	flag=0
	if sender_id not in Users.keys():
		return
	for i in range(len(receivers_id)):
		#problem when len==1
		a.append(receivers_id[i])
	#print a
	for i in range(len(a)):
		if a[i] in Users.keys():
			flag=1
		else:
			flag=0
			break
	if flag==0:
		return False
		return
	else:
		for i in range(len(a)):
			send_message(sender_id,a[i],msg)


def get_messages_from_friend(receiver_id,friend_id):
	b=[]
	if receiver_id in Users.keys():
		if friend_id in Users.keys():
			a=Messages[receiver_id]
			for i in a:
				if i[0]==friend_id:
					b.append(i[2])
			return tuple(b)
		else:
			return None
	else:
		return None

			
	

def get_messages_from_all_friends(receiver_id):
	if receiver_id in Users.keys():
		a=Messages[receiver_id]
		allm=[]
		for i in a:
			allm.append(i[2])
		return tuple(allm)
	else:
		return None



				
def delete_message(user_id,msg_id):
	#	print Messages
	if user_id in Users.keys():
		if user_id in Messages.keys():
			#		print Messages[user_id]
			length=len(Messages[user_id])
			flag=0
		#	print length
			for i in range(length):
				if msg_id == Messages[user_id][i][1]:
					msg=Messages[user_id][i]
					Messages[user_id].remove(msg)
					flag=1
					print True
		#	print Messages[user_id]
			if flag==0:
				return False
		else:
			return False
	else:
		return False




def delete_all_messages(user_id):
	if user_id in Users.keys():
		if user_id in Messages.keys():
			print Messages[user_id]
			length= len(Messages[user_id])
			print length
			for i in range(length):
				#Messages[user_id].remove(Messages[user_id][i])
				Messages[user_id].remove(Messages[user_id][0])



def delete_messaged_from_friend(receiver_id,friend_id):
	if receiver_id in Users.keys():
		if friend_id in Users.keys():
			if receiver_id in Messages.keys():
				print Messages[receiver_id]
				length=len(Messages[receiver_id])
				for i in range(length-1,-1,-1):
					if Messages[receiver_id][i][0]==friend_id:
						Messages[receiver_id].remove(Messages[receiver_id][i])
				print Messages[receiver_id]



#Acquaintances={"user_id_1":["user_id_2","user_id_3"],"user_id_2":["user_id_1"]}



#Users={ "user_id_1":("vikram1","gurgaon","03/09/1994"),"user_id_2":("vikram2","gurgaon","03/09/1994"),"user_id_3":("vikram3","gurgaon","03/09/1994")}


#Messages={}


