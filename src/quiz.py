import os
import random
from typing import TextIO
from .data import python_oop


def create_file(file_path: str, student_num: int, mode: str = "w") -> TextIO:
    return open(f"{file_path}{student_num}.txt", mode)


def write_header(file: TextIO, title: str, student_num: int) -> None:
    file.write("Name:\n\nDate:\n\n")
    file.write(f"\t\t{title}(paper {student_num})")

def generate_quiz(file: TextIO, questions: dict[str, list[str]], fixed_questions: list[str]) -> None:
    # Randomize the fixed questions
    random.shuffle(fixed_questions)
    for question in fixed_questions:
        options = questions[question]
        file.write(f"\n\n{question}\n")
        shuffled_options = random.sample(options, len(options))  # Shuffle options
        for option_index, option in enumerate(shuffled_options, start=97):
            # Convert index to corresponding alphabet letter
            option_letter = chr(option_index)
            file.write(f"{option_letter}. {option}\n")

    # Create a list of non-fixed questions
    non_fixed_questions = [q for q in questions if q not in fixed_questions]

    # Randomize the order of non-fixed questions
    random.shuffle(non_fixed_questions)

    # Write non-fixed questions to the file
    for question in non_fixed_questions:
        options = questions[question]
        file.write(f"\n\n{question}\n")
        shuffled_options = random.sample(options, len(options))  # Shuffle options
        for option_index, option in enumerate(shuffled_options, start=97):
            # Convert index to corresponding alphabet letter
            option_letter = chr(option_index)
            file.write(f"{option_letter}. {option}\n")
        file.write("\n")


def grade_answers(quiz_file: TextIO, answer_file: TextIO, questions: dict[str, list[str]]) -> float:
    quiz_file.seek(0)
    correct_answers = 0
    total_questions = 0
    for line in quiz_file:
        line = line.strip()
        if line.startswith("Q"):
            total_questions += 1
            question = line
            correct_answer = questions[question][0]
            student_answer = answer_file.readline().strip()  # Read the next line from answer file
            if student_answer == correct_answer:
                correct_answers += 1

    # Check if there are no questions in the quiz file
    if total_questions == 0:
        return 0.0

    return (correct_answers / total_questions) * 100


def display_results(score: float) -> None:
    print(f"Your score: {score}%")
