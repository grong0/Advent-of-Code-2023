def toNumeric(string: str) -> int:
    newString = ""
    for char in string:
        if (char.isnumeric()):
            newString += char
    return int(newString)

with open("./day2.txt") as f:
    colors = ["red", "green", "blue"]
    limits = [12, 13, 14]
    sum = 0
    
    for line in f:
        game_num = line.split(":")[0].split(" ")[1]
        content = line.split(":")[1]
        rounds = content.split(";")
        
        failed = False;
        for round in rounds:
            round = round.replace(" ", "")
            round = round.replace("\n", "")
            marbles = round.split(",")
            
            red = 0
            green = 0
            blue = 0
            for marble in marbles:
                if marble.find("red") != -1:
                    red = toNumeric(marble)
                elif marble.find("green") != -1:
                    green = toNumeric(marble)
                elif marble.find("blue") != -1:
                    blue = toNumeric(marble)
            
            if red > limits[0]:
                failed = True;
                break;
            elif green > limits[1]:
                failed = True;
                break;
            elif blue > limits[2]:
                failed = True;
                break;

        if not failed:
            print("didnt fail " + str(game_num))
            sum += int(game_num)
        
    print(sum)

with open("./day2.txt") as f:
    colors = ["red", "green", "blue"]
    limits = [12, 13, 14]
    power = 0
    
    for line in f:
        game_num = line.split(":")[0].split(" ")[1]
        content = line.split(":")[1]
        rounds = content.split(";")
        
        max_red = 0
        max_green = 0
        max_blue = 0
        failed = False;
        for round in rounds:
            round = round.replace(" ", "")
            round = round.replace("\n", "")
            marbles = round.split(",")
            
            
            for marble in marbles:
                if marble.find("red") != -1:
                    red = toNumeric(marble)
                    if red > max_red:
                        max_red = red
                    
                elif marble.find("green") != -1:
                    green = toNumeric(marble)
                    if green > max_green:
                        max_green = green
                    
                elif marble.find("blue") != -1:
                    blue = toNumeric(marble)
                    if blue > max_blue:
                        max_blue = blue

        power += (int(max_red) * int(max_green) * int(max_blue))
        
    print("power: " + str(power))
