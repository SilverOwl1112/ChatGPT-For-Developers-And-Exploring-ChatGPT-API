import streamlit as st

def calculate_cgpa(semester_data):
    total_credits = 0
    total_subject_credits_times_grades = 0
    
    # Define the grade mapping
    grade_mapping = {'O': 10.0, 'A+': 9.0, 'A': 8.0, 'B+': 7.0, 'B': 6.0, 'C': 5.0, 'U': 0.0}
    
    # Iterate through semester data
    for semester in semester_data:
        semester_total_credits = 0
        semester_subject_credits_times_grades = 0
        
        # Iterate through subjects in the semester
        for subject in semester['subjects']:
            subject_credits = subject['credits']
            subject_grade = grade_mapping[subject['grade']]
            semester_total_credits += subject_credits
            semester_subject_credits_times_grades += subject_credits * subject_grade
        
        total_credits += semester_total_credits
        total_subject_credits_times_grades += semester_subject_credits_times_grades
    
    if total_credits == 0:
        return 0.0
    
    return total_subject_credits_times_grades / total_credits

def main():
    st.title("Simple CGPA Calculator")
    st.write("Enter your semester details below and click 'Calculate CGPA'")
    
    # Define the grade mapping
    grade_mapping = {'O': 10.0, 'A+': 9.0, 'A': 8.0, 'B+': 7.0, 'B': 6.0, 'C': 5.0, 'U': 0.0}
    
    # Allow users to input semester data
    semester_data = []
    num_semesters = st.number_input("Enter the number of semesters:", min_value=1, max_value=10, value=1, step=1)
    for i in range(num_semesters):
        semester = {}
        semester['semester_number'] = i + 1
        semester['subjects'] = []
        st.write(f"Semester {i+1}")
        num_subjects = st.number_input(f"Enter the number of subjects for Semester {i+1}:", min_value=1, max_value=10, value=3, step=1)
        for j in range(num_subjects):
            subject_credits = st.number_input(f"Enter the credits of subject {j+1}:", min_value=1, max_value=10, value=3, step=1)
            subject_grade = st.selectbox(f"Select grade for subject {j+1}:", ['O', 'A+', 'A', 'B+', 'B', 'C', 'U'])
            semester['subjects'].append({'credits': subject_credits, 'grade': subject_grade})
        semester_data.append(semester)
    
    # Calculate and display SGPA for each semester
    for semester in semester_data:
        total_subject_credits_times_grades = 0
        total_credits = 0
        for subject in semester['subjects']:
            total_subject_credits_times_grades += grade_mapping[subject['grade']] * subject['credits']
            total_credits += subject['credits']
        sgpa = total_subject_credits_times_grades / total_credits
        st.write(f"Your GPA for semester {semester['semester_number']} is: {sgpa}")
    
    # Calculate and display CGPA
    cgpa = calculate_cgpa(semester_data)
    st.write(f"Your overall CGPA for {num_semesters} semesters is: {cgpa:.2f}")

if __name__ == "__main__":
    main()
