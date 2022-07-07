import stack
def do_math(op,op1,op2):
    if op=="*":
        return op1*op2
    elif op=="/":
        return op1/op2
    elif op=="+":
        return op1+op2
    elif op=="-":
        return op1-op2
def postfix_operator(origin_formula):
    s_operator = stack.stack()
    s_number = stack.stack()
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    list_formula=origin_formula.strip(' ').split()

    for token in list_formula:
        if token in "0123456789":
            s_number.push(int(token))
        elif token == '(':
            s_operator.push(token)
        elif token==')':
            top_token = s_operator.pop()
            while top_token != "(":
                op1=s_number.pop()
                op2=s_number.pop()
                s_number.push(do_math(top_token,op1,op2))
                top_token = s_operator.pop()
        else:
            while (not s_operator.isEmpty()) and s_number.size()>=2 and  prec[s_operator.peek()]>=prec[token]:
                op1=s_number.pop()
                op2=s_number.pop()
                s_number.push(do_math(s_operator.pop(),op1,op2))
            s_operator.push(token)

    while not s_operator.isEmpty() and s_number.size()>=2:
        op1=s_number.pop()
        op2=s_number.pop()
        s_number.push(do_math(s_operator.pop(),op1,op2))
    return s_number.pop()

