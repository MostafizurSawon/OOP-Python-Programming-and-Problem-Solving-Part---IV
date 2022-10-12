my_list = ['@F1', 'O@BCD','!', '@F2','ADDAB','!', '@F3','OKKA','!']

# expected: {'@F1','OBCD','@F2','ADDAB','@F3','OKKA'}

output_dict = {}

for i,val in enumerate(my_list):
    # print(i,">", val)
    if val[0] == '@':
        output_dict[val] = my_list[i+1]

print(output_dict)

