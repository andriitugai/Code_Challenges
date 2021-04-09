
def parse(x):
    operators = set('+-*/')
    op_out = []
    num_out = []
    buff = []
    for c in x:
        if c in operators:
            num_out.append(''.join(buff))
            buff = []
            op_out.append(c)
        else:
            buff.append(c)
    num_out.append(''.join(buff))
    return num_out,op_out

print (parse('-37+2/15'))
