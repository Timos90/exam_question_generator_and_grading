# src/quiz.py
import os
import random
from typing import TextIO
from src.data import python_oop

def create_file(file_path: str, student_num: int, mode: str = "w") -> TextIO:
    """Create or open a file for the quiz or answers."""
    # Construct the full path for the file
    full_path = f"{file_path}{student_num}.txt"  # Append the student number and .txt extension
    return open(full_path, mode)  # Open the file in the specified mode




def write_header(file: TextIO, title: str, student_num: int) -> None:
    """Write the header for the quiz file."""
    file.write("Name:\n\nDate:\n\n")
    file.write(f"\t\t{title} (Paper {student_num})\n\n")

def generate_quiz(file: TextIO, questions: dict[str, list[str]], fixed_questions: list[str]) -> None:
    """Generate quiz questions and write them to the file."""
    random.shuffle(fixed_questions)
    for question in fixed_questions:
        options = questions[question]
        file.write(f"\n\n{question}\n")
        shuffled_options = random.sample(options, len(options))
        for option_index, option in enumerate(shuffled_options, start=97):  # ASCII 'a'
            option_letter = chr(option_index)
            file.write(f"{option_letter}. {option}\n")

def grade_answers(quiz_file: TextIO, answer_file: TextIO, questions: dict[str, list[str]]) -> tuple[float, list[tuple[str, str]]]:
    """Grade the answers provided by the student."""
    quiz_file.seek(0)
    correct_answers = 0
    total_questions = 0
    incorrect_questions = []

    for line in quiz_file:
        line = line.strip()
        if line.startswith("Q:"):
            total_questions += 1
            question = line
            correct_answer = questions.get(question, [None])[0]
            if correct_answer is None:
                print(f"Error: Question '{question}' not found in data.")
                continue

            student_answer = answer_file.readline().strip()
            if student_answer.lower().strip() == correct_answer.lower().strip():
                correct_answers += 1
            else:
                incorrect_questions.append((question, correct_answer))

    if total_questions == 0:
        return 0.0, incorrect_questions
    return (correct_answers / total_questions) * 100, incorrect_questions


def display_results(score: float) -> None:
    """Display the student's results."""
    print(f"Your score: {score}%")
