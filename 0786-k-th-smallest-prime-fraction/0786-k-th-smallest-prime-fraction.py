class Solution:
    def kthSmallestPrimeFraction(self, primes, k):
        left, right, num_primes = 0, 1, len(primes)
        while True:
            mid = (left + right) / 2
            fraction_indices = [bisect.bisect(primes, primes[i] / mid) for i in range(num_primes)]
            count = sum(num_primes - i for i in fraction_indices)
            if count > k:
                right = mid
            elif count < k:
                left = mid
            else:
                return max([(primes[i], primes[j]) for i, j in enumerate(fraction_indices) if j <num_primes], key=lambda x: x[0] / x[1])

        