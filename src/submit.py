def submission_file(filename, t2_pizzas, t3_pizzas, t4_pizzas):
    total_pizzas_delivered = len(t2_pizzas) + len(t3_pizzas) + len(t4_pizzas)
    with open(filename, 'w') as f:
        f.write(str(total_pizzas_delivered) + "\n")

        if t2_pizzas:
            for p in t2_pizzas:
                f.write("2 " + " ".join([str(w) for w in p]) + "\n")

        if t3_pizzas:
            for p in t3_pizzas:
                f.write("3 " + " ".join([str(w) for w in p]) + "\n")
        
        if t4_pizzas:
            for p in t4_pizzas:
                f.write("4 " + " ".join([str(w) for w in p]) + "\n")
    f.close()

def calculate_score(pizzas, assignment):

    total_score = 0
    for delivery in assignment:
        content = set()
        for pizza_id in delivery:
            for elmt in pizzas[pizza_id]:
                if elmt not in content:
                    content.add(elmt)
        total_score += len(content) * len(content)
    return total_score
