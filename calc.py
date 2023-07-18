x = input()
expression = compile(x, 'string', 'eval')
print(eval(expression))