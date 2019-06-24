import doctest


def user_input():
    """
    Takes a number of set elements from user.
    Returns the number if it is even integer, else prints caution message and
    asks for a new number.
    F.Ex. :
    -> Please enter an even number: 1.4
       Oops!  That was no a valid number.  Try again...
       Please enter an even number: 2
       2
    """
    while True:
        try:
            n = int(input("Please enter an even number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    return n


def all_pairs_on_set(n):
    """
    (int)->list
    The function takes a number of elements and returns all pairs of elements
    made of these elements.
    >>> all_pairs_on_set(2)
    [(0, 0), (0, 1), (1, 0), (1, 1)]
    """
    all_pairs_list = [(x, y) for x in range(n) for y in range(n)]
    return all_pairs_list


def all_relations(list_of_pairs):
    """
    (list)->set
    The function takes a list of pairs and returns the list of sets of all
    possible relations made of list of pairs.
    >>> all_relations([(0, 0), (0, 1)])
    [frozenset(), frozenset({(0, 0)}), frozenset({(0, 1)}), \
frozenset({(0, 1), (0, 0)})]
    """
    all_relations_list = []
    for i in range(2**len(list_of_pairs)):
        set_of_sets = frozenset(list_of_pairs[j]
                                for j in range(len(list_of_pairs))
                                if (i // 2**j) % 2 == 1)
        all_relations_list.append(set_of_sets)
    return all_relations_list


def is_transitive(relation):
    """
    (list)->boolean/list
    The function takes a relation and returns it if it is transitive and False
    if it is not transitive.
    >>> is_transitive([(0,1),(1,1)])
    [(0, 1), (1, 1)]
    >>> is_transitive([(0,1),(1,0)])
    False
    """
    for a, b in relation:
        for c, d in relation:
            if b == c and ((a, d) not in relation):
                    return False
    return relation


def find_transitive(relations_list):
    """
    (set)->list
    The function takes a list of relations and returns a list of all
    transitive relations made of it.
    >>> print(find_transitive({frozenset(), frozenset({(0, 1), (0, 0)}),\
    frozenset({(0, 1)}), frozenset({(0, 0)})}))
    [frozenset({(0, 1), (0, 0)}), frozenset({(0, 1)}), frozenset({(0, 0)}), []]
    """
    transitive_relations = list(filter(is_transitive, relations_list))
    transitive_relations.append([])
    return transitive_relations


def find_amount(transitive_relations):
    """
    (list)->int
    The function takes a list of relations and returns their amount.
    >>> find_amount([frozenset(), frozenset({(0, 1), (0, 0)}), \
    frozenset({(0, 1)}), frozenset({(0, 0)})])
    4
    """
    return len(transitive_relations)


def write_in_file(n, transitive, amount):
    """
    (int, list, int)->string
    The function takes the amout of elements, list of transitive relations,
    the amount of transitive relations, writes in the txt file and returns a
    string of information about output.
    """
    f = open("relations", "w+")
    line = "-" * 100 + "\n"
    line += "The amount of transitive relations for " + str(n) +\
        " elements is: " + str(amount) + "\n"
    line += "-" * 100 + "\n"
    line += "Here are all transitive relations for " + str(n) + " elements:\n"
    for i in transitive:
        line += (str(set(i)) + "\n") if set(i) != set() else "{}\n"
    f.write(line)
    f.close()
    return line


def main():
    n = user_input()
    transitive = find_transitive(all_relations(all_pairs_on_set(n)))
    amount = find_amount(transitive)
    transitive_relations = [set(x) for x in transitive]
    result = write_in_file(n, transitive_relations, amount)
    print(result)


if __name__ == '__main__':
    main()
    doctest.testmod()
