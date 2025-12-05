def split_before_uppercases(formula):
    if not formula:
        return []
    start = 0
    split_formula = []
    for i in range(1, len(formula)):
        if formula[i].isupper():
            split_formula.append(formula[start:i])
            start = i
    split_formula.append(formula[start:])
    return split_formula

def split_at_digit(formula):
    digit_location = -1

    for i in range(len(formula)):
        if formula[i].isdigit():
            digit_location = i
            break
    if digit_location == -1:
        return formula, 1

    prefix = formula[:digit_location]

    j = digit_location
    while j < len(formula) and formula[j].isdigit():
        j += 1

    num = int(formula[digit_location:j])

    return prefix, num

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""
    split_formula = split_before_uppercases(molecular_formula)
    atom_counts = {}
    for atom_str in split_formula:
        prefix, num = split_at_digit(atom_str)
        # If the atom already exists in the dictionary, add to its count
        if prefix in atom_counts:
            atom_counts[prefix] += num
        else:
            # Otherwise, add the atom with its count
            atom_counts[prefix] = num
    return atom_counts


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
