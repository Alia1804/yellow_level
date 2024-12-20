def something(intervals):
    intervals.sort(key=lambda x: x[0]) # Сортируем интервалы по начальным точкам

    something = [] # Инициализируем массив для хранения объединенных интервалов

    for interval in intervals:
        if not something or something[-1][1] < interval[0]: # Если массив merged пуст или текущий интервал не перекрывается с последним интервалом в something
            something.append(interval)
        else:
            something[-1][1] = max(something[-1][1], interval[1])  # Объединяем текущий интервал с последним интервалом в something

    return something




