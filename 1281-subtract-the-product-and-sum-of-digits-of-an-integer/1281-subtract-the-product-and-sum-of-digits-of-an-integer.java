class Solution {
    public int subtractProductAndSum(int n) {
        String s = Integer.toString(n);
        int prod = 1;
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
           int digit = s.charAt(i) - '0';

            prod = prod * digit;
            sum = sum + digit;
        }
        return (prod - sum);
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna