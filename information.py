Person_info= {}
Person_info['name']= input("Enter your name: ")
Person_info['Age']= input("Enter your age: ")
Person_info['Favorite_color']= input("Enter your favorite color: ")
print("Person_info:")
for key, value in Person_info.items():
        print(f"{key.capitalize()}: {value}")