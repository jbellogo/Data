
if __name__ == "__main__":
    f = open("./words_250000_train.txt", "r")
    mydict = {}

    for w in f:
        key = len(w)-1
        # ##### Get carinalities. 
        # if key in mydict: 
        #     mydict[key] +=1
        # else:
        #     mydict[key] = 1
        ##### Partition universe into length
        g = open(f"./words_by_length/length-{key}.txt", "a")
        g.write(w)
        g.close()
