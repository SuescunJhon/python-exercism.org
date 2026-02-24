def append(list1, list2):
    return [*list1, *list2]


def concat(lists):
    if not lists:
        return lists
    return append(lists[0], concat(lists[1:]))


def filter(function, list):
    if not list:
        return list
    if function(list[0]):
        return append([list[0]], filter(function, list[1:]))
    return filter(function, list[1:])


def length(list):
    
    def aux(list, count):
        if len(list) == 0:
            return count
        return aux(list[1:], count + 1)

    return aux(list, 0)
        

def map(function, list):
    if len(list) == 0:
        return list
    return append([function(list[0])], map(function, list[1:]))


def foldl(function, list, initial):
    if len(list) == 0:
        return initial
    return foldl(function, list[1:], function(initial, list[0]))


def foldr(function, list, initial):
    if len(list) == 0:
        return initial
    return foldr(function, list[:-1], function(initial, list[-1]))


def reverse(list):
    if len(list) == 0:
        return list

    return append([list[-1]], reverse(list[:-1]))
        
