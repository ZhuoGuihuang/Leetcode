class Solution:
# @return an integer
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                print(dividend)
                # i是除数增加的倍数 加上i就是已经减去的多少倍
                res += i
                print(res)
                i <<= 1
                print(i)
                # temp增加倍数再去减
                temp <<= 1
                print(temp)
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


a = Solution
print(a.divide(a,7, 2))
print('ok')