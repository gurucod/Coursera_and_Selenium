#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
c = [8, 9, 0, 1, 2, 6, 3]

def merge(a, b):
    """Функция склеивает 2 списка в один и сортирует при этом элементы 2 списков в порядке возрастания"""
    i = 0
    j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:] + b[j:]
    return result


def merge_sort(a):
    """Функция проверяет сколько элементов в списке, если больше 1 элемента то разбивает список на 2 части
     и вставляет их в функцию(merge) кароче тут рекурсия и нужно просмотреть в дебагере"""
    if len(a) > 1:
        return merge(merge_sort(a[:len(a) // 2]), merge_sort(a[len(a) // 2:]))
    else:
        return a


print(merge_sort(c))
