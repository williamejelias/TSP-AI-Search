cityFileName = ''
numberOfCities = 0


# get name of file and number of cities and save to variables in the file
def get_name_and_city_number():
    global cityFileName
    global numberOfCities
    count = 0
    recent_string = ''
    while count <= 1:
        while True:
            character = file.read(1)
            if character == ',' or character == '':
                break
            else:
                recent_string += character
        if count == 0:
            recent_string = "".join([s for s in recent_string.strip().splitlines(True) if s.strip()])
            cityFileName = recent_string
        elif count == 1:
            recent_string = ''.join(_ for _ in recent_string if _ in ".1234567890")
            numberOfCities = int(recent_string)
        count += 1
        recent_string = ''


# read to the next comma unless at end of file, in which case pass
def read_next_value():
    recent_string = ''
    while True:
        character = file.read(1)
        if character == ',' or character == '':
            break
        else:
            recent_string += character
    string = ''.join(_ for _ in recent_string if _ in ".1234567890")
    value = int(string)
    return value


# create nxn matrix where n is number of cities
def populate_matrix():
    matrix = [[0 for _ in range(numberOfCities)] for _ in range(numberOfCities)]

    # starting in row 0 col 1, fill in each int and mirror, creating a symmetric matrix
    count = 1
    for rows in range(numberOfCities):
        for entry in range(count, numberOfCities):
            matrix[rows][entry] = read_next_value()
            matrix[entry][rows] = matrix[rows][entry]
        count += 1
    '''for i in range(numberOfCities):
        print(matrix[i])'''
    return matrix


def initialise(filepath):
    global file
    file = open(filepath)
    get_name_and_city_number()
    matrix = populate_matrix()
    return_list = [cityFileName, numberOfCities, matrix]
    file.close()
    return return_list
