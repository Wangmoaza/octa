def main():
    with open("test_input.csv") as f:
        l = f.readline()
        cnt = 0
        while True:
            l = f.readline().strip()
            
            if l == '':
                break
            cnt += 1
            print l
            print type(l)
            if cnt > 10:
                break

main()
