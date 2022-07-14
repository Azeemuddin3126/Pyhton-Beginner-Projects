print('>>> Welcome to BMI calculator <<<')

height = float(input("Enter the height in cm: "))  
weight = float(input("Enter the weight in kg: ")) 

BMI = weight / (height/100)**2  

print("Your Body Mass Index is: ",BMI)