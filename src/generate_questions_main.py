# src/generate_questions_main.py
import os
from typing import TextIO
from src import quiz
from src.data import python_oop

QUESTION_FILE_PATH = os.path.join(os.getcwd(), "questions")
ANSWER_FILE_PATH = os.path.join(os.getcwd(), "answers")

# Ensure the `questions` and `answers` directories exist
os.makedirs(QUESTION_FILE_PATH, exist_ok=True)
os.makedirs(ANSWER_FILE_PATH, exist_ok=True)

def main():
    """Generate shuffled questions for each student."""
    student_count = int(input("Enter the number of students: "))
    for student_num in range(1, student_count + 1):
        # Create quiz file
        quiz_file: TextIO = quiz.create_file(
        os.path.join(QUESTION_FILE_PATH, "python_quiz_question"), student_num, "w"
        )
        quiz.write_header(quiz_file, "Python OOP Quiz", student_num)
        
        # Generate shuffled questions
        fixed_questions = list(python_oop.keys())  # All questions from data.py
        quiz.generate_quiz(quiz_file, python_oop, fixed_questions)

        print(f"Generated quiz for Student {student_num}")
        quiz_file.close()

        # Create a blank answer file in the `answers` folder
        answer_file: TextIO = quiz.create_file(
        os.path.join(ANSWER_FILE_PATH, "python_quiz_answer"), student_num, "w"
        )
        answer_file.close()

if __name__ == "__main__":
    main()
