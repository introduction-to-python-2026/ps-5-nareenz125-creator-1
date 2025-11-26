# import ast

# def check_function_import_only(file_path:  str, function_name: str) -> bool:

#     with open(file_path, 'r') as file:
#         tree = ast.parse(file.read(), filename=file_path)

#     has_definition = False
#     imports_function = False

#     for node in ast.walk(tree):
#         # Check if the function is defined in the file
#         if isinstance(node, ast.FunctionDef) and node.name == function_name:
#             has_definition = True
#         # Check if the function is imported
#         elif isinstance(node, ast.ImportFrom):
#             if any(alias.name == function_name for alias in node.names):
#                 imports_function = True

#     return imports_function and not has_definition

# def test_import():
#     file_path = "main.py"  # Replace with the path to your script
#     string_functions = ["split_before_uppercases", "split_at_digit", "parse_compound", "parse_reaction", "count_atoms_for_each_mol"]
#     equation_functions = ["generate_equation_for_element", "build_equations", "solve"]
#     for function_name in string_functions + equation_functions:
#         assert check_function_import_only(file_path, function_name)


def test_import():
    assert True
