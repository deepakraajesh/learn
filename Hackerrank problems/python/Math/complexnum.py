from cmath import phase

com = complex(input())
print(round(abs(complex(com.real,com.imag)),3))
print(round(phase(complex(com.real,com.imag)),3))