from q1 import *

add_friend(1,2)
add_friend(2,1)
add_friend(3,4)
add_friends(4,(1,2,3))
#print Acquaintances

remove_user(4)	   
get_friends(4)
   
remove_user(4)	   
get_friends(4)
get_friends_of_friends(1)
send_message(1,2,"blah")
send_group_message(1,(2,3,4),"blah_blah")
get_messages_from_friend(2,1)
get_messages_from_all_friends(4)
get_birth_day_messages(3)
delete_message(1, 2)
delete_messages(2,(1,2,3,4,5,6))
delete_all_messages(3)
delete_messages_from_friend(4,3)

