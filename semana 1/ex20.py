# Solution code that calculates amount to be paid by a product
code_product1, units_product1, price_product1 = [float(i) for i in input().split()]
code_product2, units_product2, price_product2 = [float(i) for i in input().split()]

amount_paid = (units_product1*price_product1) + (units_product2*price_product2)
print("VALOR A PAGAR: R$ {:.2f}".format(amount_paid))