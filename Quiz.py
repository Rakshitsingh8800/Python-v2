# python quiz

score = 0

print("Welcome to the AI quiz\n")

# Question 1
print("What is the full form of AI?")
print("a. Automated Intelligence")
print("b. Artificial Intelligence")
print("c. Analytical Imposter")
print("d. Advanced Information")

answer = input("Your answer: ")
if answer.lower() == "b":
    score+=1

# Question 2
print("\n Which of these is an example of AI?")
print("a. Washing Machine")
print("b. Calculator")
print("c. Alexa")
print("d. Comb")

answer = input("Your answer: ")
if answer.lower() == "c":
    score+=1

# Question 3
print("\n Which of the following best defines Artificial Intelligence?")
print("a. . A system that stores large amounts of data")
print("b. A machine capable of performing tasks that require human intelligence")
print("c. A programming language")
print("d. A computer hardware component")

answer = input("Your answer: ")
if answer.lower() == "b":
    score+=1

# Question 4
print("\n Which area is most closely related to Artificial Intelligence?")
print("a. Database Management")
print("b. Computer Networking")
print("c. Machine Learning")
print("d. Web Hosting")

answer = input("Your answer: ")
if answer.lower() == "c":
    score+=1

# Question 5
print("\n Which programming language is commonly used in Artificial Intelligence development?")
print("a. HTML")
print("b. Python")
print("c. CSS")
print("d. SQL")

answer = input("Your answer: ")
if answer.lower() == "b":
    score+=1

print("\n Quiz completed")
print("Your Score", score,"/5")

if score == 5:
    print("Excellent🎉")
elif score >=3:
    print("Good Work👏")
else:
    print("Keep Practising😊")