def file_to_list_strings(FileName):

    list_lines = []

    with open(FileName, 'r') as F:

        for line in F:
            s1 = line.rstrip('\n')
            s2 = s1.rstrip('\r')
            s2 = s2.lower()
            list_lines.append(s2)

        return list_lines


def list_strings_to_list_words(list_strings):

    string_words = ''

    alpha = 'abcdefghijklmnopqrstuvwxyz'



    for line in list_strings:

        line.lower()

        for character in line:

            if  character in alpha:

                string_words = string_words + character

            else:

                string_words = string_words + " "

        string_words = string_words + " "

    return string_words.split()


def list_words_to_dic_words(list_words):

    dic_words = {}

    for word in list_words:

        if word in dic_words:

            dic_words[word] += 1

        else:
            dic_words[word] = 1

    return dic_words




def find_palindromes(dic_words):

    dic_palindromes = {}

    list_keys = dic_words.keys()
    list_keys.sort()

    for key in list_keys:
        string = ''


        for letter in key:

            string = letter + string


        if string == key and len(string) > 2:

            dic_palindromes[key] = 1

    return dic_palindromes
