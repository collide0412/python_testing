message = 'Hello World'

print(len(message))
print(message[-1])
print(message[0:5])
print(message[6:])
print(message.count('o'))
print(message.find('Dang'))
print(message.find('Hello'))
message = message.replace('World', 'Dang')
print(message)

greeting = 'Hello'
name = 'Dang'
message = greeting + ', ' + name + '. Welcome!'
# message = '{}, {}. Welcome!'.format(greeting, name)
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)
