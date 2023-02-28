def count_vowels(input):
    li=list(input)
    li=list(filter(lambda x: x=='a' or x=='e' or x=='i' or x=='o' or x=='u' , li))
    print(len(li))
    return

count_vowels('apple') #=> 2
count_vowels('banana') #=> 3