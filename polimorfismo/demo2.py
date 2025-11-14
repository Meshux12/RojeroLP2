class Humano:
    def hablar(self)->str:
        return "Que hay de nuevo viejo"
    
class Perro:
    def hablar(self)->str:
        return("Woof woof")
    
class Robot:
    def hablar(self)->str:
        return ("Beep boop")
    
def hablando(objeto)->str:
    return objeto.hablar()

h = Humano()
p = Perro()
r = Robot()

print(hablando(h))
print(hablando(p))
print(hablando(r))