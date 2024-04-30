path = './folder_preproc'
path_res = './folder_div10000/300-400'
max_len = 10000

for i in range(390, 400):
    with open(path + f'/{i}_a.txt', 'r') as f:
        art = f.read()
    with open(path + f'/{i}_s.txt', 'r') as f:
        sum_ = f.read()
    art += '\n\n' + sum_
    
    n = len(art)//max_len
    n += 1 if len(art)%max_len else 0
    with open(path_res + f'/{i}.txt', 'w') as f:
        f.write(str(n))
    
    for j in range(n):
        with open(path_res + f'/{i}_{j}.txt', 'w') as f:
            f.write(art[j*max_len : (j+1)*max_len])