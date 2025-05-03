'''
script pour résoudre une équation de la forme:
A = B(T1^4 - T2^4) + C(T1-T2)
avec A,B,C et T1 connues.
On utilise une methode de linéarisation.
'''

def nouveauT2(A,B,C,T1,T2):
	D = 4*B*((T1+T2)/2)**3
	return (T1*(D+C) - A)/(D+C)

A = -41.3*10**6
B = 1.04*10**(-5)
C = 3649.54
T1 = 293
precision = 0.1

T2 = 3000
prochainT2 = nouveauT2(A,B,C,T1,T2)

i=0
while abs(T2 - prochainT2) > precision:
	
	print(T2, prochainT2)
	
	T2 = prochainT2
	prochainT2 = nouveauT2(A,B,C,T1,T2)
	i+=1

print("solution trouvée:", T2)
print("verification:",A - B*(T1**4-T2**4) - C*(T1-T2))
print("En",i,"itérations")
