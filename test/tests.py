import subprocess
import os
def setUp():
    global command
    # print(os.path.join(os.getcwd().replace(":", ""), "test.db"))
    global db
    db = "test.db"
    command = f'python main.py --db="{db}" --debug'
    
def test(func):
    def wrapper():
        x = func()
        clean_up_after_each()
        return x
    tests.append(wrapper)
    return wrapper

def clean_up_after_each():
    os.remove(db)
    
tests = [setUp]

def run_with_input(input_data, admin_mode=False):
    global command
    x = command
    if admin_mode:
        x += " --admin"
    process = subprocess.run(x, input=input_data, text=True, capture_output=True, shell=True)
    if process.stdout:
        print(process.stdout)
    if process.stderr:
        print(process.stderr)
    
# @test
def test_banquet_full():
    input_data = '''
        meal create fish fishTest 200 NA
        meal create chicken chickenTest 220 NA
        meal create beef beefTest 240 NA
        meal create fish fishTestTwo 2000 NA
        meal create beef beefTestTwo 100 NA
        meal list
        staff create joe a Catering
        staff create joe b Catering
        staff create joe c "Guest Services"
        banquet create dinner "2023-01-01 19:33:23" "hong kong" "hong kong" "[1, 2, 3, 4]" 1 1 true
        banquet list
        banquet update 1 dinnerUpdated \n\n\n\n\n\n\n
        banquet list
        quit
    '''
    run_with_input(input_data, admin_mode=True)
    
    
    input_data = '''
        attendee register testuser2@email.com 123 j j staff 87654321 home polyu
        attendee login testuser2@email.com 123
        banquet register 1\n\n\n
        quit
    '''
    run_with_input(input_data)
    
    input_data = '''
        banquet list
        quit
    '''
    run_with_input(input_data, admin_mode=True)
    
# @test
def test_update_attendee():
    input_data = '''
        attendee register testuser@email.com 123 jo jo student 12345678 home polyu
        attendee login testuser@email.com 123
        attendee update testuserJOJO@email.com je je \n\n\n\n\n
        attendee info
        quit
    '''
    run_with_input(input_data)
    
# Banquet listAttendees <bin>
# @test
def test_banquet_list_attendees():
    input_data = '''
        meal create fish fishTest 200 false
        meal create chicken chickenTest 220 false
        meal create beef beefTest 240 false
        meal create fish fishTestTwo 2000 false
        meal create beef beefTestTwo 100 false
        meal list
        staff create joe a Catering
        staff create joe b Catering
        staff create joe c "Guest Services"
        banquet create dinner "2023-01-01 19:33:23" "hong kong" "hong kong" "[1, 2, 3, 4]" 1 1 true
        attendee register testuser1@email.com 123 joa jo student 12345678 home polyu
        attendee login testuser1@email.com 123
        banquet register 1
        \n\n\n
        
        attendee register testuser2@email.com 123 job jo student 12345678 home polyu
        attendee login testuser2@email.com 123
        banquet register 1
        \n\n\n
        
        attendee register testuser3@email.com 123 joc jo student 12345678 home polyu
        attendee login testuser3@email.com 123
        banquet register 1
        \n\n\n
        
        attendee register testuser4@email.com 123 jod jo student 12345678 home polyu
        attendee login testuser4@email.com 123
        banquet register 1
        \n\n\n
        
        attendee register testuser5@email.com 123 joe jo student 12345678 home polyu
        attendee login testuser5@email.com 123
        banquet register 1
        \n\n\n
        
        attendee register testuser6@email.com 123 jof jo student 12345678 home polyu
        attendee login testuser6@email.com 123
        banquet register 1
        \n\n\n
        
        attendee register testuser7@email.com 123 jog jo student 12345678 home polyu
        attendee login testuser7@email.com 123
        banquet register 1
        \n\n\n
        
        banquet listattendees 1
        
        quit
    '''
    run_with_input(input_data, admin_mode=True)

# @test
def test_attendee_types():
    input_data = '''
        attendee register testuser1@email.com 123 joa jo student 12345678 home polyu
        attendee register testuser2@email.com 123 job jo alumni 12345678 home polyu
        attendee register testuser3@email.com 123 joc jo student 12345678 home polyu
        attendee register testuser4@email.com 123 jod jo staff 12345678 home polyu
        attendee register testuser5@email.com 123 joe jo student 12345678 home polyu
        attendee register testuser6@email.com 123 jof jo student 12345678 home polyu
        attendee register testuser7@email.com 123 jog jo student 12345678 home polyu
        report attendeetypes
        quit
    '''
    run_with_input(input_data, admin_mode=True)

