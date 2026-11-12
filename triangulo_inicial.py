def classificar_triangulo(a, b, c):
    
    if a == b == c:
        return "Equilátero"
    if a == b or a == c or b == c:
        return "Isósceles"
    return "Escaleno"
