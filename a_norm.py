def main():

    import pandas as pd
    import re as re

    fh = open("A.csv","r")

    if fh.mode == 'r':
        fl = fh.readlines()
        for x in fl:
            p = re.compile(r',')
            result = p.split(x)
            p2 = re.compile(r';')
            dict_re1= result[0]
            dict_re2 = p2.split(result[1])
            dict_re3 = p2.split(result[2])
            dict_re4 = p2.split(result[3])
            length = len(dict_re4)
            if length > 1 :
                num = ""
                for i in range(length):
                    num = str(dict_re1)+"_"+str(i)
                    line = num+ ","+dict_re2[i]+ ","+ dict_re3[i]+","+ dict_re4[i]
                    print(line)
            
        


#            print(result[2])





if __name__=="__main__":
    main()
