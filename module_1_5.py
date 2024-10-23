immutablt_var=1,2,3,True,'apple'
print(immutablt_var)
immutablt_var#[0]=23# кортеж не поддерживает обращение по элементам.
print(immutablt_var)
mutable_list=[1,2,3,45]
print(mutable_list)
mutable_list[1]='banana'
print(mutable_list)