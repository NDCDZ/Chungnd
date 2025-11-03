# Lab 2: Viết class MathUtil chứa các phương thức static isPrime, factorial, gcd
class MathUtil:
    @staticmethod
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

if __name__ == "__main__":
    print("isPrime(7):", MathUtil.isPrime(7))
    print("factorial(5):", MathUtil.factorial(5))
    print("gcd(24, 18):", MathUtil.gcd(24, 18))
