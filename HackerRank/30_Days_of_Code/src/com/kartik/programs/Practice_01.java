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
public class Practice_01 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// JAVA STRING COMPARE
		
		/*
		 * Given a string, find out the lexicographically smallest and largest substring of length k.

		[Note: Lexicographic order is also known as alphabetic order dictionary order. So "ball" is smaller 
		than "cat", "dog" is smaller than "dorm". Capital letter always comes before smaller letter, so "Happy" 
		is smaller than "happy" and "Zoo" is smaller than "ball".]
		 * */
		
		Scanner sc=new Scanner(System.in);
        String inputString = sc.nextLine();
        int k=sc.nextInt();
   
        String max=inputString.substring(0,k);
        String min=inputString.substring(0,k);

        for(int i=0; i+k<=inputString.length(); i++){           
            if(inputString.substring(i, i+k).compareTo(min)<0) min=inputString.substring(i, i+k);
            if(inputString.substring(i, i+k).compareTo(max)>0) max=inputString.substring(i, i+k);
        }

        System.out.println(min);
        System.out.println(max);

	}

}
