from typing import List


class Solution:
    def computeLPSArray(sel, arr):
        lps = [0] * len(arr)

        curr_index = 1
        length = 0

        while curr_index < (len(arr)):
            if arr[curr_index] == arr[length]:
                length += 1
                lps[curr_index] = length
                curr_index +=1

            else:
                if length > 0:
                    length = lps[length-1]
                else:
                    curr_index +=1

        return lps

    def is_substring(self, arr, sub, lps):
        main_index = sub_index = 0
        while main_index < len(arr):
            if arr[main_index] == sub[sub_index]:
                if sub_index == len(sub) -1:
                    return True
                main_index +=1
                sub_index +=1
            else:
                if sub_index > 0:
                    sub_index = lps[sub_index -1]
                else:
                    main_index +=1
        return False

    def stringMatching(self, words: List[str]) -> List[str]:
        matching_words = []
        for index, word in enumerate(words):
            lps = self.computeLPSArray(word)
            for index_other, other_words in enumerate(words):
                if index == index_other:
                    continue
                if self.is_substring(other_words, word, lps):
                    matching_words.append(word)
                    break

        return matching_words




if __name__ == '__main__':
    print(Solution().computeLPSArray('ababca'))