import os
from typing import TextIO
from src import quiz

STUDENT_COUNT = 3
QUESTION_FILE_PATH = os.path.join(os.getcwd(), "questions")

def main():
    """Control the flow of the program."""

    # For each student
    for student_count in range(1, STUDENT_COUNT + 1):
        # Create the quiz file.
        quiz_file: TextIO = quiz.create_file(
            os.path.join(QUESTION_FILE_PATH,"python_quiz_question"),
            student_count, "w"
        )
        answer_file: TextIO = quiz.create_file(
            os.path.join(QUESTION_FILE_PATH,"python_quiz_answer"),
            student_count, "r"
        )

        # Write a header in the quiz file
        quiz.write_header(quiz_file, "Python OOP Quiz", student_count,)
        fixed_questions = ["Q:What is the full meaning of OOP?",
                           "Q:What does 'self' represent in OOP?",
                           "Q:What are the main principles of OOP?"
        ]
        quiz.generate_quiz(quiz_file, quiz.python_oop, fixed_questions)

        quiz_file.close()

        quiz_file = quiz.create_file(os.path.join(QUESTION_FILE_PATH,"python_quiz_question"),\
                                    student_count, "r"
                                    )

        score = quiz.grade_answers(quiz_file, answer_file, quiz.python_oop)
        quiz.display_results(score)

        quiz_file.close()
        answer_file.close()

if __name__ == "__main__":
    main()
