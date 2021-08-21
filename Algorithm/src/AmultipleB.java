import java.util.Scanner;

public class AmultipleB {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		int b = scan.nextInt();
		
		if ( a <= 0 ) {
			System.out.println("a는 0보다 커야함");
		}
		else if (b <= 0) {
			System.out.println("b는 0보다 커야함");
		}
		else {
			int result = a * b;
			System.out.println(result);
		}
		
	}
}