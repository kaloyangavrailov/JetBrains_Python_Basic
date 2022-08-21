o_strand, c_strand = input().split()

restriction_site = 'CTGCAG'
c_restriction_site = ''
for i in range(len(restriction_site)):
    if restriction_site[i] == 'A':
        c_restriction_site += 'T'
    elif restriction_site[i] == 'C':
        c_restriction_site += 'G'
    elif restriction_site[i] == 'T':
        c_restriction_site += 'A'
    elif restriction_site[i] == 'G':
        c_restriction_site += 'C'

start_i_restriction_site = o_strand.find(restriction_site)

o_cut = o_strand[0:start_i_restriction_site+1]

o_remainder = o_strand[start_i_restriction_site+1:len(o_strand)]

print(f'{o_cut} {o_remainder}')


start_i_c_restriction_site = c_strand.find(c_restriction_site)

c_cut = c_strand[0:start_i_c_restriction_site+5]
c_remainder = c_strand[start_i_c_restriction_site+5:len(c_strand)]

print(f'{c_cut} {c_remainder}')
