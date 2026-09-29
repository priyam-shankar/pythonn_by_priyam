color = input("Enter color:")

match color:
    case "green" :
        print("go")
    case "red" :
        print("stop")
    case "yellow" :
        print("look")
    case _:
        print("wrong color for traffic light")