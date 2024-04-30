# -*- coding: utf-8 -*-

path_1 = './folder_res'
path_2 = './folder_div10000/300-400'
path_res = './folder_translated'


for i in range(300, 400):
    with open(path_2 + f'/{i}.txt', 'r') as f:
        n = int(f.read())
    
    art = ''
    for j in range(n):
        with open(path_1 + f'/{i}_{j}.txt', 'r', encoding="utf-8") as f:
            art += f.read().replace('\\n\\n', '\n\n')[37:-11]
    with open(path_res + f'/{i}.txt', 'w', encoding="utf-8") as f:
            f.write(art)
