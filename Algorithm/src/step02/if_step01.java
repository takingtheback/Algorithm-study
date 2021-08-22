package step02;

import java.util.Scanner;

/**
 * 문제
 * 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
 * 입력
 * 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
 * 출력
 * 첫째 줄에 다음 세 가지 중 하나를 출력한다.
 * A가 B보다 큰 경우에는 '>'를 출력한다.
 * A가 B보다 작은 경우에는 '<'를 출력한다.
 * A와 B가 같은 경우에는 '=='를 출력한다.
 * 제한
 * -10,000 ≤ A, B ≤ 10,000
 */
public class if_step01 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int A = scan.nextInt();
		int B = scan.nextInt();
		
		if ( A < -10000 || A > 10000) {
			System.out.println("a는 -10000보다 크거나 같아야하고, 10000보다 작거나 같아야함");
		}
		else if (B < -10000 || B > 10000) {
			System.out.println("b는 2보다 크거나 같아야하고, 100000보다 작거나 같아야함");
		}
		
		if(A > B) {
			System.out.println(">");
		}
		else if (A < B) {
			System.out.println("<");
		}
		else {
			System.out.println("==");
		}
	}	
}
