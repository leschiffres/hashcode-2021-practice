from parser import parse_file
from submit import submission_file, calculate_score
from implementation import random_algorithm
from time import time

input_folder_path = "./input/"
output_folder_path = "./output/"

filenames = [
"b_little_bit_of_everything.in",
"c_many_ingredients.in",
"d_many_pizzas.in",
"e_many_teams.in"
]

data = {}
scores = {}
# read input
time_given = 60 # in seconds
for filename in filenames:
    now = time()
    total_pizzas, t2, t3, t4, pizzas, has_duplicate = parse_file(input_folder_path + filename)
    data[filename] = (total_pizzas, t2, t3, t4, pizzas, has_duplicate)
    scores[filename] = 0
    total_time = round(time() - now, 2)
    print(f"Time to read file {filename}: {total_time} seconds")
    
# run algorithm
total_time = 0
start = time()
iterations = 0
while total_time < time_given:
    iterations += 1
    now = time()
    for filename in filenames:
        total_pizzas, t2, t3, t4, pizzas, has_duplicate = data[filename]
        t2_pizzas, t3_pizzas, t4_pizzas = random_algorithm(total_pizzas, t2, t3, t4, pizzas)

        score = calculate_score(pizzas, t2_pizzas) + calculate_score(pizzas, t3_pizzas) + calculate_score(pizzas, t4_pizzas)
        if score > scores[filename]:
            print(f"Found new highscore for file {filename}: {score}")
            scores[filename] = score
            # produce output files
            output_filename = output_folder_path + filename[:-3] + ".out"
            submission_file(output_filename, t2_pizzas, t3_pizzas, t4_pizzas)
    end = round(time() - now, 2)
    total_time += end
    print(f"Iteration: {iterations}, Total Time: {end}")

print("-"*50)
print("Final highscores")
print("-"*50)
for filename in filenames:
    print(f"File: {filename} Highscore: {scores[filename]}")

total_time = round(time() - start, 2)
print(f"Total iterations: {iterations}")
print(f"Total execution time of algorithm: {total_time} seconds")
