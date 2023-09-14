def validateip(ip):
    count=""
    num=0
    k=0
    for i in range(len(ip)):
        if ip[i]!=".":
            num=0
            count+=ip[i]
        else:
            count=""
            num+=1
            k+=1
        if(k>=4):
            return "not valid"
        if(len(count)==1 and int(count)==0):
            return "not valid"
        if(num>1 or( len(count)>1 and (int(count)<=0 or int(count)>=255))):
            return "not valid"
    return "valid ip"
ip=input()
print(validateip(ip))