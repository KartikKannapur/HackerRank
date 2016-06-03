/**
 * 
 */
package com.kartik.programs;

import java.util.Scanner;

/**
 * @author Kartik Kannapur
 *
 */
public class Day_07 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] arr = new int[n];
        for(int i=0; i < n; i++){
            arr[i] = in.nextInt();
        }
        for(int j=0; j<arr.length;j++){
            System.out.print(arr[arr.length-j-1] + " ");
        }
        
        in.close();

	}

}
