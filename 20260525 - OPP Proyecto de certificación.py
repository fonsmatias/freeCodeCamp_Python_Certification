import math

class Rectangle():
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def set_width(self,width):
    # Establece el ancho del rectángulo
        self.width=width

    def set_height(self,height):
    # Establece la altura del rectángulo
        self.height=height
        
    def get_area(self):
    # Devuelve el área
        area=self.width*self.height
        return (area)
    
    def get_perimeter(self):
    # Devuelve el perímetro  2(ancho+alto)
        perimetro=2*(self.height+self.width)
        return (perimetro)
    
    def get_diagonal(self):
    # Devuelve la diagonal (pitágoras)
        diagonal=math.sqrt(self.height**2+self.width**2)
        return (diagonal)

    def get_picture(self):
    # Devuelve una cadena que representa la forma usando líneas de *. El número de líneas debe ser igual a la altura y el número de * en cada línea debe ser igual al ancho. Debe haber un carácter de nueva línea (\n) al final de cada línea. Si el ancho o la altura es mayor que 50, esto debe devolver la cadena: Demasiado grande para una imagen
        if (self.width > 50) or (self.height > 50):
            return ("Too big for picture.")
        return(( "*" * self.width + "\n" ))*(self.height)

    def get_amount_inside(self, figura):
    # acepta otra figura (cuadrado o rectángulo) como argumento. Devuelve el número de veces que la figura pasada como argumento cabe dentro de la figura que invoca (sin rotaciones). Por ejemplo, en un rectángulo con un ancho de 4 y una altura de 8 podrías caber dos cuadrados con lados de 4
        
    # planteo relación entre lasrgos y anchos: cuántas piezas entran a lo ancho, cuántas a lo largo + multiplicar esos dos resultado    
        cantidad_a_lo_ancho=self.width // figura.width
        cantidad_a_lo_largo=self.height // figura.height
        cantidad=cantidad_a_lo_ancho*cantidad_a_lo_largo
        return (cantidad)

    def __str__(self):
        return (f"Rectangle(width={self.width}, height={self.height})")
            
            
class Square (Rectangle): #subclase de Rectangle
    def __init__(self, width):
        super().__init__(width, width)

    def set_side(self, width):
    # defino los 2 lados iguales para que cuando vayan a la clase padre tenga 2 argumentos para calcular
        self.width=width
        self.height=width

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return (f"Square(side={self.width})")



#-------------------------------------------------

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))