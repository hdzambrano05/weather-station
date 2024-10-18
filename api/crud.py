'''
C > Create (INSERT)
R > Read (SELECT)
U > Update (UPDATE)
D > Deleate (DELETE)

'''
import os
from database import cur
from database import con

def main_menu():
    print(":::MAIN MENU:::")
    print("[1] Create users")
    print("[2] List users")
    print("[3] Salir")
    print("===============")


def create_user():

    new_user_query = '''
        INSERT INTO users (username,email,password,role) 
        VALUES ('Harold','hd@mail.com','123456', '1')
    ''' 
    con.execute(new_user_query)
    con.commit()

    print(new_user_query)
    os.system('pause')

    con.close()

create_user()