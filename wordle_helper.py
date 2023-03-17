import timeit


def contains_letters(letters):
    L = []
    for i in letters:
        L.append(i.lower())
    print(L)
    cnt = 0
    with open('wordle.txt') as fp:
        line = fp.readline()
        while line:
            # [1] and L[1] in line[2] and L[2] in line[3] and L[3] in line[4]:
            if L[0] in line and L[1] in line and L[2] in line:
                print(line)
                cnt += 1
            line = fp.readline()
    print(cnt)

# opens the text of all possible 5 letter words
# loads that into a list L and returns the list


def load_wordle():
    L = []
    with open('wordle.txt') as fp:
        line = fp.readline()
        if len(line.strip()) == 5:
            L.append(line.strip())
        while line:
            line = fp.readline()
            if len(line.strip()) == 5:
                L.append(line.strip())
    i = 0
    for word in L:
        if len(word) != 5:
            print("Hey Hey Hey ")
            print(f"word is <{word}> index = {i} length of L = {len(L)}")
        i = i + 1

    return L


def dwindle(alpha, L):
    tmp_L = []
    i = 0
    for i in L:
        if alpha in i:
            pass
        else:
            tmp_L.append(i)

    return tmp_L


def first_dwindle(missed, L):

    for i in missed:
        L = dwindle(i, L)
    return L


def includers(alpha, L):
    tmp_L = []
    for i in L:
        if alpha in i:
            tmp_L.append(i)
        else:
            pass
    return tmp_L


def first_includers(adds, L):
    for i in adds:
        L = includers(i, L)
    return L


def end_in(alpha, L):
    tmp_l = []
    for i in L:
        if i[4] == alpha:
            tmp_l.append(i)
    return tmp_l


def location_letters(alpha, loc, L):
    tmp_L = []
    for i in L:
        if alpha == i[loc-1]:
            tmp_L.append(i)

    return tmp_L


def non_location_letter(alpha, loc, L):
    tmp_L = []
    for i in L:
        # print(f"i = {i} and type of i = {type(i)}")
        if alpha in i:
            if alpha == i[loc - 1]:
                pass
            else:
                tmp_L.append(i)
    return tmp_L


def letter_count(L):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_dict = {}
    total = len(L)
    for i in alphabet:
        count = 0
        for j in L:
            if i in j:
                count += 1
        # print(f"{i} appeard in {count} words which is {count/total}")
        alphabet_dict[i] = round(count/total, 5)

    # print(alphabet_dict)
    return alphabet_dict


def print_word_list(L):
    i = 1
    for word in L:
        if (i % 9) != 0:
            print(f"{word}\t", end='')
        else:
            print(word)
        i = i+1

    print(f"\n # of words= {len(L)}")


def choices():
    print("Enter your choice:\n")
    print("1 - Enter letters that have been excluded.")
    print("2 - Enter a letter in the wrong location (a,2).")
    print("3 - Enter a letter in the correct location (t,1).")
    print("4 - Exit")
    print()

    # respnose wil be a string type 'str'
    response = input()
    # print(type(response))

    if response not in "1234":
        print("Invalid response.")
        return 0
    else:
        return response


alphabet = 'abcdefghijklmnopqrstuvwxyz'


def enter_excluded_letters():
    print("Enter the letter(s) to exclude")
    ex_let = input()
    response = ''

    for letter in ex_let:
        if letter.lower() in alphabet:
            response = response + letter.lower()
    return response


def wrong_let_loc():
    print("Enter the correct letter:")
    letter = input()
    print(f"Enter the invalid location of {letter}: ")
    print("1 2 3 4 5")
    print("_ _ _ _ _")
    wrong_location = int(input())
    # print(type(wrong_location))

    return [letter, wrong_location]


def correct_let_loc():
    print("Enter the correct letter:")
    letter = input()
    print(f"Enter the correct location of {letter}: ")
    print("1 2 3 4 5")
    print("_ _ _ _ _")

    correct_location = int(input())
    # print(type(correct_location))

    return [letter, correct_location]


def main():
    print("Welcome to Wordle helper!")

    # st = timeit.default_timer()
    # ft = timeit.default_timer() - st
    valid = True
    L = load_wordle()

    while valid:
        response = choices()
        if response == '1':
            # print("selected 1")
            ex_let = enter_excluded_letters()
            # print(ex_let)
            # "cnstompu"
            L = first_dwindle(ex_let, L)
        elif response == '2':
            # print('Selected 2')
            pair = wrong_let_loc()
            # print(pair)
            L = non_location_letter(pair[0], pair[1], L)

        elif response == '3':
            # print('Selected 3')
            pair = correct_let_loc()
            # print(pair)
            L = location_letters(pair[0], pair[1], L)
        elif response == 0 or response == '4':
            valid = False

        print_word_list(L)


if __name__ == '__main__':
    main()
