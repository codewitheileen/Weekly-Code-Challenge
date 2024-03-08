words = ['shoes', 'papers', 'apple', 'chair', 'book', 'wall']
odd_length_words= [word for word in words if len(word) % 2 !=0]
print("Words with odd number of characters:")
print(odd_length_words)