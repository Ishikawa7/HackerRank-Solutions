import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class JavaStaticInitializerBlock {

private static boolean flag;
private static int B;
private static int H;
static{
    Scanner s = new Scanner(System.in);
    B = Integer.parseInt(s.nextLine());
    H = Integer.parseInt(s.nextLine());
    if(B<=0 || H<=0){
        flag = false;
        System.out.println("java.lang.Exception: Breadth and height must be positive");
    }else{
        flag = true;
    }
}

public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
	}//end of main

}//end of class
