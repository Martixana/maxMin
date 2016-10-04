Maximum = None
Minimum= None

while True:
    inp = raw_input('Enter a number: ')
    if inp == 'done': break
    
    try:
        num = int(inp)
    except:
        print 'Invalid input'
        continue
    if Maximum is None or num > Maximum:
        Maximum = num
    if Minimum is None or num < Minimum:
        Minimum = num
    
print 'Maximum is', Maximum
print 'Minimum is', Minimum