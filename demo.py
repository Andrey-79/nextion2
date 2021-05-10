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
    pass

x, y = 100, 100
width, height = 200, 200

draw_house(x, y, width, height)
