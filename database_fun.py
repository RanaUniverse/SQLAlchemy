

'''
This is my module so that i dont need to change the datagase_main_class module 
for call any function
Here i will defines some functions here so that i can use this in other main program
1st: add_user_and_return_id_ ✅
2nd: i will add a fun which will take the id_ and then it will search
    in my database about the row and return the objec fully

-Rana Universe 🍌🍌🍌
'''


import sys
sys.dont_write_bytecode = True



from datetime import date
from pathlib import Path


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from database_main_class import Base, Student



db_filename = "student_info.db"
folder_name = Path("RanaUniverse") / "database_store_folder"
folder_name.mkdir(parents= True, exist_ok= True)
file_location = folder_name / db_filename
file_url = f"sqlite+pysqlite:///{file_location}"

engine = create_engine(url= file_url, echo= False)

Session = sessionmaker(bind= engine)
session = Session()

Base.metadata.create_all(engine)




def add_student(name, age, gender, email, dob):
    '''This not maybe good to use i just created it without intension'''
    new_student = Student(name=name, age=age, gender=gender, email=email, date_of_birth=dob)
    try:
        session.add(new_student)
        session.commit()
        return True, "Student added successfully."
    except Exception as e:
        print(e)
        return False
    


def add_user_and_return_id_1(name:str=None, age:int=0, gender:str=None, email:str=None, dob:date=None):
    '''
    No Need Function 
    i return the id_ so that after insert some data i can use this id_
    to to perform some next operation
    '''

    new_student = Student(name, age, gender, email, dob)
    session.add(new_student)
    session.commit()
    inserted_id_ = new_student.id_
    session.close()
    print("User added successfully. ID:", inserted_id_)
    return inserted_id_


def add_user_and_return_id_(name:str=None, age:int=0, gender:str=None, email:str=None, dob:date=None):
    '''
    i return the id_ so that after insert some data i can use this id_
    to to perform some next operation: This is good as try except is here
    '''

    try:
        new_student = Student(name, age, gender, email, dob)
        session.add(new_student)
        session.commit()
        inserted_id = new_student.id_
        print("User added successfully. ID:", inserted_id)
        return inserted_id
    
    except Exception as e:
        session.rollback()
        print("Error adding user:", e)
        return None
    finally:
        session.close()



def get_student_count_by_name(student_name: str = ""):
    ''''
    here i will pass the student name and i will get the full student obj
    of all the row
    '''
    try:
        student = session.query(Student).filter_by(name = student_name).all()
        count_1 = student.__len__()
        count_2 = len(student)

        print(count_1)
        print(count_2)
        return student
    except Exception as e:
        print("Error retrieving student:", e)
        return None









if __name__ == "__main__":
    # add_user_and_return_id("ranfdfa",232,343,4543,5,435,4,54,5,4)
    add_user_and_return_id_("ranfdfa", 232, "Male", "example@example.lcom", date.today())
    get_student_count_by_name("Rana")





