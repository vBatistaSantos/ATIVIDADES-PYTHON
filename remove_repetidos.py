def remove_repetidos(li):
    list.sort(li);
    for x in li:
        while li.count(x)!=1:
            li.remove(x);
    return li;
