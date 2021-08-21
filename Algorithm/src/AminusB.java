import java.util.Scanner;

public class AminusB {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		int b = scan.nextInt();
		
		if ( a <= 0 || a >= 10 ) {
			System.out.println("a 범위초과");
		}
		else if (b <= 0 || b >= 10) {
			System.out.println("b 범위초과");
		}
		else {
			int result = a - b;
			System.out.println(result);
		}
		
	}
}