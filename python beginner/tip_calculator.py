print('#'*25)
print('Welcome to tip calculator')
print('#'*25)
#Taking inputs 
bill = float(input('What was the total bill?: '))
tip = int(input('How much tip would you like to give?: '))
people = int(input('how many people would  split the bill?: '))
#calculation
tip_percentage = tip/100
total_tip_bill = bill*tip_percentage
total_bill = bill+total_tip_bill
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)
#Execution
print('Each person should: ',bill_per_person)