import ast

"""
modes: exec, eval, single
"""


def expression_nodes(expression):
    for node in ast.walk(expression):
        yield node

sum_str = '5 + 9 + 2'
expression = ast.parse(sum_str, mode='eval')
expression_body = expression.body
#print(ast.dump(expression))
#print(expression_body)
#print(expression_body.right.n)
#print(expression_body.left.left.n)
#print(expression_body.left.right.n)
#print(expression_body.op)
#print(eval(compile(expression, '', mode='eval')))
#
for x in expression_nodes(expression):
    pass
    #print x
#
#
#
class NodeVisitor(ast.NodeVisitor):

    def visit_Num(self, tree_node):
        print "visit...", tree_node
        self.generic_visit(tree_node)

    def visit_BinOp(self, tree_node):
        print "visit...", tree_node
        self.generic_visit(tree_node)

class NodeTransformer(ast.NodeTransformer):
    def visit_Num(self, tree_node):
        print "transform...", tree_node


node_visit = NodeVisitor().visit(expression)
node_transform = NodeTransformer().visit(expression)
