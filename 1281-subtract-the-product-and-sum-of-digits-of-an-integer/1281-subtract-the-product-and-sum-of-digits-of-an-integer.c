int subtractProductAndSum(int n) {
    int prod = 1;
    int sum =0;

    while(n > 0){
        int digit = n % 10 ;
        
        prod = prod * digit ;
        sum = sum + digit;

        n = n/10;
    }
    return prod-sum;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna