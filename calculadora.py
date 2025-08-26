# calculadora simples que reinicia automaticamente

def calculo (x,y,op):
	if (op == "+"):
		return x+y
	elif (op == "-"):
		return x-y
	elif (op == "/"):
		return x/y
	elif (op == "*"):
		return x*y
	else: (print ("Digite um operador valido! "))
		calculo (x,y,op)
x = input
y = input
op = input