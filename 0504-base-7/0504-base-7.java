class Solution {
    public String convertToBase7(int num) {
        String sign = "";
        String ans = "";
        
        if(num == 0){
            return "0";
        }
        
        if(num < 0){
            sign = "-";
            num = Math.abs(num);
        }
        while(num != 0){
            ans = Integer.toString(num % 7) + ans ;
            num = (num / 7);

        }

        return sign + ans;
    }
}