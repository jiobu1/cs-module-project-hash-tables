def no_dups(s):
    # Your code here
    words = s.split()
    unique = []
    for word in words:
        if (s.count(word)>1 and (word not in unique)or s.count(word)==1):
            unique.append(word)


    return " ".join(unique)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))