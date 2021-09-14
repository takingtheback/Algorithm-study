package Programmers;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
		
		int len = scan.nextInt();
		
		for(int i = 1; i <= len; i++) {
			int a = scan.nextInt();
			int b = scan.nextInt();
			System.out.println("Case #" + i + ": " + (a+b));
		}
	}
}