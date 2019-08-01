import ast

"""
modes: exec, eval, single
"""
expression = '5 + 9 + 2'
code = ast.parse(expression, mode='eval')
code_body = code.body
print(ast.dump(code))
print(code_body)
print(code_body.right.n)
print(code_body.left.left.n)
print(code_body.left.right.n)
print(code_body.op)
print(eval(compile(code, '', mode='eval')))
