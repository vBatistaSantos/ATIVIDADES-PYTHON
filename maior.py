def maior_elemento(li):
    maior=li[0];
    for x in li:
        if maior<x:
            maior=x;
    return maior
