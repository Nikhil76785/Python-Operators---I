amount = int(input("Enter a number: "))

note_100 = amount//100
note_50 = (amount%100)//50
note_10 = (amount%100%50)//10
note_5 = (amount%100%50%10)//5
note_1 = (amount%100%50%10%5)//1

print("Notes of Rs.100: ", note_100)
print("Notes of Rs.50: ", note_50)
print("Notes of Rs.10: ", note_10)
print("Notes of Rs.5: ", note_5)
print("Notes of Rs.1: ", note_1)