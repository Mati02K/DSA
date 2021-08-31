# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# My Version of merge sort
# from util import time_it
# @time_it
# def longestPalindrome(s):
#     if len(s)==0:
#         return 
#     temp = ''
#     pali = ''
#     i = j = 0
#     while (i<len(s)-1):
#         temp = temp + s[i]
#         j = i + 1
#         while (j<len(s)):
#             temp = temp + s[j]
#             j+=1
#             if temp[::-1] == temp and len(temp) > len(pali):
#                 pali = temp[::-1]
#         temp = ''
#         i+=1
#         j=0
#     if len(pali)==0:
#         pali = s[0]
            
            
                
#     return pali

# def helper(s, l, r):
#     while l >= 0 and r < len(s) and s[l] == s[r]:
#         l -= 1; r += 1
#     return s[l+1:r]
# @time_it
# def longestPalindrome2(s):
#     res = ""
#     for i in range(len(s)):
#         # odd case, like "aba"
#         tmp = helper(s, i, i)
#         if len(tmp) > len(res):
#             res = tmp
#         # even case, like "abba"
#         tmp = helper(s, i, i+1)
#         if len(tmp) > len(res):
#             res = tmp
#     return res


def romantonum(s):
    romanlist = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
    value = 0
    prev = 0
    for i in s[::-1]:
        if romanlist[i] >= prev:
            value+=romanlist[i]
        else:
            value-= romanlist[i]
        prev = romanlist[i]
    return value
if __name__ == '__main__':
    # print(longestPalindrome("jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn"))
    # print(longestPalindrome2("jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn"))
    print(romantonum('IV'))