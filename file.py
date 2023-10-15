# .csv
# .txt

# with open('message.txt', 'w') as file:
#     file.write('Hello from Python')
# with open('message.txt', 'a') as file:
#     file.write('Hello from Python')
with open('message.txt', 'r') as file:
    text = file.read()
    print(text)
