from parser import parse_file
from submit import submission_file, calculate_score
from implementation import random_algorithm, maximize_number_of_elements
from time import time

start = time()

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

for filename in filenames:
    now = time()
    total_pizzas, t2, t3, t4, pizzas, has_duplicate = parse_file(input_folder_path + filename)
    data[filename] = (total_pizzas, t2, t3, t4, pizzas, has_duplicate)
    scores[filename] = 0
    total_time = round(time() - now, 2)
    print(f"Time to read file {filename}: {total_time} seconds")


for filename in filenames:
    print("-"*50)
    print(f"File: {filename}")
    print("-"*50)
    total_pizzas, t2, t3, t4, pizzas, has_duplicate = data[filename]
    print(f"Instance:\nTotal Pizzas: {total_pizzas}\nt2, t3, t4: {t2, t3, t4}\n")
    
    # t2_pizzas, t3_pizzas, t4_pizzas = random_algorithm(total_pizzas, t2, t3, t4, pizzas)
    t2_pizzas, t3_pizzas, t4_pizzas = maximize_number_of_elements(total_pizzas, t2, t3, t4, pizzas)
    
    score = calculate_score(pizzas, t2_pizzas) + calculate_score(pizzas, t3_pizzas) + calculate_score(pizzas, t4_pizzas)
    print(f"Scoring for file {filename}: {score}")
    scores[filename] = score
    # produce output files
    output_filename = output_folder_path + filename[:-3] + ".out"
    submission_file(output_filename, t2_pizzas, t3_pizzas, t4_pizzas)

print("-"*50)
print("Final scores")
print("-"*50)
for filename in filenames:
    print(f"File: {filename} Highscore: {scores[filename]}")

total_time = round(time() - start, 2)
print(f"Total execution time: {total_time} seconds")