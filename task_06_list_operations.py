# Consider a list (list = []). You can perform the following commands:
# 1. insert i e: Insert integer  at position .
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer .
# 4. append e: Insert integer  at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines
# of commands where each command will be of the 7 types listed above.
# Iterate through each command in order and perform
# the corresponding operation on your list.

# Input Format
# The first line contains an integer, n, denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.

# Constraints
# The elements added to the list must be integers.

# Output Format
# For each command of type print, print the list on a new line.


# Sample input:
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print


# Sample Output:
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]



commands_num = int(input())
commands_list = []
my_list = []

for _ in range(commands_num):
    current_command = input().split()
    commands_list.append(current_command)

for command_line in commands_list:
    command = command_line[0]

    if command_line[0] == "insert":
        i = int(command_line[1])
        e = int(command_line[2])
        my_list.insert(i, e)

    elif command_line[0] == "print":
        print(my_list)

    elif command_line[0] == "remove":
        element_to_remove = int(command_line[1])
        my_list.remove(element_to_remove)

    elif command_line[0] == "append":
        element_to_append = int(command_line[1])
        my_list.append(element_to_append)

    elif command_line[0] == "sort":
        my_list.sort()

    elif command_line[0] == "pop":
        my_list.pop()

    elif command_line[0] == "reverse":
        my_list.reverse()

