import java.util.Scanner;
/**
 * BotSavesPrincess
 */
public class BotSavesPrincess {

    public static void main(String[] args) {
        Scanner scanner = new Scanner (System.in);
        //input
        int n = scanner.nextInt();
        scanner.nextLine();
        //actualy you need to read only the first and last row (4 corners)
        String input = scanner.nextLine();
        for(int i=1; i<n-1; i++){scanner.nextLine();}   //skip useless lines
        input = input + scanner.nextLine(); 

        String [] combinations = new String [2];
        //detect princess position and set the proper "zig-zag" combinations
        if (input.charAt(0) == 'p'){
            combinations[0] = "UP";
            combinations[1] = "LEFT";
        }
        else
        {
            if (input.charAt(n-1) == 'p'){
                combinations[0] = "UP";
                combinations[1] = "RIGHT";
            }
            else
            {
                if (input.charAt(n) == 'p'){
                    combinations[0] = "DOWN";
                    combinations[1] = "LEFT";
                }
                else
                {
                    combinations[0] = "DOWN";
                    combinations[1] = "RIGHT";
                }
            }
        }
        //move towards the princess
        for(int i=0;i<(n-1)/2;i++){
            System.out.println(combinations[0]);
            System.out.println(combinations[1]);
        }

        
        scanner.close();
    }
}