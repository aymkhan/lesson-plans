# Aymen Khan
# Dec 2025

# This program will find the Lessons and Activities for ASL1, ASL2, and ASL3 courses

import os
import csv
import pandas as pd
#from docx import Document

def start():
	print("Hello, Gianna!")

ASL1_LESSON_KEYS = []
ASL1_LESSON_VALUES = {}
ASL1_LESSONS = {}

ASL1_file = os.getcwd() + "/database/lessons/ASL1_Lessons.csv"

# Open the CSV file and load it into pandas by calling the read_csv() method
with open(ASL1_file,'r') as asl1:
	data = pd.read_csv(asl1) # read_csv() method is needed for pandas to READ the csv
				 # print this method's value without using to_string() will only print the first few rows and last few rows
#	print(data.to_string())
#	print(data)
	data.columns = data.columns.str.lower() # just to be cautious of case sensitive text, I've changed all column names to lowercase 
#	print(data.head(10))

def get_user_prompt():
	prompt = input("📣 How can I help you?\n")
	return prompt

# Take user input 
prompt = get_user_prompt().lower()

lesson = "lesson"
activity = "activity"
ASL1 = "asl1"
ASL2 = "asl2"
ASL3 = "asl3"


if lesson in prompt:
	if ASL1 in prompt:
		# split the prompt str and only keep the part from 'lesson' onwards
		# send this part of the string to the DataFrame obj: data[str] to receive all the rows associated with this column
		find_lesson = prompt.split(ASL1 + " ")
		lesson = find_lesson[-1]
		print("Here are the Vocab words for", ASL1.upper() + " " + lesson.capitalize() + ":\n" )
		for row in data[lesson]:
			if pd.notna(row):
				print(row)
			else:
				pass
		print("\n")
	elif ASL2 in prompt:
		# find ASL2 Lesson
		print("Hello this is ASL2")
	else:
		print("I can help you find Lessons or Activities for ASL1, ASL2, or ASL3")
		get_user_prompt()
		 


#	for column in data:
#		if "Lesson 2" in column:
#			print(column)
#			print(columna


'''
Lines below are responsible for working with DOCX files

# Set the paths for LESSON .docx files
ASL1_docx = os.getcwd() + "/database/lessons/ASL1_lessons.docx"
print(f"os.path: ", ASL1_docx) 

# Open the .docx file to read
ASL1 = Document(ASL1_docx)
p = ASL1.paragraphs

lesson = "Lesson"
counter = 0

for table in ASL1.tables:
	for row in table.rows:
		for cell in row.cells:
			if lesson in cell.text:
				counter +=1
				lesson = "Lesson " + str(counter)
				print("Found lesson ", counter)
				ASL1_LESSON_KEYS.append(lesson)


for line in p:
	print(line.text) #prints each line
	if lesson in line.text:
		counter +=1
		lesson = "Lesson " + str(counter)
		print("Found lesson ", counter)
		ASL1_LESSON_KEYS.append(lesson)


print(f"Lesson keys: ", ASL1_LESSON_KEYS)
'''
		

