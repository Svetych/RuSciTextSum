# -*- coding: utf-8 -*-

for i in range(100):
    with open(f"{i}.txt", "r", encoding="utf-8") as f:
        txt = f.read().replace('\t', ' ')
    
    while txt.find('  ') != -1:
        txt = txt.replace('  ', ' ')

    with open(f"{i}.txt", "w", encoding="utf-8") as f:
        f. write(txt)