class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        prod = 1
        su = 0
        for i in s:
            prod *= int(i)
            su += int(i)

        return (prod-su)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna