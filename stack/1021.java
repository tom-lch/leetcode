//使用java实现
//在下一个版本中使用栈来实现

class Solution {
    public String removeOuterParentheses(String S) {
        int start = 0;
        int index = 0;
        StringBuilder sub = new StringBuilder();
        for(int i=0; i < S.length(); i++){
            if (S.charAt(i) == '('){
                start++;
            }
            if (S.charAt(i) == ')'){
                start--;
            }
            if (S.charAt(i) == '(' && start ==1){
                index = i;
            }
            if (start == 0){
                sub.append(S.substring(index+1, i));
            }
        }
        return sub.toString();
    }
}