# python3

def parallel_processing(n, m, data):
    output = []
    workers= [0]*n
    for job in data:
        for i in range(1,n):
            if workers[i]<workers[i-1]:
                s_index = i
            else:
                s_index = i-1
        output.append((s_index,workers[s_index]))
        workers[s_index]+=job

    return output

def main():

    print("Input: ")
    inp = list(map(int, input().split()))
    n=inp[0]
    m=inp[1]
    data = list(map(int, input().split()))
    

    assert len(data) == m
    result = parallel_processing(n,m,data)
    
    for i, j in result:
        print(i, j)



if __name__ == "__main__":
    main()
