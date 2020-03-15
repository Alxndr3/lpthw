jogdict = dict()
joglist = list()
numgol = list()
while True:
    jogdict['jogador'] = str(input('Nome do Jogador: ')).strip().title()
    npart = int(input(f'Quantas partidas {jogdict["jogador"]} jogou? '))
    totgol = 0
    for x in range(1, npart + 1):
        golp = int(input(f"Quantos gols na partida {x}? "))
        numgol.append(golp)
        totgol += golp
    jogdict['gols'] = numgol.copy()
    jogdict['total'] = totgol
    joglist.append(jogdict.copy())
    numgol.clear()
    bk = ' '
    while bk not in 'SN':
        bk = str(input('Deseja continuar? S/N: ')).strip().upper()
    if bk == 'N':
        print(30 * '-')
        break
    print(30 * '-')
print(f"{'Cod':<10}{'Nome':<10}{'Gols':<10}{'Total':<10}")
for x, y in enumerate(joglist):
   print(f"{x:<10}{y['jogador']:<10}{y['gols'].__str__():<10}{y['total']}")
print(30 * '-')
while True:
    try:
        est = int(input('Mostrar dados de qual Jogador? '))
    except ValueError:
        pass
    else:
        if est == 999:
            print('bye...')
            break
        else:
            try:
                lev = joglist[est]
            except IndexError:
                print(f'ERRO. Não exite jogador com o código {est}')
                print(30 * '-')
                pass
            else:
                print(f"Levantamento do jogador {lev['jogador']}")
                for f, g in enumerate(lev['gols']):
                    print(f'No jogo {f + 1} fez {g} gols')

