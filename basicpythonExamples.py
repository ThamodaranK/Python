'''
Examples for 
Functions
Allow the use of the line continuation character (\)
Adition of two numbers
''' 
'Program - 1'
'''
	Return addition of three numbers and concadination of string
'''
def adition(numOne, numTwo):
	numthree = 3;
	total = numOne + \
	        numTwo + \
	        numthree
	return 'Addition of three numbers Output : ' + str(total);

# Function for concad tow strings
def stringConcad(str1, str2):
	return str1+str2;

# Function for read letter in words
def readLeters(word):
	for letter in word:		
		print(letter);

def displayMonths(mounthList, conditionsForCalling):
	total = [];
	for condition in conditionsForCalling:
		if(condition == 1):
			week = displayWeek();			# Function calling
		elif(condition == 2):
			weekDays = displayWeekDays();   # Function calling
		elif(condition == 3):
			total.append(mounthList);       # Array append(push)
			total.append(weekDays);         # Array append(push)
			total.append(week);             # Array append(push)			
	return total;

def displayWeek():
	weeks = ['Week 1',
				'Week 2',
				'Week 3',
				'Week 4']	
	return weeks;

def displayWeekDays():
	weekDays = ['Sunday',
				'Monday',
				'Tuesday',
				'Wednesday',
				'Thursday',
				'Friday',
				'Saturday']
	return weekDays;

print(adition(numOne=2,numTwo=3));
print(stringConcad(str1='Thamu ',str2='is a Software Engineer'));
readLeters("Hi This IS THAMODARN K");

months = {"month 1":"Jan",    # Example for dictionaries (associative arrays is called as dictionaries)
			"month 2":"Feb",
			"month 3":"Mar",
			"month 4":"Apr",
			"month 5":"May",
			"month 6":"Jun",
			"month 7":"July",
			"month 8":"Aug",
			"month 9":"Sep",
			"month 10":"Oct",
			"month 11":"Nov",
			"month 12":"Dec"};
conditionsForCalling = [1,2,3];
res = displayMonths(months, conditionsForCalling);
print(res);