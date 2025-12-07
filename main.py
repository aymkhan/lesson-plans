# Aymen Khan
# Dec 2025

'''
This program returns the lesson plans for ASL 1, 2, and 3.
	1. Download the clean/final versions of the .docx files and store them in /database
		a. /database/lessons
		b. /database/activity
	2. Read the .docx file for the Lessons (might be 3 files for each class - ASL1, 2, and 3
	3. Read the .docx file for Activities (single file) 

DOCX files:
	1. LESSONS
		- Create a Dict to load into pandas DataFrame per course: ASL1, ASL2, and ASL3
		- Dict should have Lesson numbers as KEYS, for ex: "Lesson 1", "Lesson 1.2", "Lesson 2" 
		- Dict should have the vocab words per lesson as VALUES
		- Example Dict:
			ASL1 = {
				"Lesson 1":["hello", "good morning", "good night"],
				"Lesson 1.2":["good evening", "bonjour"],
				"Lesson 2":["food", "water", "lunch", "dinner"]
				}

USER INPUT TO READ THE LESSONS:
	1. Take user input for READING lessons:
		- Maybe allow the user to enter something like: "ASL1 lesson 2" for Lessons and "ASL1 activity 3" for Activities
		- If the user response contains "ASL1", check if the response contains "lesson" 

USER INPUT TO WRITE NEW LESSONS:
	1. Take user input for WRITING new lessons:
		- Ask the user: "Would you like to add a new lesson or activity?" -  user input: lesson/activity
		- "Which course would you like to add a new {lesson/activity} for?" 
			- if ASL1:
				- APPEND to ASL1 Dict
			- so on..
				
'''

# Start the program

import find_lessons

find_lessons.start()














