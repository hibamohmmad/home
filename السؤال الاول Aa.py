group=['hiba','aya','reem','yousef','ibrahem']
name=input('enter student name')
for i in range(5):
     if name in group:
        print(name,'the user is graduated')
        break
     else:
        print('the user is failed')
        break
