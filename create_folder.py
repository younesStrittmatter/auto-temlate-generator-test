import os

os.makedirs('test_folder')

with open(os.path.join('test_folder', "testfile.txt"), "w") as file:
    file.write("This is a test file")