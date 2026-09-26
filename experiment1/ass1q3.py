import pandas as pd
def get_grade(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    return 'F'
students = {
    'Student Name': ['Amit', 'Riya', 'Sourav', 'Neha', 'Rahul'],
    'Roll Number': [101, 102, 103, 104, 105],
    'Marks': [92, 85, 78, 67, 90],
    'Attendance': [88, 92, 80, 75, 95]
}
df = pd.DataFrame(students)
df['Grade'] = df['Marks'].apply(get_grade)
print(df)

