try:
    from prettytable import PrettyTable, DOUBLE_BORDER
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "prettytable"])
    from prettytable import PrettyTable, DOUBLE_BORDER


table = PrettyTable()
table.set_style(DOUBLE_BORDER)

school_nam = input("Enter School Name: ")
student_name = input("Enter Student Name: ")
father_name = input("Enter Father's Name: ")
session = (input("Enter Year of Session: "))
roll_no = input("Enter Roll No. of Student: ")
branch = input("Enter Branch of Student: ")
mobile_no = input("Enter Mobile No. of Student: ")

print('\n' + '='*110)
print(f"{school_nam.center(110)}")
print('='*110)
print('\t\t\t\tSTUDENT REPORT CARD\n')

print(f"Name: {student_name}\t\t\tRoll No: {roll_no}")
print(f"Father's Name: {father_name}\t\tBranch: {branch}")
print(f"Session Year: {session}\t\t\tMobile No: {mobile_no}\n")
print('='*110)
print("\t\t\t\t\tRESULTS\n")


n = int(input("Enter number of subjects: "))
subjects = []

for i in range(n):
    print(f"\n--- Subject {i+1} ---")
    subject = input("Enter Subject Name: ")
    
    
    while True:
        try:
            obtained_marks = float(input("Enter Obtained Marks: "))
            break
        except ValueError:
            print("Invalid input! Enter a number.")

    
    while True:
        try:
            total_marks = float(input("Enter Maximum Marks: "))
            if total_marks <= 0:
                print("Total marks must be greater than zero!")
                continue
            break
        except ValueError:
            print("Invalid input! Enter a number.")

    
    percentage = (obtained_marks / total_marks) * 100

    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B+'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    else:
        grade = 'F'

    subjects.append([i+1, subject, obtained_marks , total_marks , grade])


table.field_names = ["S.NO", "SUBJECT", "OBTAINED MARKS", "TOTAL MARKS", "GRADE"]

for row in subjects:
    table.add_row(row)


print(table)


total_obtained = sum([row[2] for row in subjects])
total_max = sum([row[3] for row in subjects])
overall_percentage = (total_obtained / total_max) * 100

print("\n" + "="*110)
print(f"Total Obtained: {total_obtained} / {total_max}")
print(f"Overall Percentage: {overall_percentage:.2f}%")

if overall_percentage >= 90:
    final_grade = 'A+'
elif overall_percentage >= 80:
    final_grade = 'A'
elif overall_percentage >= 70:
    final_grade = 'B+'
elif overall_percentage >= 60:
    final_grade = 'B'
elif overall_percentage >= 50:
    final_grade = 'C'
else:
    final_grade = 'F'

print(f"Final Grade: {final_grade}")
print("="*110)
