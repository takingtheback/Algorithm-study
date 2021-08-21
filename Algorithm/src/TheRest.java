import java.util.Scanner;

public class TheRest {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int A = scan.nextInt();
		int B = scan.nextInt();
		int C = scan.nextInt();
		
		if ( A < 2 || A > 100000) {
			System.out.println("a는 2보다 크거나 같아야하고, 100000보다 작거나 같아야함");
		}
		else if (B < 2 || B > 100000) {
			System.out.println("b는 2보다 크거나 같아야하고, 100000보다 작거나 같아야함");
		}
		else if (C < 2 || C > 100000) {
			System.out.println("c는 2보다 크거나 같아야하고, 100000보다 작거나 같아야함");
		}
		else {
			System.out.println((A+B)%C);
			System.out.println(((A%C) + (B%C))%C);
			System.out.println((A*B)%C);
			System.out.println(((A%C) * (B%C))%C);
		}
		
	}
}