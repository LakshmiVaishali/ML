from subprocess import STARTF_USESHOWWINDOW


print("|**************************************  Question 1 Start  **************************************************|")
#Part 1: Sorting List for Min Age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

min1 = ages[0]
for ele in ages:
    if ele<min1:
        min1=ele
print("Minimum age:",min1)

#Sorting List for Max Age
maxages = max(ages)

max1 = ages[0]
for ele in ages:
    if ele>max1:
        max1=ele
print("Maximum age:",max1)

#Adding the min age and the max age again to the list
print("Adding max and min ages to list")
ages.insert(0, 19)
ages.insert(11, 26)
print(ages)

#Finding the median age (one middle item or two middle items divided by two)
print("Median Age is:",(ages[6]-ages[5])/2+ages[5])

#Finding the average age (sum of all items divided by their number)
print("The Average age is",sum(ages)/len(ages))

#Range of the ages (max minus min)
print("Range of ages is",ages[11]-ages[0])

print("====================================== Question 1 End =================================================")
print("|**************************************  Question 2 Start  **************************************************|")

dog = {} #empty Dictionary
print(dog) #print dictionary
#Adding name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Scooby'
dog['color'] = 'white'
dog['breed'] = 'Pitbull'
dog['legs'] = '4'
dog['age'] = '3'
print(dog)

#student dictionary with first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student['first_name'] = 'Tom'
student['last_name'] = 'Holland'
student['gender'] = 'M'
student['age'] = '26'
student['marital_status'] = 'Married'
student['skills'] = ['swinging','Shooting']
student['country'] = 'Uk'
student['city'] = 'London'
student['address'] = 'Lndn'
print(student)

print('Student Dictionary length') #length of the student dictionary
print(len(student))

print("value of skills and the data type, as a list")
print(type(student['skills']))

print("adding skills values by adding skills") #adding skills values by adding one or two skills
student['skills'].append('Crawling')
student['skills'].append('Jumping')
print(student['skills'])

print(student.keys()) #Dictionary keys as a list
print(student.values()) #Dictionary values as a list

print("====================================== Question 2 End =================================================")
print("|**************************************  Question 3 Start  **************************************************|")

brothers = ("Patel", "Rahaj") #tuple with brothers
print("brothers:",brothers)

sisters = ("Priya", "Priti") #tuple with sisters
print("sisters:",sisters)

siblings = brothers + sisters #assigning brothers and sisters tuples to siblings variable
print("siblings:",siblings)

print(len(siblings)) #Counting number of siblings

#adding the name of father and mother and assigning to family_members variable
family_members = siblings + ("Jack", "Perry")
print(" Whole Family names:",family_members)

print("====================================== Question 3 End =================================================")
print("|**************************************  Question 4 Start  **************************************************|")

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("Set length:")
print(len(it_companies)) #Length of the set it_companies

it_companies.add("Twitter") #Adding 'Twitter' to it_companies
print(it_companies)

#Adding multiple IT companies at once to the set it_companies
it_companies.add("Oracle")
it_companies.add("Cisco")
it_companies.add("Tesla")
print(it_companies)

it_companies.remove("IBM") #Removing IBM from the set it_companies
print(it_companies)

C = A | B #Joining A and B
print(C) 

D = A & B #Finding intersection of A and B
print(D)

E = A | B #Joining A with B and B with A
F = B | A
print(E)
print(F)

G = B - A #Symmetric difference between A and B
print(G)

#Deleting the sets completely
A.clear()
B.clear()
print(A)
print(B)

ageset = set(age) #Converting the ages to a set and comparing the length of the list and the set.
print(len(age))
print(len(ageset))

print("====================================== Question 4 End =================================================")
print("|**************************************  Question 5 Start  **************************************************|")

area_of_circle = 3.141592 * 30 * 30 #variable name of area_of_circle_
print("Area =",area_of_circle) #Calculating area of circle

circum_of_circle = 2 * 3.141592 * 30
print("Circumference =",circum_of_circle) # Print Circumference of a circle

rad = float(input("Enter radius: ")) #Taking the radius as user input
print("Area =",3.141592 * rad * rad) #Printing area

print("====================================== Question 5 End =================================================")
print("|**************************************  Question 6 Start  **************************************************|")

#Split methods and set to get the unique words.
sent = "I am a teacher and I love to inspire and teach people"
sent_words = sent.split()
unique = set(sent_words)
print("Unique words are",len(unique))
print("Unique words =",unique)

print("====================================== Question 6 End =================================================")
print("|**************************************  Question 7 Start  **************************************************|")

#String Formatting
print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

print("====================================== Question 7 End =================================================")
print("|**************************************  Question 8 Start  **************************************************|")

radius = 10
area = 3.14 * radius ** 2
print('"The area of a circle with radius {} is {:.0f} meters square."'.format(radius, area))

print("====================================== Question 8 End =================================================")
print("|**************************************  Question 9 Start  **************************************************|")

N = float(input("Please Enter number of students: ")) # Prompt for user input
STARTF_USESHOWWINDOW = 1 #initiate no of students to 1
weights = [] # empty weights list
while STARTF_USESHOWWINDOW <= N:
    studentry = float(input("Enter student "+str(STARTF_USESHOWWINDOW)+"'s weight: "))
    weightconvert = studentry * 0.45359237
    weights.insert(STARTF_USESHOWWINDOW, weightconvert)
    STARTF_USESHOWWINDOW += 1
print("Weights:",weights)

print("====================================== Question 9 End =================================================")
print("|**************************************  Question 10 Start  **************************************************|")

print("Training: 1o, 2o, 3x, 6x\nTesting: 6x, 7o, 10o, 11o")

#Confusion matrix, accuracy, sensitivity and specificity values.
print("TN: 1\tFP: 0\nFN: 0\tTP: 5\nAccuracy: 1\nSensitivity: 1\nSpecificity: 1")

print("====================================== Question 10 End =================================================")