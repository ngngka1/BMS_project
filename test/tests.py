import subprocess
import os
def setUp():
    global command
    # print(os.path.join(os.getcwd().replace(":", ""), "test.db"))
    command = f'python main.py --admin --db="{"test.db"}" --auto-remove'
def test(func):
    tests.append(func)
    return func
tests = [setUp]

def run_with_input(input_data):
    process = subprocess.run(command, input=input_data, text=True, capture_output=True, shell=True)
    if process.stdout:
        print(process.stdout)
    if process.stderr:
        print(process.stderr)
    
@test
def test01():
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
        banquet create dinner "2023-01-01 19:33:23" "hong kong" "hong kong" "[1, 2, 3, 4]" 1 100 true
        banquet list
        quit
    '''
    run_with_input(input_data)
    
# @test
def test02():
    input_data = '''
        meal create fish fishTest 200 NA
        meal create chicken chickenTest 220 NA
        meal create beef beefTest 240 NA
        meal create fish fishTestTwo 2000 NA
        banquet create dinner 2023-01-01 19:33:23 1000 1
        banquet list
    '''
    run_with_input(input_data)