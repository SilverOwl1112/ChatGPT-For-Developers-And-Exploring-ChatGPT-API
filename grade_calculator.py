import streamlit as st

def calculate_grade(test_scores):
    # Define the grading scale
    grading_scale = {
        'A': 90,
        'B': 80,
        'C': 70,
        'D': 60,
        'F': 0
    }
    
    # Calculate the average test score
    average_score = sum(test_scores) / len(test_scores)
    
    # Determine the grade based on the grading scale
    for grade, score_cutoff in grading_scale.items():
        if average_score >= score_cutoff:
            return grade

def main():
    st.title("Simple Grade Calculator")
    st.write("Enter your test scores below and click 'Calculate Grade'")
    
    # Allow users to input test scores
    test_scores = []
    num_tests = st.number_input("Number of tests:", min_value=1, max_value=10, value=3, step=1)
    for i in range(num_tests):
        test_score = st.number_input(f"Test {i+1} score:", min_value=0, max_value=100, value=0, step=1)
        test_scores.append(test_score)
    
    # Calculate the grade and display the result
    if st.button("Calculate Grade"):
        final_grade = calculate_grade(test_scores)
        st.write(f"Your final grade is: {final_grade}")

if __name__ == "__main__":
    main()
