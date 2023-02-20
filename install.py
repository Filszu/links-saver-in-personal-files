import winreg
import os
import sys

# Get the path to the directory where the install.py script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Set the name of the Python script file
script_name = "main.py"

# Set the file extension to associate with the script
file_ext = ".links"

# Construct the path to the Python executable and the script file
# python_exe = os.path.join(script_dir, "python.exe"

python_exe = "C:\Python311\python.exe"
python_exe =  sys.executable
script_path = os.path.join(script_dir, script_name)

print("python path->\n",python_exe,"\nscript path \n",script_path)



# Get the path to the Python executable and the script file
command = f'"{python_exe}" "{script_path}" "%1"'

# Set up the registry keys for the file extension association
key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\\Classes\\" + file_ext)
winreg.SetValue(key, "", winreg.REG_SZ, "Link File")
winreg.SetValueEx(key, "DefaultIcon", 0, winreg.REG_SZ, python_exe + ",0")
subkey = winreg.CreateKey(key, r"shell\open\command")
winreg.SetValue(subkey, "", winreg.REG_SZ, command)

# Tell the user that the association was successful
print(f"File extension {file_ext} is now associated with {script_name}.")

input()

# this code has been generated with chat gpt support
