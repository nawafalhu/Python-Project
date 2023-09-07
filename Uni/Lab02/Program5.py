list = ['Blue color', 'Red#', 'Purple', 'Red %', 'Black']

special_char = '@_!#$%^&*()<>?/\|}{~:;.[]'
 
out_list = [''.join(x for x in string if not x in special_char) for string in list]

print(out_list)

print(list)