def main():

    import pandas as pd
    import re as re

    in_filename = "A.csv"
    out_filename = "B.csv"
    
    with open(in_filename, 'r') as in_file, open(out_filename, 'a') as out_file:

        if in_file.mode == 'r':
            input_lines = 0
            output_lines = 0
            for x in in_file:
                input_lines = input_lines + 1
                p = re.compile(r',')
                result = p.split(x)
                p2 = re.compile(r';')
                dict_re1= result[0]
                dict_re2 = p2.split(result[1])
                dict_re3 = p2.split(result[2])
                dict_re4 = p2.split(result[3])

#                print(type(dict_re1), type(dict_re2), type(dict_re3), type(dict_re4))
   
                
                length = len(dict_re4)
                print(input_lines, "=", dict_re1)

                lines = str(dict_re1[0])+ ","+dict_re2[0]+ ","+ dict_re3[0]+","+ dict_re4[0]+"\n"
                output_lines =output_lines + 1
                out_list=[]
                
                if length > 1 :
                    output_lines = output_lines -1
                    num = ""
                    i=0
                    
                    for i in range(length-1):
                        output_lines = output_lines + 1
                        num = str(dict_re1)+"_"+str(i)
                  
                        
                        a= num+ ","+dict_re2[i]+ ","+ dict_re3[i]+","+ dict_re4[i] +"\n"
                        out_list.append(a)
                    else :
                        out_list.append(lines)
                i=0
                for i in range(length-1):
                    out_file.write(out_list[i])

        print("total input line =", input_lines , "\n", "Total output line = ", output_lines)

       
if __name__=="__main__":
    main()
