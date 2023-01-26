# Este programa cuenta las caritas felices dado que estas empiezan con ':' o ';', pueden tener '~' o '-', y si o si
# terminan con 'D' o ')'
# El tiempo de ejecucion es O(n) siendo n el numero total de caracteres del arreglo entrante

smiles = [';D', ':-(', ':-)', ';~)']
# smiles = [';]', ':[', ';*', ':$', ';-D']

count = 0

for s in smiles:
    if s[0] in [':', ';']:
        if s[1] in ['-', '~']:
            if s[2] in [')', 'D']:
                count += 1
        elif s[1] in [')', 'D']:
            count += 1

print(count)
