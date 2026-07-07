# a common mistake in real time while working with while loop is putting into infinite loop. Where 
# the loop never stops, make sure the expression in the loop will eventually becomes false, you can use break keyword
# to exit from the loop. 

i = 0
a = 'pythonwithnetwork'
# print all values except 'n' & 'r'

while i < len(a):
    if a[i] == 'n' or a[i] == 'r':
        i += 1
        continue
    print(a[i])
    i += 1