# 'w' : write
# 'r': read
# 'a' : add
nomFicher = 'testFile.txt'
"""with open(nomFicher, 'w') as f:
    f.write('rayan')
    f.close()"""


"""with open(nomFicher, 'r') as f:
    content = f.readl()
    list_nom = content.split()
    list_nom1 = content.split(',')
    print(list_nom)
    print(list_nom1)
    f.close()"""

"""with open(nomFicher, 'r') as f:
    content = f.readlines()
    print(content)
    f.close()"""

"""nom = input('nom: ')
prenom = input('prenom: ')
age = input('age: ')
annee = input('annee: ')

with open(nomFicher, 'a') as f:
    f.write('\n')
    f.write(nom+' ')
    f.write(prenom+' ')
    f.write(age+' ')
    f.write(annee)
    f.close()"""

"""with open(nomFicher, 'w') as f:
    f.truncate(0)
    f.close()"""

with open(nomFicher, 'r') as f:
    content = f.readlines()
    print(content)
    f.close()

with open(nomFicher, 'w') as f:
    f.write(content[0])
    f.write(content[1])
    f.close()

