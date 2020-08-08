"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
ClassList=[]
def main():
    data = get_data()
    for i in data:
        print(i)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    ClassList = []
    input_file = open(FILENAME,'r')
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        ClassList.append("{} is taught by {} and has {} students".format(parts[0],parts[1],parts[2]))
        print("----------")
    input_file.close()
    return ClassList


main()