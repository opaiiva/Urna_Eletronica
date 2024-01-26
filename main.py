# Urna Eletronica

urna = [['Alice', 0], ['Bob', 0], ['Charlie', 0]]

for i in range(4):
    
    voto = input('Digite o nome do candidato em que deseja votar: ')

    encontrado = False
    
    for candidato in urna:
        
        if candidato[0] == voto:
            
            candidato[1] += 1
            
            encontrado == True
            break
        
    if not encontrado:
        
        print('Voto nulo. ')
        
print('\n Resultados: ')
        
votos_maximos = -1
vencedor = ''

for candidato in urna:
    
    print(f'Candidato{[0]}: {candidato[1]} votos')
    
    if candidato[1] > votos_maximos:
        
        votos_maximos = candidato[1]
        
        vencedor = candidato[0]
        
print(f'\n O vencedor é {vencedor} com {votos_maximos} votos!')
    
print()
