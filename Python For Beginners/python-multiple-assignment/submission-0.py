msg1, msg2 = "World", "Hello"
msg3, msg4, msg5 = "Name", "Is", "My"
# Don't change the code above this line
temp = msg1
msg1 = msg2
msg2 = temp
temp = msg3
msg3 = msg5
temp2 = msg5
msg5 = msg4
msg4 = temp

# Don't change the code below this line
print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)
