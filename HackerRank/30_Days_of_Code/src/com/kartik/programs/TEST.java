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
        int N=sc.nextInt();
        
        System.out.println(inputString);
        System.out.println(N);    
        
        ArrayList arr_combo = new ArrayList();
        
        for (int i = 0; i < inputString.length()-2; i++) {
//			System.out.println(inputString.substring(i,i+3));
			arr_combo.add(inputString.substring(i,i+3));
		}
        
//        System.out.println(arr_combo.size());
        
        
        int k = N;
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