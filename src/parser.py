def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
            
        total_pizzas, t2, t3, t4 = [int(w) for w in lines[0].strip().split()]
            
        pizzas = []
        has_duplicate = False
        for line in lines[1:]: 
            pizza = line.strip().split()[1:]
            pizzas.append(pizza)
            
    return total_pizzas, t2, t3, t4, pizzas, has_duplicate
    