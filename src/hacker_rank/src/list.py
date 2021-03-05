if __name__ == "__main__":
    N = int(float(input()))
    result = []
    commands = []
    for i in range(N):
        command = input()
        commands.append(command)

    for command in commands:
        each_command = command.split(" ")

        if each_command[0] == "insert":
            result.insert(int(each_command[1]), int(each_command[2]))
        if each_command[0] == "append":
            result.append(int(each_command[1]))
        if each_command[0] == "sort":
            result.sort()
        if each_command[0] == "remove":
            result.remove(int(each_command[1]))
        if each_command[0] == "print":
            print(result)
        if each_command[0] == "pop":
            result.pop()
        if each_command[0] == "reverse":
            result.reverse()

    # commands = [
    #     "insert 0 5",
    #     "insert 1 10",
    #     "insert 0 6",
    #     "print",
    #     "remove 6",
    #     "append 9",
    #     "append 1",
    #     "sort",
    #     "print",
    #     "pop",
    #     "reverse",
    #     "print",
    # ]
