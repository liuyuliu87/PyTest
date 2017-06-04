def println(the_list,flag=False,level=0):
    for each_item in the_list:
        if isinstance(each_item,list):
            println(each_item,flag=True,level=level+1)
        else:
            if flag:
                for i in range(level):
                    print("\t",end='')
            print(each_item)


if __name__=="__main__":
    namelist=['andy','Alex',['shane','Aria']]
    println(namelist)