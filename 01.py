fruts = ['apple','bananas','grapes','kiwi']
i = 0
while i < len(fruts):
    output = f' {i+1}  {fruts[i]}'
    print(output)
    i +=1



fruts1 = ['apple','bananas','grapes','kiwi']
fruts2 = ['apple','bananas','grapes','kiwi']
for i in fruts2:    # возник вопрос , если мы будем перебирать  1 список , почему удаляется через 1 ?
    if i in fruts1:
        fruts1.remove(i)
print(fruts1)

first_list = [2, 7, 5, 6, 9, 15]
new_list = []
last_name = len(first_list)
i = 0
while i < last_name :
    if first_list[i] % 2 == 0:
        new_list.append(first_list[i] / 4)
    else:
        new_list.append(first_list[i] * 2)
    i += 1
print(new_list)

