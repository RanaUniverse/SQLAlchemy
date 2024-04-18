import sys
sys.dont_write_bytecode = True


'''
This is the function from where i will try to call different function 
so that i can understand how my database functions are wowrking 
# database_main_class.py is the module where i will defines a class 
# database_fun.py is the module where the functions are written 
this is the main scripts where i will try to run different databse operation

-Rana Universe 🍌🍌🍌

'''


from database_fun import session, Student
from database_fun import add_user_and_return_id_


student_1 = Student("Rana", 22, "Male", "RanaUniverse321@gmail.com",22)




if __name__ == "__main__":
    print("main funciton is starting")
    add_user_and_return_id_("Rana", 22, "Male", "RanaUniverse321@gmail.com")












