import ast

file_name = ""
file_obj = open(file_name)
expression = ast.parse(file_obj.read())
