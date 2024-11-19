# Your Name Here : Rikart Yeimo
# UWYO COSC 1010
# Submission Date :10/15/2024 
# Homework 1 
# Lab Section-5
# Sources, people worked with, help given to: 
# your
# comments
# here
# You are given a list of dictionaries where each dictionary represents a student and their scores 
# in different subjects.
# 
# Student Data:
mors_abjad_dictionary = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}

def plaintext_to_mors(plaintext):
    plaintext = plaintext.upper()
    mors_code = " "
   
    for abjad in plaintext:
        if abjad.isalpha():
            mors_code += mors_abjad_dictionary[abjad] 
        elif abjad:
            mors_code += "  "
    return mors_code.strip()
Input = input("Please, write word/sentence:")
output_mors = plaintext_to_mors(Input)
print("Abjad Result:", output_mors)

#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.

# Your task is to calculate the average scores for each student and print the names of students
# whose average score is greater than 80.

#Solution