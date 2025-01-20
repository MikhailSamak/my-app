import os

folder_path = "C:\\AI\\AI_Projects\\site_project\\memory"

try:
    test_file = os.path.join(folder_path, "test_file.txt")
    with open(test_file, "w") as f:
        f.write("This is a test.")
    os.remove(test_file)
    print("Права записи есть!")
except PermissionError:
    print("Нет прав записи в папку.")
