/**
 * 
 */
package com.kartik.programs;

import java.util.Scanner;

/**
 * @author Kartik Kannapur
 *
 */
public class Day_03 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		double mealCost = scan.nextDouble();
		int tipPercent = scan.nextInt();
		int taxPercent = scan.nextInt();
		
		scan.close();
	      
		
//		System.out.println(mealCost);
//		System.out.println(tipPercent);
//		System.out.println(taxPercent);
		
		double totalCost = ((100 + tipPercent + taxPercent)*mealCost)/100;
		
		System.out.println("The total meal cost is " + Math.round(totalCost) + " dollars.");

	}

}
