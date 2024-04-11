################################
# Your Name
# Your Section
# Your Student ID Number
################################
# REFERENCES
# Links that you referred while solving
# the problem
# http://link.to.an.article/video.com
################################
# SOLUTION
# Your Solution Score:
# Put your number here
################################

#Defining the function to read the file
def read_content(file_path):
    content = []
    file = open(file_path, 'r')
    content = file.readlines()
    file.close()
    return content

#Defining the function to claculate the points
def calculate_points(lines):
    total = 0
#Determining the points
    shape_points = {'A': 1, 'B': 2, 'C': 3}
    outcome_points = {'X': 0, 'Y': 3, 'Z': 6}
    
#Reiterating every lines in the list
    for line in lines:
        line = line.strip()
        if line:
            parts = line.split()
            if len(parts) == 2:
                shape, outcome = parts
                if shape in shape_points and outcome in outcome_points:
                    total += shape_points[shape] + outcome_points[outcome]
                else:
                    print(f"Error: Invalid character in line '{line}'")
            else:
                print(f"Error: Invalid format in line '{line}'")
    
    return total

#specifying the file path
file_path = 'input_7_cap1.txt'
lines = read_content(file_path)
if lines:
    total = calculate_points(lines)
    print(f"The total score is {total}")
else:
    print("No content to process.")