import os
from database import cur
from database import con

menu_status = True



def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(":::MAIN MENU:::")
    print("[1] Create user")
    print("[2] List users")
    print("[3] Exit")
    print("===============")
    
    try:
        opt = int(input('Choose an option: '))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None
    return opt

def create_user():
    uname = input('Username: ')
    uemail = input('E-mail: ')
    passwd = input('Password: ')

    new_user_query = f'''
        INSERT INTO users (username, email, password, role) 
        VALUES ('{uname}','{uemail}' ,'{passwd}' ,1 )
    '''
    
    con.execute(new_user_query)
    con.commit()
    print('User created successfully!')
    os.system('pause')


def list_users():
        cur.execute('SELECT id, username, email, role FROM users')
        users = cur.fetchall()

        if users:
            print("::: USERS LIST :::")
            for user in users:
                print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Role: {user[3]}")
               
        else:
            print("No users found.")
        
        
        os.system('pause')
  

while menu_status:
    op = main_menu()
    
    if op == 1:
        create_user()
    elif op == 2:
        list_users()
    elif op == 3:
        print("Exiting...")
        menu_status = False
    elif op is None:
        continue
    else:
        print("Invalid option. Please try again.")

