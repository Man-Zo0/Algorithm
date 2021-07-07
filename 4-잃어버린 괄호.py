sent = input()
sent = '(' + sent + ')'
sent = sent.replace('-',')-(')

r=''
skipzero = True

for s in sent:
    if s == '0':
        if not skipzero:
            r += s
    elif '1' <= s <= '9':
        r += s
        skipzero = False
    else:
        r += s
        skipzero = True

print(eval(r))