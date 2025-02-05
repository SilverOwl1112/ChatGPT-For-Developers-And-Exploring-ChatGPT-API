import streamlit as st

def calculate_sgpa(subjects):
    total_credits = sum(subject['credits'] for subject in subjects)
    total_grade_points = sum(subject['grade'] * subject['credits'] for subject in subjects)
    return total_grade_points / total_credits if total_credits != 0 else 0

def calculate_cgpa(semesters):
    total_credits = sum(subject['credits'] for semester in semesters for subject in semester)
    total_grade_points = sum(subject['grade'] * subject['credits'] for semester in semesters for subject in semester)
    return total_grade_points / total_credits if total_credits != 0 else 0

def main():
    st.title("CGPA Calculator")
    
    grade_mapping = {
        'O': 10,
        'A+': 9,
        'A': 8,
        'B+': 7,
        'B': 6,
        'C': 5,
        'U': 0
    }

    num_semesters = st.number_input("Enter the number of semesters:", min_value=1, max_value=12, value=1, step=1)
    semesters = []

    for i in range(num_semesters):
        st.header(f"Semester {i+1}")
        num_subjects = st.number_input(f"Enter the number of subjects for semester {i+1}:", min_value=1, max_value=20, value=1, step=1, key=f"num_subjects_sem{i}")
        subjects = []
        
        for j in range(num_subjects):
            subject_credits = st.number_input(f"Enter the credits of subject {j+1}:", min_value=1, max_value=10, value=3, step=1, key=f"credits_sem{i}_sub{j}")
            subject_grade = st.selectbox(f"Select the grade for subject {j+1}:", options=list(grade_mapping.keys()), key=f"grade_sem{i}_sub{j}")
            subjects.append({'credits': subject_credits, 'grade': grade_mapping[subject_grade]})
        
        semesters.append(subjects)

    if st.button("Calculate CGPA"):
        sgpas = [calculate_sgpa(semester) for semester in semesters]
        cgpa = calculate_cgpa(semesters)
        
        for idx, sgpa in enumerate(sgpas):
            st.write(f"SGPA for Semester {idx+1}: {sgpa:.2f}")
        st.write(f"Overall CGPA: {cgpa:.2f}")

if __name__ == "__main__":
    main()

