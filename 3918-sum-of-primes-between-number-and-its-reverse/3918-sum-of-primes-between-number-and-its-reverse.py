class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        s = str(n)
        reverse = ""
        su = 0
        for i in range(len(s)-1,-1,-1):
            reverse += s[i]
        rn = int(reverse)
        
        sm = n if n < rn else rn
        bi = n if n > rn else rn

        for j in range(sm, bi + 1):

            if j < 2:
                continue

            prime = True

            for k in range(2, int(j ** 0.5) + 1):
                if j % k == 0:
                    prime = False
                    break

            if prime:
                su += j
                    

        return su