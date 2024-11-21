**Exam Question Generator and Grading**
===========================

An automated system for generating customized quizzes and grading answers. This project is ideal for educators who want to create unique quizzes for multiple students and automate the grading process. It leverages Python's file handling and randomization to create tailored question sets and evaluate student responses efficiently.

**Features**
------------

*   **Quiz Generation**:
    
    *   Dynamically creates shuffled quizzes for each student.
        
    *   Supports multiple-choice questions with randomized options.
        
    *   Generates separate question files for students.
        
*   **Answer Grading**:
    
    *   Grades student answers automatically.
        
    *   Provides detailed feedback, including scores and incorrect answers.
        
    *   Supports multiple students with individual answer files.
        
*   **Modular Design**:
    
    *   Cleanly separated functionality for quiz generation and grading.
        
    *   Easy to extend with new question sets or formats.
        

**Project Structure**
---------------------
```sh
exam_question_generator_and_grading/ 
├── questions/  # Generated question files
├── answers/    # Answer files for students
├── src/
│ ├── data.py   # Contains the question set
│ ├── quiz.py   # Core logic for generating quizzes and grading
│ ├── generate_questions_main.py    # Script to generate quizzes
│ ├── grade_answers_main.py     # Script to grade answers
├── README.md   # Project documentation
```
**Getting Started**
-------------------

### **Prerequisites**

*   Python 3.7 or higher installed on your system.
    
*   A terminal or command prompt for running the scripts.
    

### **Setup**

1.  git clone https://github.com/your-username/exam_question_generator_and_grading.git
    cd exam_question_generator_and_grading
    
2.  **Ensure the required folder structure**:
    
    *   Ensure **questions** and **answers** directories exist in the project root.
        
    *   If they are missing, the scripts will create them automatically.
        
3.  **Install dependencies (if any)**:
    
    *   Currently, this project uses only Python standard libraries.
        

### **Usage**

#### **1\. Generate Quizzes**

Use the **generate_questions_main.py** script to generate quizzes for multiple students:
```sh
python3 -m src.generate_questions_main
```

*   Enter the number of students when prompted.
    
*   The script will generate quiz files in the **questions** folder and corresponding empty answer files in the **answers** folder.
    

#### **2\. Fill in the Answer Files**

Manually open the files in the **answers** folder (e.g., 'python_quiz_answer1.txt') and provide the answers for each student.

#### **3\. Grade Answers**

Run the **grade_answers_main.py** script to grade the answers:
```sh
python3 -m src.grade_answers_main
```

*   Enter the number of students when prompted.
    
*   The script will read the quizzes and answers, calculate scores, and display detailed feedback.
    

### **Example**

1.  **Generate Questions**:
    
    *   Enter the number of students: 2
        
    *   Generated quiz for Student 1 at **questions/python_quiz_question1.txt**
    Generated quiz for Student 2 at **questions/python_quiz_question2.txt**
        
2.  **Grade Answers**:
    
    *   Enter the number of students: 2
        
    *   Results for Student 1:Score: 80%
    Review your incorrect answers:Q: What does 'self' represent in OOP?Correct Answer: The object
    Results for Student 2:Score: 100%
        

**Extending the Project**
-------------------------

### Add More Questions

*   Open src/data.py.
    
 ```python 
"Q:Your Question?": 
"Correct Answer", # Always list the correct answer first 
"Wrong Answer 1", 
"Wrong Answer 2", 
"Wrong Answer 3"
```
    

### Customize Functionality

*   Modify **src/quiz.py** to change the randomization logic or grading rules.
    
*   Adjust **src/generate_questions_main.py** or **src/grade_answers_main.py** for specific workflows.
    

**Contributing**
----------------

Contributions are welcome! Feel free to open issues or submit pull requests for:

*   Bug fixes.
    
*   Additional features.
    
*   Enhancements to documentation.
    


**Acknowledgments**
-------------------

*   Thanks to Python for its powerful standard library.
    
*   Special thanks to educators who inspire projects like this!
    
