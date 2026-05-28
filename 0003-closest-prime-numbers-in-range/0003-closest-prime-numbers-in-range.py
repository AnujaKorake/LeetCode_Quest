class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = [True] * (right + 1)
        isPrime[0] = False
        isPrime[1] = False

        for i in range(2,int(right**0.5)+1):
            if isPrime[i]:
                for j in range(i*i,right+1,i):
                    isPrime[j] = False

        primes = []
        for num in range(left, right+1):
            if isPrime[num]:
                primes.append(num)

        if len(primes) < 2:
            return [-1, -1]

        minDiff = float('inf')
        ans = [-1, -1]

        for i in range(1, len(primes)):
            diff = primes[i] - primes[i-1]

            if diff < minDiff:
                minDiff = diff
                ans = [primes[i-1], primes[i]]


        return ans



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna