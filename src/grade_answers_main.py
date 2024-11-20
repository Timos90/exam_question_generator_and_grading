import os
from typing import TextIO
from src import quiz
from src.data import python_oop

QUESTION_FILE_PATH = os.path.join(os.getcwd(), "questions")
ANSWER_FILE_PATH = os.path.join(os.getcwd(), "answers")

def main():
    """Grade answers provided by students."""
    student_count = int(input("Enter the number of students: "))
    for student_num in range(1, student_count + 1):
        # Check if both quiz and answer files exist
        question_file_path = os.path.join(QUESTION_FILE_PATH, f"python_quiz_question{student_num}.txt")
        answer_file_path = os.path.join(ANSWER_FILE_PATH, f"python_quiz_answer{student_num}.txt")
        
        if not os.path.exists(question_file_path):
            print(f"Error: Missing question file for Student {student_num} ({question_file_path})")
            continue
        if not os.path.exists(answer_file_path):
            print(f"Error: Missing answer file for Student {student_num} ({answer_file_path})")
            continue
        
        # Open the quiz and answer files
        quiz_file: TextIO = open(question_file_path, "r")
        answer_file: TextIO = open(answer_file_path, "r")
        
        # Grade answers
        score, incorrect_questions = quiz.grade_answers(quiz_file, answer_file, python_oop)
        
        # Display results
        print(f"Results for Student {student_num}:")
        print(f"Score: {score}%")
        if incorrect_questions:
            print("Review your incorrect answers:")
            for question, correct_answer in incorrect_questions:
                print(f"{question}\nCorrect Answer: {correct_answer}")
        print("-" * 40)
        
        quiz_file.close()
        answer_file.close()

if __name__ == "__main__":
    main()