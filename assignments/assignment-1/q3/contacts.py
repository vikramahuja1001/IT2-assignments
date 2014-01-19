
from phonenum import *

def create_contacts():
	return {}

def add_contacts(contacts, name, country, phone_num, phone_type):
    if contacts.has_key(name):
        phone_nums = contacts[name]
        phone_nums.append(Phonenum(country,phone_num, phone_type))
    else:
    	contacts[name] = [ Phonenum(country,phone_num, phone_type) ]


def update_contact_number(contacts, contact_name, old_number, new_number):
	if contacts.has_key(contact_name):
		new_number = new_number.strip()
		if len(new_number) is not 10 :
			return False
		if new_number.isdigit() == False:
			return False

		phone_nums=contacts[contact_name]
		for i in range(len(phone_nums)):
			if contacts[contact_name][i][1] == old_number :
				a=list(contacts[contact_name][i])
				a[1]=new_number
				contacts[contact_name][i]=tuple(a)
				return True
	else:
		return False
"""		
c={}
add_contacts(c, 'ken',"", "0911234567890", "home")
add_contacts(c, 'ken',"", "2345678901", "work")
add_contacts(c, 'ken', "","2345678902", "work")
print c
update_contact_number(c, 'ken', "1234567890", "9999999999")
print c
"""
