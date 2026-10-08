import csv
from tkinter import Tk, filedialog

FILE_NAME = None
def select_file():
    # Let the user create a new csv file or popen an existing one 
    global FILE_NAME
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    while True:
        mode = input("Select mode\n1: Create new file\n2:Open an existing file: ")
        if mode == "1":
            path = filedialog.asksaveasfilename(
                title="Create a new csv file",
                filetypes=[("CSV files", "*.csv")],
                defaultextension=".csv"
            )
            if path:
                open(path, "a",newline="").close()  
        elif mode == "2":
            path = filedialog.askopenfilename(
                title="Open an existing file",
                filetypes=[("CSV files","*.csv")]
            )
        else:
            print("Invalid optiion")
            continue
        if path:
            FILE_NAME = path
            print(f"Selected file: {FILE_NAME}")
            root.destroy()
            return
        print("No file selected. Please try again.")
def add_students():
    try:
        name = input("Enter name: ")
        course = input("Enter course: ")
        mat_no = input("Enter Matric number: ")
        age = input("Enter your age: ")
        with open(FILE_NAME,"a",newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name,course,mat_no,age])
        print("Added\n")
    except PermissionError:
        print("Try adding again.Make sure Excel/Notepad is not open")
def view_students():
    try:
        with open(FILE_NAME,"r",newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
         print("No records found\n")
def delete_students():
    mat_no = str(input("Enter matric number to clear: "))
    try:
        with open(FILE_NAME, "r", newline="") as f:
            rows = list(csv.reader(f))

        # keep only rows that do NOT contain mat_no
        new_rows = [row for row in rows if mat_no not in row]

        if len(new_rows) == len(rows):
            print("Matric number not found.\n")
        else:
            with open(FILE_NAME, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(new_rows)
            print("Deleted\n")

    except FileNotFoundError:
        print("File not found.\n")
select_file()
        

while True:
    choice = input("Enter your option:\n1: Add\n2: View students\n3: Delete\n4: Exit \n")
    if choice == "1":
        add_students()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_students()
    elif choice == "4":
        break