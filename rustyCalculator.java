import java.util.Stack;


public class rustyCalculator {   
    public static String answer(String str) { 

        // Your code goes here.

    	    Stack<Character> stack = new Stack<Character>();
        String rpn = "";
        
        for(char c : str.toCharArray()) {
            switch(c) {
            case '+':
                // Better check if there is a higher order operation
                while(!stack.empty() && stack.peek() == '*') {
                    rpn+=stack.pop();
                }
                stack.push(c);
                break;
            case '*':
                stack.push(c);
                break;
            default:
                rpn+=c;
                break;
            }
        }
        
        //All done, let's get our remaining operators
        while(!stack.isEmpty())
            rpn+=stack.pop();
        return rpn;     
    }

     public static void main(String[] args) {
    	
    	System.out.println(answer("2*4*3+9*3+5"));
    } 
}
