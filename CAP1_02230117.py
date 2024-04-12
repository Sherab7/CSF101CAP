################################
# Your Name: Ugyen Wangchuk
# Your Section: 1ECE
# Your Student ID Number: 02230117
################################
# REFERENCES
# https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
# https://youtu.be/jM281ESajTs?si=zjNYmQGo6AGAiqMo
# https://youtu.be/1Y9F0yQLM2A?si=fwUeYIjOvGXtBMQU 
################################
# SOLUTION
# Your Solution Score:50169
# Put your number here: 7
################################

# Function to read game results from a file
def read_game_results(file_path):
    # Initialize an empty list to store game results
    game_results = []
    
    with open(file_path, 'r') as input_file:
        for line in input_file:
            figure, outcome = line.strip().split()           
            game_results.append((figure, outcome))
   
    return game_results

# Function to calculate the perfect score based on game results
def calculate_perfect_score(game_results):
   
    perfect_score = 0
    # Iterate through each game result
    for figure, outcome in game_results:
        # Determine the score for each figure-outcome combination and add it to the perfect score
        if figure == "A":
            perfect_score += 3 if outcome == "X" else 4 if outcome == "Y" else 8
        elif figure == "B":
            perfect_score += 1 if outcome == "X" else 5 if outcome == "Y" else 9
        else:
            perfect_score += 2 if outcome == "X" else 6 if outcome == "Y" else 7
   
    return perfect_score

file_path = 'input_7_cap1.txt'          # Provide the actual file path
game_results = read_game_results(file_path)
perfect_score = calculate_perfect_score(game_results)  # Calculate perfect score based on game results
print("Final Score:", perfect_score)  # Print the final perfect score