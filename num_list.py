num_list= input("Enter a list of integers separated by spaces:").split()
num_list= [int(num) for num in num_list]
Total_sum= sum(num_list)
print(Total_sum)