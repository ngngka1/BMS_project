# tests/test_main.py
import subprocess

def test_main_script():
    # Command to run your main script
    command = ["python", "main.py"]
    
    # Input to send to the script
    input_data = "attendee help\n"
    
    # Running the command
    result = subprocess.run(command, input=input_data, text=True, capture_output=True)
    
    # Assertions
    assert result.returncode == 0  # Check if the command was successful
    assert "Processed: Hello, World!" in result.stdout  # Check the output
    assert result.stderr == ""  # Ensure there are no errors

if __name__ == "__main__":
    test_main_script()