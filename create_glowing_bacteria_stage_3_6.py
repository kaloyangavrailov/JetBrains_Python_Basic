def get_complimentary(o_gfp):
    global c_gfp

    c_gfp = ''

    for i in range(len(o_gfp)):
        if o_gfp[i] == 'A':
            c_gfp += 'T'
        elif o_gfp[i] == 'C':
            c_gfp += 'G'
        elif o_gfp[i] == 'T':
            c_gfp += 'A'
        elif o_gfp[i] == 'G':
            c_gfp += 'C'

    return print(f'{o_gfp}\n{c_gfp}')

O_gfp = input()

get_complimentary(O_gfp)