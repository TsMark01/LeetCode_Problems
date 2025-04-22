class Solution(object):
    def plusOne(self, digits):
        str_dg = ''
        result_list = []

        for i in digits:
            str_dg += str(i)

        int_dg = int(str_dg)
        result_digit = int_dg + 1

        for i in str(result_digit):
            result_list.append(int(i))
        print(result_list)
        return result_list