# @test
def test_popular_meals_report():
    input_data = '''
        meal create fish fishTest 200 false
        meal create chicken chickenTest 220 false
        meal create beef beefTest 240 false
        meal create fish fishTestTwo 2000 false
        meal create beef beefTestTwo 100 false
        meal create beef beefTestThree 100 false
        meal create beef beefTestFour 100 false
        meal create beef beefTestFive 120 true
        meal list
        staff create joe a Catering
        staff create joe b Catering
        staff create joe c "Guest Services"
        banquet create dinner "2023-01-01 19:33:23" "hong kong" "hong kong" "[1, 2, 3, 8]" 1 1 true
        banquet create dinnertwo "2023-01-01 19:33:23" "hong kong" "hong kong" "[2, 6, 7, 8]" 1 1 true
        banquet create dinnerthree "2023-01-01 19:33:23" "hong kong" "hong kong" "[1, 5, 7, 8]" 1 1 true
        
        
        report popularmeals
        quit
    '''
    run_with_input(input_data, admin_mode=True)
    
# @test
def test_inadequate_meal():
    input_data = '''
        meal create fish fishTest 200 NA
        meal create chicken chickenTest 220 NA
        meal create beef beefTest 240 NA
        meal create fish fishTestTwo 2000 NA
        meal create beef beefTestTwo 100 NA
        meal list
        staff create joe a Catering
        staff create joe b Catering
        staff create joe c "Guest Services"
        banquet create dinner "2023-01-01 19:33:23" "hong kong" "hong kong" "[1, 3, 4]" 1 1 true
        banquet list
        banquet update 1 dinnerUpdated \n\n\n\n\n\n\n
        banquet list
        quit
    '''
    run_with_input(input_data, admin_mode=True)
   
# @test
def test_attendence_report():
    input_data = '''
        meal create beef beefTestTwo 100 false
        meal create beef beefTestThree 100 false
        meal create beef beefTestFour 100 false
        meal create beef beefTestFive 120 true
        staff create joe a Catering
        banquet create dinner "2023-01-01 19:33:23" "hong kong" "hong kong" "[1, 2, 3, 8]" 1 123 true
        attendee register testuser1@email.com 123 joa jo student 12345678 home polyu
        attendee login testuser1@email.com 123
        banquet register 1
        \n\n\n
        
        attendee register testuser2@email.com 123 job jo student 12345678 home polyu
        attendee login testuser2@email.com 123
        banquet register 1
        \n\n\n
        
        attendee register testuser3@email.com 123 joc jo student 12345678 home polyu
        attendee login testuser3@email.com 123
        banquet register 1
        \n\n\n
        
        attendee register testuser4@email.com 123 jod jo student 12345678 home polyu
        attendee login testuser4@email.com 123
        banquet register 1
        \n\n\n
        
        attendee register testuser5@email.com 123 joe jo student 12345678 home polyu
        attendee login testuser5@email.com 123
        banquet register 1
        \n\n\n
        
        attendee register testuser6@email.com 123 jof jo student 12345678 home polyu
        attendee login testuser6@email.com 123
        banquet register 1
        \n\n\n
        
        attendee register testuser7@email.com 123 jog jo student 12345678 home polyu
        attendee login testuser7@email.com 123
        banquet register 1
        \n\n\n
        
        quit
    '''
    
    run_with_input(input_data, admin_mode=True)
    
    input_data = '''
        Attendee attend 6 1
        Attendee attend 1 1
        Attendee attend 2 1
        banquet listAttendees 1
        report attendence
        quit
    '''
    
    run_with_input(input_data, admin_mode=True)

# @test
def test_staff_attendence():
    input_data = '''
        meal create beef beefTestTwo 100 false
        meal create beef beefTestThree 100 false
        meal create beef beefTestFour 100 false
        meal create beef beefTestFive 120 true
        staff create joe a Catering
        banquet create dinner "2023-01-01 19:33:23" "hong kong" "hong kong" "[1, 2, 3, 8]" 1 123 true
        banquet create dinnertwo "2023-01-01 19:33:23" "hong kong" "hong kong" "[1, 2, 3, 8]" 1 123 true
        banquet create dinnerthree "2023-01-01 19:33:23" "hong kong" "hong kong" "[1, 2, 3, 8]" 1 123 true
        
        staff attend 1 1
        
        report staffattendence
        quit
    '''
    run_with_input(input_data, admin_mode=True)

@test
def test_criteria():
    input_data = '''
        meal create fish fishTest 200 false
        meal create chicken chickenTest 220 false
        meal create beef beefTest 240 false
        meal create fish fishTestTwo 2000 false
        meal create beef beefTestTwo 100 false
        meal list
        staff create joe a Catering
        staff create joe b Catering
        staff create joe c "Guest Services"
        banquet create dinner "2023-01-01 19:33:23" "hong kong" "hong kong" "[1, 2, 3, 4]" 1 1 true
        banquet create lunch "2023-01-01 19:33:23" "hong kong" "hong kong" "[1, 2, 3, 4]" 1 1 true
        banquet create dinnertwo "2023-01-01 19:33:23" "hong kong" "hong kong" "[1, 2, 3, 4]" 1 1 true
        banquet list "[nameContains=din, datebefore=2024-01-01 19:33:23]"
        banquet list
        quit
    '''
    run_with_input(input_data, admin_mode=True)
    
# @test
# def test_banquet_list