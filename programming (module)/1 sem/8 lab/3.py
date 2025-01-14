def most_common_top3(st):
    str = st.replace(' ', '')
    from collections import Counter
    list = Counter(str)
    
    print(list.most_common(3))
  


most_common_top3('Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью')
