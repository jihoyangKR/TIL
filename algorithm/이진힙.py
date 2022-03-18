# data = [69, 10, 30, 2, 16, 8, 31, 12]

H = [0] * 100
hsize = 0 # 초기값은 0

def pop():
    # empty --> hsize == 0 비어있는지 아닌지 먼저 체크하고 pop을 하는게 좋다.
    global hsize
    ret = H[1]
    H[1] = H[hsize]
    hsize -= 1

    p, c = 1, 2 # c : 왼쪽자식

    while c <= hsize: # 왼쪽자식부터 check
        if c + 1 <= hsize and H[c] < H[c + 1]: #오른쪽이 존재하고 오른쪽 자식이 더 크면
            c += 1 # c는 오른쪽을 가리킨다.
        if H[p] >= H[c]: # 부모가 자식보다 크거나 같으면 그대로 두고
            break
        H[p], H[c] = H[c], H[p] # 그렇지 않으면 부모와 자식을 바꾼다.
        p = c # 다음 비교를 위해 자식인덱스가 부모 인덱스가 되고
        c = p * 2 # 부모 인덱스 * 2 한 값이 왼쪽 자식 인덱스로 만들어주면 된다.

    return ret

def empty():
    return hsize == 0

data = [69, 10, 30, 2, 16, 8, 31, 12]

for val in data:

