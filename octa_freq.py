LARGENUM = 100000000

def parse(filePath):
    print("started")
    
    with open(filePath, "r") as fr:
        print "read file"
        line = fr.readline() # read first line (containing info)
        cnt = 0
        
        while True:
            line = fr.readline().strip()
            if line == '':
                break
            
            try:
                cnt += 1
                tokens = line.split(',')
                
                # validity check
                if len(tokens[5:]) != 65536:
                    continue
                
                octa = [int(i) for i in tokens[5:]]
                octa_freq = cal_freq(octa)
                write2file(octa_freq)

                if cnt % 1000 == 0:
                    print cnt 
            ### END - try
            except ValueError:
                continue
            ### END - except
        ### END - for line
    ### END - with

    print("fininsed")
### END - def parse

def write2file(octa_freq):
    with open("db3_octa_freq.csv", "a") as fw:
        string = ""
        for freq in octa_freq:
            string += str(freq) + ','

        string = string[:-1] + '\n'
        fw.write(string)
    ### END - with open
### END - def write2file

def cal_freq(cntList):
    total = sum(cntList)
    freqList = []
	
    for item in cntList:
	freqList.append(int((LARGENUM * item)/total))

    return freqList
### END - def cal_freq


def main():
    parse("8mer.csv")

main()
