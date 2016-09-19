import numpy as np

def parse(filePath, start, end):

    freq_list = []
    cnt = 0
    with open(filePath, "r") as f:
        while True:
            line = f.readline().strip()
            
            if line == '':
                break

            tokens = [int(i) for i in line.split(',')]
            freq_list.append(tokens)

            cnt += 1

            if cnt % 1000 == 0:
                print cnt
        ### END - while
    ### END - with
    
    print "start saving"
    np.save("db3_octa_freq", freq_list)
### END - def parse


def main():
    parse("db3_octa_freq.csv")

main()
