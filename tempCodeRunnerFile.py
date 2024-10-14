import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Function to calculate attendance based on total classes held
def calculate_attendance(attended_classes, total_classes):
    if total_classes == 0:  # Prevent division by zero
        return 0
    attendance_score = (attended_classes / total_classes) * 100
    return min(attendance_score, 100)  # Cap attendance score at 100%

# Function to calculate lab attendance based on total lab classes held
def calculate_lab_attendance(lab_attended_classes, total_lab_classes):
    if total_lab_classes == 0:  # Prevent division by zero
        return 0
    lab_attendance_score = (lab_attended_classes / total_lab_classes) * 100
    return min(lab_attendance_score, 100)  # Cap lab attendance score at 100%

# Function to calculate assignment scores based on the selected scheme
def calculate_assignments(assignments_columns, scheme, max_marks):
    if len(assignments_columns) == 0:  # Handle empty assignment columns
        return 0
    if scheme == 'Best Of All':
        best_score = max(assignments_columns)
        return (best_score / max_marks) * 100  # Convert to percentage
    elif scheme == 'Average':
        avg_score = sum(assignments_columns) / len(assignments_columns)
        return (avg_score / max_marks) * 100  # Convert to percentage
    elif scheme == 'Relative Grading':
        max_assignment_score = max(assignments_columns)
        return (sum(assignments_columns) / (max_assignment_score * len(assignments_columns))) * 100
    return 0

# Function to calculate quiz scores based on the selected scheme
def calculate_quizzes(quizzes_columns, scheme, max_marks):
    if len(quizzes_columns) == 0:  # Handle empty quiz columns
        return 0
    if scheme == 'Best Of All':
        best_score = max(quizzes_columns)
        return (best_score / max_marks) * 100  # Convert to percentage
    elif scheme == 'Average':
        avg_score = sum(quizzes_columns) / len(quizzes_columns)
        return (avg_score / max_marks) * 100  # Convert to percentage
    elif scheme == 'Relative Grading':
        max_quiz_score = max(quizzes_columns)
        return (sum(quizzes_columns) / (max_quiz_score * len(quizzes_columns))) * 100
    return 0

# Function to calculate MST scores based on the selected scheme
def calculate_mst(mst_columns, max_marks):
    if len(mst_columns) == 0:  # Handle empty MST columns
        return 0
    best_score = max(mst_columns)
    return (best_score / max_marks) * 100  # Convert to percentage

# Function to calculate the final Continuous Assessment (CW) score
def calculate_cw(attendance_score, lab_attendance_score, assignment_score, quiz_score, mst_score, weights):
    return (attendance_score * weights['attendance'] +
            lab_attendance_score * weights['lab_attendance'] +
            assignment_score * weights['assignments'] +
            quiz_score * weights['quizzes'] +
            mst_score * weights['mst'])  # Add MST weightage

