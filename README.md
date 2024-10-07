# Attendance and Class Assessment Calculator

This Python script calculates students' attendance, lab attendance, assignment, and quiz scores based on various user-defined schemes and weights. It outputs the Continuous Assessment (CW) score for each student and saves the results in an Excel file, including the percentage for each section.

## Features
- **Attendance Calculation**: Calculates the attendance percentage for each student based on total attended and total held classes.
- **Lab Attendance Calculation**: Calculates lab attendance similarly to regular attendance.
- **Assignment Score Calculation**: Three schemes are supported: 
  - **Best Of All**: Takes the best assignment score.
  - **Average**: Averages all assignment scores.
  - **Relative Grading**: Uses relative grading based on the maximum assignment score.
- **Quiz Score Calculation**: Same schemes as assignment calculation.
- **Weighted Continuous Assessment (CW)**: Combines attendance, lab attendance, assignment, and quiz scores based on user-defined weights to calculate the final CW score.
- **Excel Export**: Outputs results in Excel format with percentage symbols for clarity.

## Requirements
- Python 3.x
- Pandas
- Tkinter (for file dialog)

Install dependencies using:
```bash
pip install pandas
