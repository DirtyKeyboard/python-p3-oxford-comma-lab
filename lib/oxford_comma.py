def oxford_comma(items):
    if len(items) == 2:
        return " and ".join(items)
    elif len(items) >= 3:
        ret = ""
        for el in items:
            if items.index(el) == len(items) - 1:
                ret += 'and ' + el
            else:
                ret += el + ', '
        return ret
    else:
        return ", ".join(items)
