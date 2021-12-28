import random
from time import time

def random_algorithm(total_pizzas, t2, t3, t4, pizzas):
    # random.seed()
    groups = {2:[], 3:[], 4:[]}
    for i in range(len(pizzas)):
        dice = random.randint(2,4)
        groups[dice].append(i)

    # print(f"Group of 4-member teams: {len(groups[4])}")
    # print(f"Group of 3-member teams: {len(groups[3])}")
    # print(f"Group of 2-member teams: {len(groups[2])}")

    # now we have split pizzas into the 3 groups and we need to assign them into teams
    # To do that we need to partition each group into sets of k pizzas.
    random.shuffle(groups[2])
    random.shuffle(groups[3])
    random.shuffle(groups[4])
    def partition_pizzas(group, k, total_teams):
        # suffle the pizzas in this group randomly
        random.shuffle(group)
        # create sets of size k
        partition = [group[i:i+k] for i in range(0,len(group),k)]
        # check if the last set has exactly k elements (it might have less)
        if len(partition[-1]) < k:
            partition.pop()
        # this command is also doing the same because it checks if all sets have cardinality k, 
        # but does unnecessary computation
        # partition = [p for p in partition if len(p)==k]
        
        # the number of all sets  should be less or equal to the number of total teams
        partition = partition[:total_teams]
        return partition

    t2_pizzas = partition_pizzas(groups[2], 2, t2)
    t3_pizzas = partition_pizzas(groups[3], 3, t3)
    t4_pizzas = partition_pizzas(groups[4], 4, t4)
    return t2_pizzas, t3_pizzas, t4_pizzas


# the algorithm goes as follows:
# sorts the pizzas based on the number of the ingredients they contain.
# then starts building deliveries for teams of size 4. Once they are full,
# goes to build deliveries for teams with size 3 and then 2.

# it builds deliveries by picking the pizza with the largest number of ingredients.
# Then iterates over all available pizzas and finds the pizza that adds the maximum number of 
# ingredients. In ties, (if max number of new ingredients is 5 and we have two pizzas with sizes 20 & 10
# then the pizza with smaller number is selected).
# Once the second pizza is added it's removed from the available pizzas and the algorithm goes on adding a new pizza
# adding the max number of ingredients until the delivery is completed. i.e. we have pizzas for each member of the team,
# or in other words, the size of the delivery is equal to the size of the team.
def maximize_number_of_elements(total_pizzas, t2, t3, t4, pizzas):
    total_deliveries = 0
    # all the deliveries for the teams of size 2,3,4, each key of the dictionary points to a list of lists
    groups = {2:[], 3:[], 4:[]} 
    # just a helper dictionary to reduce code size in the algorithm
    team_sizes = {2:t2, 3:t3, 4:t4} 

    # we build a new list where every pizza will be stored as a tuple of three elements: 
    # 1. a set with the ingredients so that operations between sets is maximized.
    # 2. the index of the pizza in the initial array so that we can form deliveries with the right pizza id
    # 3. the size of the pizza so that we can sort them by the number of ingredients.
    available_pizzas = []
    for i in range(len(pizzas)):
        p = pizzas[i]
        available_pizzas.append((set(p), i, len(p)))

    # sort pizzas based on number of ingredients
    available_pizzas.sort(key=lambda tup: tup[2], reverse=True)

    # print(available_pizzas)
    # since algorithm is pretty slow when considering all pizzas
    batches = 2000

    # we start by building teams of size equal to 4. When we run out of teams of size equal to 4, we will go to 3 and then 2.
    i = 0 
    team_size = 4
    start_time = time()
    while team_size > 1 and len(available_pizzas) >= team_size:
        total_deliveries += 1
        if total_deliveries % 200 == 0:
            total_time = round(time() - start_time, 2)
            start_time = time()

            print(f"Total time to make 200 deliveries: {total_time} sec")
        # get the largest pizza in the current list
        ingredients, index, total_ingredients = available_pizzas.pop(0)
        delivery = [index]
        # keep a separate set including all the ingredients of the current delivery.
        delivery_ingr = set([ i for i in ingredients]) # should we copy the set?

        # while we have not added pizzas equal to the size of the team
        while len(delivery) < team_size:
            # find pizza maximizing total new ingredients in the delivery
            max_new_ingredients = set()
            selected_pizza_index = -1
            # go over all pizzas and find how many new elements they add
            # for i in range(len(available_pizzas)):
            for i in range(min(batches, len(available_pizzas))):
                ingredients, index, total_ingredients = available_pizzas[i]

                # ingredients & delivery_ingr are both sets so the following minues operator will keep the elements of the left
                # side that are not on the right_side (it will still remain a set)
                new_ingredients = ingredients - delivery_ingr
                if len(new_ingredients) >= len(max_new_ingredients):
                    max_new_ingredients = new_ingredients
                    selected_pizza_index = i

            # remove pizza from the list
            ingredients, index, total_ingredients = available_pizzas.pop(selected_pizza_index)
            delivery.append(index)
            delivery_ingr.update(max_new_ingredients)

        # add the delivery in the dictionary with all the deliveries for teams of size equal to 4
        groups[team_size].append(delivery)

        if len(groups[team_size]) == team_sizes[team_size]:
            team_size -= 1
            
    return groups[2], groups[3], groups[4]
