print('Welcom to the tip calculator')
bill = float(input('what was the total bills?\n$'))
tip = float(input("what percentage tip would you like to give? 10, 12, 15\n"))
pepole = int(input("How many pepole to split the bill?\n"))

# calculation the total with tip and split it 
total_bill = round(bill * (1 + (tip / 100)), 2)
bill_per_person = round(total_bill / pepole, 2)

print(f'The total number is {total_bill}, Each person should pay ${bill_per_person}')