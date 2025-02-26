#Code goes here

secret_message_dict = {}

# importing data to manipulate
with open('c:/Users/gum12/Documents/CS/homeworkfolder-Gizmofire/Homework/Homework 04/SecretMessage.txt', 'r') as file:
    for line in file:
        number, word = line.strip().split()
        secret_message_dict[int(number)] = word

# Print the dictionary to verify

# sorts by numerical key
secret_message_dict = dict(sorted(secret_message_dict.items()))


row = 1
count = 0


for x in secret_message_dict:


    print(secret_message_dict[x], end=" ")
    count += 1
    

    if count == row:
        count = 0
        print("\n")    
        row += 1
        # print("index row ++")   
   




# print(secret_message_dict)