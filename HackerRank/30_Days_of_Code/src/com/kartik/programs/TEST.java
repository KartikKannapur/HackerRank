/**
 * 
 */
package com.kartik.programs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

/**
 * @author Kartik Kannapur
 *
 */


class A{
	  static class B{}
	  static class C{ B b;
	    C(B b){this.b=b;}
	    int foo(){return 42;}
	  }
	}


public class TEST {

	/**
	 * @param args
	 */
	
//	public static String[] var_strings={" Hello " , "This " , "is ", "Sorting ", "Example"};
	
	
	public static void main(String[] args) {
		A.C n = new A.C(null);
		System.out.println(n.foo()==42);
		
		
//		String[] strings = { "x", "a", "b", "k" };
//		Arrays.sort(strings);
//		System.out.println(Arrays.toString(strings));
		

	}
}
 
