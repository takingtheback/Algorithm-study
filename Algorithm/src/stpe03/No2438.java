package stpe03;

import java.util.Scanner;

public class No2438 {
	/**
	 * 문제
	 * 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
	 * 입력
	 * 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
	 * 출력
	 * 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
	 */
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
			
			int len = scan.nextInt();
			
			for(int i = 1; i <= len; i++) {
				for(int j = 0; j < i; j++) {
				System.out.print("*");
			}
				System.out.println("");
		}
	}
}
