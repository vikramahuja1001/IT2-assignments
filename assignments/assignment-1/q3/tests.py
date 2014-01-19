from contacts import create_contacts
from contacts import add_contacts
from phonenum import *
from contacts import update_contact_number

def test_add_multiple_contact_numbers():
    c = create_contacts()
    add_contacts(c, 'ken',"91", "1234567890", "home")
    add_contacts(c, 'ken',"91", "2345678901", "work")
    add_contacts(c, 'ken',"91", "2345678902", "work")
    assert(len(c.keys()) == 1)
    update=update_contact_number(c,"ken","1234567890","9700881234")
    assert(update==True)

def test_generic_contacts_behavior():
	contacts = {}
	contacts["Guido"] = Phonenum("","098765ab21", "home")
	contacts["Ritchie"] = Phonenum("91","5678904321", "home")
	contacts["Rob"] = Phonenum("","1234567890", "work")
	contacts["Steve"] = Phonenum("92","123456789", "work")
	assert(len(contacts.keys()) == 4)

	phone_steve = contacts["Steve"] 
	assert(phone_steve is None)
	assert(contacts["Guido"] is None)

	try:
	    phone_ken = contacts["ken"]
	    assert(0)
	except KeyError as e:
		assert(1)

if __name__ == '__main__':
    test_generic_contacts_behavior()
    test_add_multiple_contact_numbers()
