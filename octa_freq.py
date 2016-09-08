import numpy as np

def parse(filePath):
    print("started")
    octa_freq = [] # shape: (n_samples, 4^8)
    
    with open(filePath) as f:
        print "read file"
        line = f.readline() # read first line (containing info)
        cnt = 0
        
        while True:
            line = f.readline().strip()
            if line == '':
                break
            
            try:
                cnt += 1
                tokens = line.split(',')
                
                # validity check
                if len(tokens[5:]) != 65536:
                    continue
                
                octa = [int(i) for i in tokens[5:]]
                octa_freq.append(cal_freq(octa))
                
                if cnt % 1000 == 0:
                    print cnt 
            ### END - try
            except ValueError:
                continue
            ### END - except
        ### END - for line
    ### END - with

    np.save("db3_octa_freq", octa_freq)
    print("fininsed")
### END - def parse

def cal_freq(cntList):
    total = sum(cntList)
    freqList = []
	
    for item in cntList:
	freqList.append(item/total)

    return freqList
### END - def cal_freq


def main():
    parse("8mer.csv")

main()
