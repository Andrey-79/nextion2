def main():
    x, y = 100, 100
    width, height = 200, 200
    
    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
    Функция рисует домик ширины width и высоты height
    от опорной точки  (x, y) которая находиться в нижней
    точке фундамента
    :param x координата х середины домика
    :param y координата у низа фундамента
    :param width полная ширина домика (фундамент и вылет крыши включены)
    :param height полная высота домика
    :return: None
    """
    print("Типа рисую домик...", x, y, width, height)
    fondation_height = 0.05 * height
    walls_width  = 0.9 * width
    walls_height  = 0.5 * height
    roof_height  = height - fondation_height - walls_height
    
    draw_house_fondation(x, y, width, fondation_height)
    draw_house_walls(x, y - fondation_height, walls_width, walls_height)
    draw_house_roof(x, y - fondation_height - walls_height, width, roof_height)

    
def draw_house_fondation(x, y, width, height):
    """
    Основание домика
    """
    print("Типа рисую основание домика...", x, y, width, height)
    

    
def draw_house_walls(x, y, width, height):
    """
    Стены
    """
    print("Типа рисую стены домика...", x, y, width, height)
    

    
def draw_house_roof(x, y, width, height ):
    """
    Крыша
    """
    print("Типа рисую крышу домика...", x, y, width, height)
    

main()
