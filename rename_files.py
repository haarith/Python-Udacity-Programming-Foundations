import os

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"C:\github-repos\Python-Udacity-Programming-Foundations\prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\github-repos\Python-Udacity-Programming-Foundations\prank")

    # (2) for each file, rename filename
    for file_name in file_list:
        print("Old name = " + file_name)
        from string import digits
        os.rename(file_name, file_name.translate({ord(k):None for k in digits}))
        print("New name = " + file_name)

    os.chdir(saved_path)
    print("Completed successfully!")
    
rename_files()
