

from collections import Counter


def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

print(is_anagram("ana", "aan"))
print(is_anagram("banana", "anbnaa"))
print(is_anagram("banaaa", "anbnaa"))