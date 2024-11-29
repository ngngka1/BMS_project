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
    
@test
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
        quit
    '''
    run_with_input(input_data, admin_mode=True)
    
    input_data = '''
        attendee register testuser@email.com 123 jo jo student 12345678 home none
        attendee login testuser@email.com 123
        banquet register 1\n\n\n
        quit
    '''
    run_with_input(input_data)
    input_data = '''
        attendee register testuser2@email.com 123 j j staff 87654321 home none
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
def test02():
    pass