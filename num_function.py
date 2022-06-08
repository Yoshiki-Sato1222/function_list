import itertools

#特定の数字が入っているかの判定
def search(num,search_num):

    flag = 0

    num_list = [int(num_1) for num_1 in str(num)]

    for i in num_list:
        if i == search_num:
            flag = 1
            break
        else:
            pass

    if flag == 1:
        return True
    else:
        return False


#素数検索(エラトステネスの篩)<set>
def prime(num):
    N = [True for i in range(num+1)]
    N[0],N[1] = False,False
    

    for i in range(2,int(num ** 0.5) + 1):
        if N[i] == True:
            for j in range(i * 2,num+1,i):
                N[j] = False
    
    prime_list = set(i for i,v in enumerate(N) if v == True)

    return prime_list


#素数判定
def prime_check(num):
    flag = 0

    for i in range(2,num):
        if i * i > num:
            break

        if num % i == 0:
            flag = 1
            break
        else:
            pass

    if flag == 1:
        return False
    else:
        return True


#特定の数字がリスト内にあるかの検索しインデックスを返す<set>
def search_list(list_1,num):

    idx = set(i for i,v in enumerate(list_1) if v == num)

    return idx


#重複を許さない組み合わせnCrの取り方(r = 3)
def comb_list(list):
    ans_list = []
    for i,j,k in itertools.combinations(list,3):
        ans_list.append([i,j,k])
    
    return ans_list


    
if __name__ == '__main__':
    
    #適当な数
    num = int(input())
    #探したい数
    search_num = int(input())

    if search(num,search_num):
        print("Yes")
    else: 
        print("No")


print(prime(num))

if prime_check(num):
    print("prime number")
else:
    print("Not prime number")

test_list = [i for i in reversed(range(num+1))]
print(search_list(test_list,search_num))