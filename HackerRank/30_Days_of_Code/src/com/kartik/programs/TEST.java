/**
 * 
 */
package com.kartik.programs;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * @author Kartik Kannapur
 *
 */
public class TEST {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
        String inputString = sc.nextLine();
        
        String reversedString = "";
        for (int i = inputString.length()-1; i >= 0; i--) {
//			System.out.println(inputString.charAt(i));
			reversedString += inputString.charAt(i);
		}
        
//        inputString.
        
        if (inputString.equals(reversedString)) {
			System.out.println("Yes");
		}
        else {
			System.out.println("No");
		}
        

	}
}
 
