x = 1
set = []
while True:
    x_square = x**2
    if x_square > 100:
        break
    set.append((x,x_square))
    x+=1
print(("-"*20).center(2,"*"))
for i in range(len(set)):
    print("{0:3d} | {1:5d}".center(20).format(set[i][0],set[i][1]))
print(("-"*20).center(2,"*"))