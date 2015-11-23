class Symbol():
    pass

class VariableSymbol(Symbol):

    def __init__(self, name, type):
        self.name = name
        self.type = type


class FunctionSymbol(Symbol):

    def __init__(self, name, type, arguments):
        self.name = name
        self.type = type
        self.arguments = arguments


class SymbolTable(object):

    def __init__(self, parent, name): # parent scope and symbol table name
        self.parent = parent
        self.name = name
        self.store = {}
        self.scopes= []

    def put(self, name, symbol): # put variable symbol or fundef under <name> entry
        self.store[name] = symbol

    def get(self, name): # get variable symbol or fundef from <name> entry
        if name in self.store:
            return self.store[name]
        else:
            if self.parent is not None:
                return self.parent.get(name)
            else:
                return None

    def getParentScope(self):
        return self.parent

    def pushScope(self, name):
        curr = SymbolTable(self, name)
        self.scopes.append(curr)
        return curr

    def popScope(self):
        if len(self.scopes) > 0:
            self.scopes.pop()
        return self.parent