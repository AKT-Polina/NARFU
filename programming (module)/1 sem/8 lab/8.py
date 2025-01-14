def delete_backspace(st):
    result = []
    
    for char in st:
        if char == '@':
            # Если результат не пустой, удаляем последний добавленный символ
            if result:
                result.pop()
        else:
            result.append(char)
            
    return ''.join(result)

# Проверки
print(delete_backspace('пп@олс@кр@овт@оде@ец'))  # Ожидаемый результат: полководец
print(delete_backspace('сварка@@@@@лоб@ну@'))   # Ожидаемый результат: слон