# Main program flow
def main():
    # Initialize Tkinter
    Tk().withdraw()  # Prevent the root window from appearing
    print("Please select the Excel file.")
    file_path = askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    
    if not file_path:
        print("No file selected. Exiting the program.")
        return

    # Load data from Excel
    df = pd.read_excel(file_path, sheet_name='Sheet1')

    # User inputs for maximum values and weights
    total_attendance_classes = int(input("Enter total number of attendance classes held: "))
    total_lab_attendance_classes = int(input("Enter total number of lab attendance classes held: "))
    max_assignment_marks = float(input("Enter maximum assignment marks: "))  # Maximum marks for assignment
    max_quiz_marks = float(input("Enter maximum quiz marks: "))  # Maximum marks for quiz
    max_mst_marks = 20  # Maximum marks for MST

    weights = {
        'attendance': float(input("Enter weightage for attendance: ")) / 100,
        'lab_attendance': float(input("Enter weightage for lab attendance: ")) / 100,
        'assignments': float(input("Enter weightage for assignments: ")) / 100,
        'quizzes': float(input("Enter weightage for quizzes: ")) / 100,
        'mst': float(input("Enter weightage for MST: ")) / 100,  # Add MST weightage input
    }

    # Prepare lists to store dynamic column names
    attendance_cols = [col for col in df.columns if "Attendance" in col and "Lab" not in col]  # Only attendance columns
    lab_attendance_cols = [col for col in df.columns if "Lab Attendance" in col]  # Only lab attendance columns
    assignment_cols = [col for col in df.columns if "Assignment" in col]  # Only assignment columns
    quiz_cols = [col for col in df.columns if "Quiz" in col]  # Only quiz columns
    mst_cols = [col for col in df.columns if "MST" in col]  # Only MST columns

    # User input for schemes
    assignment_scheme = input("Select assignment scheme (Best Of All / Average / Relative Grading): ")
    quiz_scheme = input("Select quiz scheme (Best Of All / Average / Relative Grading): ")

    # Create a list to store results
    results = []

    # Loop through each student and calculate scores
    for index, row in df.iterrows():
        # Debugging: Print the row to see attendance data
        print(f"\nProcessing student: {row['Name']}")
        print(f"Attendance Data: {row[attendance_cols].tolist()}")
        print(f"Lab Attendance Data: {row[lab_attendance_cols].tolist()}")
        print(f"MST Data: {row[mst_cols].tolist()}")

        # Calculate attendance score
        attendance_score = calculate_attendance(row[attendance_cols].sum(), total_attendance_classes)
        
        # Calculate lab attendance score
        lab_attendance_score = calculate_lab_attendance(row[lab_attendance_cols].sum(), total_lab_attendance_classes)
        
        # Calculate assignment score
        assignment_score = calculate_assignments(row[assignment_cols].tolist(), assignment_scheme, max_assignment_marks)
        
        # Calculate quiz score
        quiz_score = calculate_quizzes(row[quiz_cols].tolist(), quiz_scheme, max_quiz_marks)

        # Calculate MST score
        mst_score = calculate_mst(row[mst_cols].tolist(), max_mst_marks)

        # Debugging: Print the calculated scores for the student
        print(f"Calculated Attendance Score: {attendance_score:.2f}%")
        print(f"Calculated Lab Attendance Score: {lab_attendance_score:.2f}%")
        print(f"Assignment Score: {assignment_score:.2f}%")
        print(f"Quiz Score: {quiz_score:.2f}%")
        print(f"MST Score: {mst_score:.2f}%")

        # Calculate final Continuous Assessment score
        final_cw = calculate_cw(attendance_score, lab_attendance_score, assignment_score, quiz_score, mst_score, weights)

        # Store results for terminal output and Excel with percentage sign for CW
        results.append({
            'Name': row['Name'],
            'Roll No': row['Roll No'],
            'Classes Attended (%)': f"{attendance_score:.2f}%",
            'Labs Attended (%)': f"{lab_attendance_score:.2f}%",
            'Assignment Marks Obtained (%)': f"{assignment_score:.2f}%",
            'Quiz Marks Obtained (%)': f"{quiz_score:.2f}%",
            'MST Marks Obtained (%)': f"{mst_score:.2f}%",  # Add MST score to the results
            'CW': f"{final_cw:.2f}%"
        })

    # Print results in terminal
    print("\nResults:")
    print(f"{'Name':<25} {'Roll No':<15} {'Classes Attended (%)':<20} {'Labs Attended (%)':<20} {'Assignment Marks Obtained (%)':<30} {'Quiz Marks Obtained (%)':<25} {'MST Marks Obtained (%)':<25} {'CW':<10}")
    print("="*175)
    for result in results:
        print(f"{result['Name']:<25} {result['Roll No']:<15} {result['Classes Attended (%)']:<20} {result['Labs Attended (%)']:<20} {result['Assignment Marks Obtained (%)']:<30} {result['Quiz Marks Obtained (%)']:<25} {result['MST Marks Obtained (%)']:<25} {result['CW']:<10}")

    # Create a DataFrame from the results
    results_df = pd.DataFrame(results)

    # Save results to Excel
    output_path = "C:/Users/pandy/Downloads/attendance_results.xlsx"  # Change this to your desired output path
    results_df.to_excel(output_path, index=False)

    print(f"\nResults have been saved to '{output_path}'")

if __name__ == "__main__":
    main()
