package stpe03;

import java.util.Scanner;

/**
 * 문제 8393	합
 * n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
 * 입력
 * 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
 * 출력
 * 1부터 n까지 합을 출력한다.
 */
public class No8393 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		scan.close();
		int result = 0;
		
		for(int i = 1; i <= n; i++) {
			result += i;
		}
		System.out.println(result);
	}
}
