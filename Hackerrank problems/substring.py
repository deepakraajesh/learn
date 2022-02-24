def count_substring(string, sub_string):
    result=0
    length=len(string)
    j=len(sub_string)
    for i in range (length):
        if(string[i:j]==sub_string):
            result +=1
        j+=1

    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)