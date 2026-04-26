class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for ele in strs:
            result += str(len(ele)) + "_" + ele
        # print(result)
        return result

    def decode(self, s: str) -> List[str]:

        length, decode_lst, i = "", [], 0
        while i < len(s): 
            if s[i] == '_':
                # print(length)
                length = int(length)
                decode_lst.append(s[i+1 : i+1+length])
                # print(decode_lst)
                i += length
                length = ""
            else:
                length += s[i]
            i += 1
        return decode_lst
