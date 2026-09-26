import pandas as pd
def main():
    students = {
        "Student Name": ["Amit", "Riya", "Sourav", "Neha", "Rahul", "Priya", "Karan", "Meera", "Arjun", "Isha"],
        "Roll Number": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        "Marks": [72, 88, 91, 67, 84, 95, 78, 82, 69, 90],
        "Attendance": [85, 92, 88, 80, 91, 96, 75, 87, 79, 94],
    }
    df = pd.DataFrame(students)
    filtered_df = df[df["Marks"] > 80]
    print("==== Students with Marks Above 80 ====")
    print(filtered_df)
if __name__ == "__main__":
    main()
