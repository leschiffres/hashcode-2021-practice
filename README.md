# hashcode
This is a repo containing the code we used for the practice problem of google hashcode 2019.

## Team Members
- Matthaios Letsios [@leschiffres](https://github.com/leschiffres)
- Konstantinos dogeas [@ildoge](https://github.com/ildoge)

## Brief Description

Given a list of pizzas and the number of teams  having k=2,3,4 members in total, deliver exactly k pizzas to each team accordingly, so that the total number of distinct ingredients is maximized.

The score for a single team is the square of the total number of distinct ingredients.

## Execution Command
`python3 run.py`

# Implemented Algorithms

## Random algorithm

1. Create a list of pizzas that will be sent explicitely to a specific type of team.
2. Place each pizza to the lists (uniformly at random).
3. Get a random permutation of for the ids of each pizza.
4. Create sets of pizzas of size k.
5. Keep sets as many as the total teams for each type.

## Greedy Algorithm 
(Maximime distinct random elements iteratively.)

1. Sort the pizzas based on the number of the ingredients they contain.
2. Start building deliveries for teams of size 4. Once they are full, build deliveries for teams with size 3 and then 2.
3. Build deliveries as follows: 
	- Picking the pizza with the largest number of ingredients.
	- Iterates over all available pizzas and find the pizza that adds the maximum number of new ingredients. In ties, (if max number of new ingredients is 5 and we have two pizzas with sizes 20 & 10 then the pizza with smaller number is selected).
	- Once the second pizza is added, it's removed from the available pizzas and the algorithm goes on adding a new pizza until the delivery is completed (i.e. k number of pizzas have been selected for a k member team)

*Note*: Unfortunately when iterating over all pizzas to find the one that maximizes the number of new ingredients, it takes too long to parse all the pizzas. For this reason, an additional parameter was added (`batches` variable in the code), set to 2000, and considers the next 2000 available pizzas to select the one that maximizes the new distinct ingredients.

## File content
- **parser.py**: contains a function named `parse_file(filename)` that parses a file and returns:
	- `total_pizzas`: the number of total pizzas
	- `t2, t3, t4`: the total number of 2,3,4 member teams
	- `pizzas`: a list containing for every pizza a list with the ingredients it contain
- **implementation.py**: contains the implementation of the algorithms. The functions have as parameters the content of the file as given by `parse_file` function.
- **submit.py**: contains two functions.
	- `submission_file(filename, t2_pizzas, t3_pizzas, t4_pizzas)` : given the output filename and the assignment of pizza IDs to the type of teams. It creates / overwrites the output file with the assignments accordingly
	- `calculate_score(pizzas, assignment)`: is an redundant function just for the calculation of the score.
- **run.py**: The file that runs the algorithm in all files.
	1. Reads the input using the function `parse_file` from **parse.py**.
	2. Runs the selected algorithm from **implementation.py**
	3. Outputs the partition of the pizzas using the function `submission_file` from **submit.py**


## Sonstige
An additional file `repeated_random_run.py` was also added that runs repeatedly the random algorithm for a given period of time and outputs the best solution found.