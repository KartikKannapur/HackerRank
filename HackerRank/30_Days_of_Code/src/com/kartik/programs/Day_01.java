/**
 * 
 */
package com.kartik.programs;

import java.util.Scanner;

/**
 * @author Kartik Kannapur
 *
 */
public class Day_01 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int i = 4;
		double d = 4.0;
		String s = "HackerRank";
		
		Scanner scan = new Scanner(System.in);
		int firstNumber = scan.nextInt();
		double secondNumber = scan.nextDouble();
		String tempString = scan.nextLine();
		String inputString = scan.nextLine();
		scan.close();
	      
		System.out.println(i + firstNumber);
		System.out.println(d + secondNumber);
		System.out.println(s + inputString.toString());
		

	}

}
