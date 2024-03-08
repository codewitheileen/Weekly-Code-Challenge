Odd_numbers= input("Enter odd numbers from 0 to 10 separated by spaces:")
Odd_numbers_list= Odd_numbers.split()
int_numbers_list1= set (int(num) for num in Odd_numbers_list)

print("Odd numbers entered:", int_numbers_list1)

Prime_numbers= input("Enter prime numbers from 0 to 10 separated by spaces:")
Prime_numbers_list= Prime_numbers.split()
int_numbers_list2= set (int(num) for num in Prime_numbers_list)

print("Prime number entered:", int_numbers_list2)

intersection_set= int_numbers_list1.intersection(int_numbers_list2)
print('Intersection using intersection():', intersection_set)

