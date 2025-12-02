
with open("data.txt", "r") as file:
    current_position = 50
    numberOfZeros = 0
    for line in file:
        cleanValue = line.strip()
        direction = cleanValue[0]
        distance = int(cleanValue[1:])
        if(direction == 'L'):
            new_position = (current_position-distance) % 100
            if(new_position > current_position and current_position != 0):
                numberOfZeros += 1
        elif(direction == 'R'):
            new_position = (current_position+distance) % 100
            if(new_position < current_position and new_position != 0):
                numberOfZeros += 1
        else:
            raise ValueError("Invalid direction character. Must be 'L' or 'R'.")
        
        
        current_position = new_position
        #land directly on zero
        #if(current_position == 0):
        #
        #cross over a zero
        if current_position == 0:
            numberOfZeros += 1
        number_of_rotations = distance // 100
        numberOfZeros += number_of_rotations

        print(f"Direction: {direction}, Distance: {distance}")
        print(f"Current Position: {current_position}")
        print(f"Number of times position was zero: {numberOfZeros}")

    print(f"Number of times position was zero: {numberOfZeros}")