import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
/**
 * JavaCurrencyFormatter
 */
public class JavaCurrencyFormatter {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();

        NumberFormat nF = NumberFormat.getCurrencyInstance();
  
        nF.setCurrency(Currency.getInstance(Locale.US)); 
  
        //String us = nF.getCurrency().getDisplayName(); 
        
        //System.out.println("US: " + us);
        //System.out.println("India: " + india);
        //System.out.println("China: " + china);
        //System.out.println("France: " + france);
    }
}