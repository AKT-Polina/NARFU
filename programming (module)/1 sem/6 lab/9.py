regions = {
    'Архангельская область': ['Архангельск', 'Новодвинск', 'Северодвинск', 'Шенкурск', 'Котлас'],
    'Ленинградская область': ['Санкт-Петербург', 'Пушкин', 'Павловск']
}
 
cities = ['Архангельск', 'Пушкин', 'Котлас']
 
for city in cities:
    for region, cities_in_region in regions.items():
        if city in cities_in_region:
            print(region)
            break
