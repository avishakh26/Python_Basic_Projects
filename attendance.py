


print('''***[[[Here we can save class attendance 
welcome to the attendance tracker]]]***''')




class Attendance:
    def __init__(self):
        self.records = {}



    def mark_attendance(self, student_name):
        if student_name not in self.records:
            self.records[student_name] = True

            print(f"Attendance marked for {student_name}.")


        else:
            print(f"{student_name} is already marked present.")



    def view_attendance(self):
        print("Attendance Records:")

        for student, present in self.records.items():
            status = "Present" if present else "Absent"
            print(f"{student}: {status}")



def main():
    attendance_tracker = Attendance()


    while True:
        action = input("Enter 'mark' to mark attendance, 'view' to see records, or 'exit' to quit: ").strip().lower()
        if action == 'mark':
            name = input("Enter student name: ").strip()
            attendance_tracker.mark_attendance(name)


        elif action == 'view':
            attendance_tracker.view_attendance()
        elif action == 'exit':
            break


        else:
            print("Invalid input. Please try again.")




if __name__ == "__main__":
    main()
