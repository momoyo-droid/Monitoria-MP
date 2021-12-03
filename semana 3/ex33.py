nome = input()

PO_aulas = int(input())
PO_moni = int(input())
PO_tare = int(input())
NOTA_av = float(input())

if PO_aulas == 100 and PO_moni == 100 and PO_tare >= 75 and NOTA_av >= 5.0:
    print("{} com direito a certificado".format(nome))
else:
    print("{} sem direito a certificado".format(nome))
