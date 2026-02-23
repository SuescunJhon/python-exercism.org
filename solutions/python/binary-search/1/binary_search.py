def find(search_list, value):
    if not search_list:
        raise ValueError("value not in array")
        
    index = len(search_list) // 2
    middle = search_list[index]
    
    if middle == value:
        return index
        
    if middle > value:
        return find(search_list[:index], value)

    return find(search_list[index+1:], value) + index + 1
