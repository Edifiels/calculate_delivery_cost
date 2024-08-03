def calculate_delivery_cost(distance, size, fragile, load):
    cost = 0
    
    # Расчет стоимости по расстоянию
    if distance > 30:
        cost += 300
    elif distance > 10:
        cost += 200
    elif distance > 2:
        cost += 100
    else:
        cost += 50
    
    # Учет габаритов
    if size == "big":
        cost += 200
    else:
        cost += 100
    
    # Учет хрупкости
    if fragile:
        if distance > 30:
            raise ValueError("Хрупкие грузы нельзя возить на расстояние более 30 км")
        cost += 300
    
    # Учет загруженности
    load_factors = {
        "very_high": 1.6,
        "high": 1.4,
        "above_average": 1.2,
        "normal": 1
    }
    cost *= load_factors.get(load, 1)
    
    # Проверка минимальной суммы
    return max(400, int(cost))
