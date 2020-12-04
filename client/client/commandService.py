def command_checker(user, command):
    if command[:3] == "pwd":
        return False, user.path

    elif command[:5] == "cd ..":
        index = user.path.rfind("/")
        if index < 1:
            index += 1
        user.path = user.path[:index]
        return False, None

    elif command[:4] == "cd /":
        user.path = command[3:]
        return False, None

    elif command[:3] == "cd ":
        if user.path[-1] != "/":
            user.path += "/"
        user.path = user.path+command[3:]
        return False, None

    else:
        return True, None
