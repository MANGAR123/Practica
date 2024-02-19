def grade(s,m, n, i, no):
    """
    >> > grade(4.99)
    'suspens'
    >> > grade(8)
    'notable'
    >> > grade(6.99)
    'aprovat'
    >> > grade(9.5)
    'excel.lent'
    >> > grade(10)
    'MH'
    """
    n= 0
    m= 5
    i= 0
    while i<5:
        i= 1+i
        print("Pon puntaje de la materia", i)
        no= "user"
        n= no + n

s= n / m

if s<5:
    print( s ,",el alumno esta suspendido")
if s<9 and s>=7:
    print(s ,",el alumno es notable")
if s>=5 and s<7:
    print( s ,",el alumno esta aprobado")
if s>=9 and s<10:
    print(s ,",el alumno esta excelente")
if s == 10:
    print(s, ",el alumno esta MH")

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())