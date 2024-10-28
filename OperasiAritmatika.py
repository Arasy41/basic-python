# operasi aritmatika

a = 21
b = 4

# operasi tambah +
hasil = a + b 
print(a,"+",b"=",hasil)

# operasi kurang -
hasil = a - b
print(a,"-",b,"=",hasil)

# operasi perkalian *
hasil = a * b
print(a,"*",b,"=",hasil)

# operasi pembagian
hasil = a / b
print(a,"/",b,"=",hasil)

# operasi eksponen (pangkat) **
hasil = a ** b 
print(a,"**",b,"=",hasil)

# operasi modulus %
hasil = a % b 
print(a,"%",b,"=",hasil)

# operasi floor division //
hasil = a // b 
print(a,"//",b,"=",hasil)

# prioritas operasi operational predence

x = 4
y = 3
z = 5

hasil = x ** y * z + x / y - y % z // x 
print(x, '*' ,y, '' ,z, '+' ,x, '/' ,y, '-' ,y, '%' ,z, '//' ,x,'=',hasil)

hasil = x + y * z
print(x, '+' ,y, '*',z,'=',hasil)
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print('(',x, '+' ,y,') *',z,'=',hasil)