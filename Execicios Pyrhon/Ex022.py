n = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {n.upper()}')
print(f'Seu nome em minúsculas é {n.lower()}')
f = n.split()
d = ''.join(f)
print(f'Seu nome tem ao todo {len(d)} letras')
print(f'Seu primeiro nome e {f[0].capitalize()} e ele tem {len(f[0])} letras')
