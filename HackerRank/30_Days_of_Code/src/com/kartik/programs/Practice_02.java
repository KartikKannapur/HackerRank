/**
 * 
 */
package com.kartik.programs;

import java.util.Scanner;

/**
 * @author Kartik Kannapur
 *
 */
public class Practice_02 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// Given a string , print "Yes" if it is a palindrome, print "No" otherwise. 
		//The strings will consist lower case english letters only. The strings will have at most 50 characters.
		
		
		Scanner sc=new Scanner(System.in);
        String inputString = sc.nextLine();
        
        String reversedString = "";
        for (int i = inputString.length()-1; i >= 0; i--) {
//			System.out.println(inputString.charAt(i));
			reversedString += inputString.charAt(i);
		}
        
        if (inputString.equals(reversedString)) {
			System.out.println("Yes");
		}
        else {
			System.out.println("No");
        }
	}

}
