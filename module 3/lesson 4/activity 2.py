school_name = "Future Star Academy"
school_location = "Dhaka"
academic_year = 2026
total_students = 450
principal_name = "Mr. Rahman"

def student_section():
    print("\n=== Student Section ===")
    print("School:", school_name)
    print("Academic Year:", academic_year)
    print("Total Students", total_students)
    print("Welcome to our school!")

def teacher_section():
    print("\n=== Teacher Section ===")
    print("School:", school_name)
    print("Principal:", principal_name)

def school_announcement():
    print("\n School Announcement ===")
    print("School:", school_name)
    print("Academic Year:", academic_year)
    print("Total Students", total_students)

student_section()
teacher_section()
school_announcement()

print("\nUpdating School Information...")

academic_year = 2027
total_student = 500

student_section()
teacher_section()
school_announcement()