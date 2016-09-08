import numpy as np

def parse(filePath):
    project_uid = []  # col 0
    ncbi_name = []  # col 2
    taxon_name = []  # col 3
    taxonomy = []  # col 4
    octa = [] # col 5 - 65540
    index = []
    with open(filePath) as f:
        #f.readline() # read first line (containing info)
        cnt = 0
        for i in range(24001, 48494):
            try:
                line = f.readline()
                cnt += 1
                tokens = line.strip().split(',')
                
                if len(tokens[5:]) != 65536:
                    continue
                
                octa.append([int(i) for i in tokens[5:]])
                index.append(cnt-1)
                project_uid.append(tokens[0])
                ncbi_name.append(tokens[2])
                taxonomy.append(tokens[4])
                
                if cnt % 1000 == 0:
                    print cnt 
            ### END - try
            except ValueError:
                continue
                
            ### END - except
        ### END - for line
    ### END - with
    
    #octa        = np.asarray(octa)
    #project_uid = np.asarray(project_uid)
    #ncbi_name   = np.asarray(ncbi_name)
    #taxonomy    = np.asarray(taxonomy)

    np.save('db3_project_uid_2', project_uid)
    np.save('db3_ncbi_name_2', ncbi_name)
    np.save('db3_taxonomy_2', taxonomy)
    np.save('db3_octa_2', octa)
    
    #print project_uid.shape
    #print octa.shape
### END - def parse hylumNames = getTopPhylumList(taxons)

def main():
    parse('../8mer.csv')

main()
