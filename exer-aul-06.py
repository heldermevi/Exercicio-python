# vendo se o valor é numerico decimal alfabético ou alfa numerico

n = input ('Digite um valor =')

print ('E numerico?', n.isnumeric() )
print ('E decimal?', n.isdecimal() )
print ('E alfa numerico', n.isalnum() )
