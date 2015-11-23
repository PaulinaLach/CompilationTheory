
class Node(object):

    def __str__(self):
        return self.printTree()

#class Node(object):
#
#    def accept(self, visitor):
#        return visitor.visit(self)
#
#    def __init__(self):
#        self.children = ()

class BinExpr(Node):

    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

#class BinExpr(Node):
#
#    def __init__(self, op, left, right, token):
#        self.token = token
#        self.op = op
#        self.left = left
#        self.right = right

class Const(Node):
    def __init__(self, val):
        self.val = val

class Declarations(Node):
    def __init__(self):
        self.declarations = []

    def push(self, declaration):
        self.declarations.append(declaration)

class Declaration(Node):
    def __init__(self, type, inits):
        self.type = type
        self.inits = inits

class Instructions(Node):
    def __init__(self):
        self.instructions = []

    def push(self, instruction):
        self.instructions.append(instruction)

class ReturnInstr(Node):
    def __init__(self, expr):
        self.expr = expr

class PrintInstr(Node):
    def __init__(self, expr):
        self.expr = expr

class Inits(Node):
    def __init__(self):
        self.inits = []

    def push(self, init):
        self.inits.append(init)

class Init(Node):
    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

class AssignmentInstruction(Node):
    def __init__(self, id, expr):
        self.id = id
        self.expr = expr

class ChoiceInstr(Node):
    def __init__(self, condition, instruction, else_instr):
        self.condition = condition
        self.instruction = instruction
        self.else_instr = else_instr

class WhileInstr(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction

class RepeatInstr(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction

class ContinueInstr(Node):
    pass #use default

class BreakInstruction(Node):
    pass #use default

class CompoundInstruction(Node):
    def __init__(self, declarations, instructions_opt):
        self.declarations = declarations
        self.instructions_opt = instructions_opt

class CastFunction(Node):
    def __init__(self, functionName, args):
        self.functionName = functionName
        self.args = args

class ExprInBrackets(Node):
    def __init__(self, expr):
        self.expr = expr

class ExpressionList(Node):
    def __init__(self):
        self.expressions = []

    def push(self, expr):
        self.expressions.append(expr)

class FunctionList(Node):
    def __init__(self):
        self.functions = []

    def push(self, expr):
        self.functions.append(expr)

class Function(Node):
    def __init__(self, type, id, args_list_or_empty, compound_instr):
        self.type = type
        self.id = id
        self.args_list_or_empty = args_list_or_empty
        self.compound_instr = compound_instr

class Arguments(Node):
    def __init__(self):
        self.arguments = []

    def push(self, argument):
        self.arguments.append(argument)

class Argument(Node):
    def __init__(self, type, id):
        self.type = type
        self.id = id

#do nowej gramatyki: program -> blocks -- blocks -> blocks block -- block -> declarations fundefs instructions
class Block(Node):
    def __init__(self, declarations, fundefs_opt, instructions_opt):
        self.declarations = declarations
        self.fundefs_opt = fundefs_opt
        self.instructions_opt = instructions_opt

#do nowej gramatyki:
class Blocks(Node):
    def __init__(self):
        self.blocks = []

    def push(self, block):
        self.blocks.append(block)
