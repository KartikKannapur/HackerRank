import zlib
import binascii
import nltk

b_comp_str_1 = "789c030000000001"
b_comp_str = zlib.decompress(binascii.unhexlify(b_comp_str_1))



b = zlib.decompress(binascii.unhexlify(b_comp_str))
c = binascii.unhexlify(b)
words_list = (zlib.decompress(c)).split("\n")

def TagSegmenter(input_word):
    arr_valid_words = []
    for N in range(2, len(input_word)):
        for i in range(len(input_word)-N+1):
            if input_word[i:i+N] in words_list:
                arr_valid_words.append(input_word[i:i+N])

    arr_valid_words

    arr_valid_sub_words = []
    arr_vallid_sub_words_2 = []
    def my_func(var_word, var_arr, var_sub_word):
        arr_vallid_sub_words_2.append(var_sub_word)
    #     if [i for i in var_arr if i[0] == var_word[:1]]:
    #         if [i for i in var_arr if i[0] == var_word[:1] if i in input_word] not in arr_valid_sub_words:
    #             arr_valid_sub_words.append([i for i in var_arr if i[0] == var_word[:1] if i in input_word])

        for i in [i for i in var_arr if i[0] == var_word[:1]]:
            if var_word.replace(i, "") != var_word:
                my_func(var_word.replace(i, ""), arr_valid_words, i )
            else:
                break

    my_func(input_word, arr_valid_words, "")

    # print arr_valid_sub_words
    # print arr_vallid_sub_words_2

    arr_valid_output = []
    import itertools
    for i in list(itertools.combinations_with_replacement(arr_vallid_sub_words_2,4)):
    #     print "".join(list(i))
        if "".join(list(i)) == input_word:
    #         print " ".join(list(i)).lstrip()
            arr_valid_output.append(" ".join(list(i)).lstrip())
    if arr_valid_output:
        print arr_valid_output[0]
    else:
        print "No Output"
        
#TagSegmenter("wearethepeople")

N = int(raw_input())

for i in range(0, N):
	TagSegmenter(raw_input())