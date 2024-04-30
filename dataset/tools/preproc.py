path = './folder'
path_res = './folder_preproc'
'''
for i in range(390, 400):
    with open(path + f'/{i}_a.txt', 'r') as f:
        art = f.read()
    with open(path + f'/{i}_s.txt', 'r') as f:
        sum_ = f.read()
    if (len(art) < 50  or len(sum_) < 10):
        print(i)
'''
for i in range(390, 400):
        with open(path + f'/{i}_a.txt', 'r') as f:
                art = f.read().replace('\n ', '')
        art = art.replace(' .', '.')
        art = art.replace(' ,', ',')
        art = art.replace(' ', ' ')
        with open(path_res + f'/{i}_a.txt', 'w') as f:
                f.write(art)
        
        with open(path + f'/{i}_s.txt', 'r') as f:
                sum_ = f.read().replace('\n ', '')
        sum_ = sum_.replace(' .', '.')
        sum_ = sum_.replace(' ,', ',')
        sum_ = sum_.replace(' ', ' ')
        
        with open(path_res + f'/{i}_s.txt', 'w') as f:
                f.write(sum_)
        
#'''