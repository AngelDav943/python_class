import math

def arearect(b:float, a:float) -> float:
    """
    Calcula el area de un rectangulo
    - b (float): Base del rectangulo
    - a (float): Altura del rectangulo
    """
    return b * a 

def dist(x1:float, y1:float, x2:float, y2:float) -> float:
    """
    Calcula distancias entre dos puntos.    
    --params--
    - x1 (float): coordenada x del primer punto
    - y1 (float): coordenada y del primer punto
    - x2 (float): coordenada x del segundo punto
    - y2 (float): coordenada y del segundo punto

    --return--
    - dist (float): es la distancia entre los dos puntos
    """
    x:float = math.pow(x2 - x1, 2)
    y:float = math.pow(y2 - y1, 2)
    dist = math.sqrt( x + y )
    return dist

if __name__ == "__main__":
    print("Funciones!!")