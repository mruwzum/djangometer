from igmeter.InstaMeter import *



def ejecutarMeter():

    im = InstaMeter(username='elenabravoarche')
    res = im.analyze_profile()

    listaResultado = []
    listaResultado.append(im.print_account_statistic())
    listaResultado.append(im.print_top_liked())
    listaResultado.append(im.print_top_commented())
    listaResultado.append(im.print_top_viewed())
    return listaResultado
