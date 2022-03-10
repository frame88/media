b = input('Inserisci una data nel formato dd/mm/yy: ')
a = float(input('inserisci i tuoi guadagni giornalieri: '))

count = 1
tot = a
var_lettura = open("dati.txt", "a")
var_lettura.write('\n' + b + '\t' + str(a) + '\t' + 'La tua media giornaliera: ' + str(tot/count) + ' euro')

while a != 000:

    b = input('Inserisci una data nel formato dd/mm/yy: ')
    a = float(input('inserisci i tuoi guadagni giornalieri: '))
    tot += a
    if a != 000:
        count += 1
        var_lettura.write('\n' + b + '\t' + str(a) + '\t' + 'La tua media giornaliera: ' + str(tot/count) + ' euro')


var_lettura.close()
print('La tua media giornaliera è:', tot/count,'€')
print(var_lettura)
