#                                                                Урок 1
# множество - список только уикальных значений aaabcd -> abcd

# def strcounter(s):
#     for symbol in set(s):
#         count = 0
#         for sub_sumbol in s:
#             if symbol == sub_sumbol:
#                 count+=1
#         print(symbol,count)

# strcounter('aabcd')


def strcounter(s): #O(2N)->O(N)
    syms_counter ={}
    for symbol in s:
        syms_counter[symbol] = syms_counter.get(symbol,0)+1

    for symbol,count in syms_counter.items():
        print(symbol, count)

strcounter('dfhdsuhfjksf')



# ghfgh