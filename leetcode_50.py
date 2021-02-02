class Solution:
    # def myPow(self, x: float, n: int) -> float:
    #     return x ** n

    # def myPow(self, x: float, n: int) -> float:
    #     if n == 0:
    #         return 1
    #     elif n < 0:
    #         return 1 / self.myPow(x, -n)
    #     else:
    #         if n % 2 == 0:
    #             return self.myPow(x * x, n // 2)
    #         else:
    #             return x * self.myPow(x, n - 1)
    

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow
    


if __name__ == '__main__':
    print(Solution().myPow(2, 5))