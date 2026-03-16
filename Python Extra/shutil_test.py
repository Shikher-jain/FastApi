import shutil
import os
import time

# print(dir(shutil))

print("Shutil Test [copy] Shutil Test Copy")
shutil.copy('shutil_test.py', 'shutil_test_copy.py')
time.sleep(2)

print("Shutil Test [copy2] Shutil Test Copy 2")
shutil.copy2('shutil_test.py', 'shutil_test_copy2.py')
time.sleep(2)

print("Shutil Test [copytree] Shutil Test Copy Tree")
shutil.copytree('Tricks', 'Tricks_copy', dirs_exist_ok=True)
time.sleep(2)

# os.mkdir('Test_Folder', exist_ok=True)
print("[make directory] Test_Folder")
os.makedirs('Test_Folder', exist_ok=True)
time.sleep(2)

print("Shutil Test [move] Shutil Test Copy to Test_Folder")
shutil.move('shutil_test_copy.py', 'Test_Folder/t1')
shutil.move('shutil_test_copy2.py', 'Test_Folder/t1')
time.sleep(2)

print("[Remove] t [if exists]")
# os.remove('t')
if os.path.exists('t'):
    os.remove('t')

time.sleep(2)

print("[Remove] Test_Folder ")
shutil.rmtree('Test_Folder', ignore_errors=True)

time.sleep(2)

print("[Remove] Tricks_copy ")
shutil.rmtree('Tricks_copy', ignore_errors=True)

time.sleep(2)
print(os.listdir())