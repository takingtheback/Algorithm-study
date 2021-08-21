import java.util.Scanner;

public class AdivineB {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		int b = scan.nextInt();
		
		if ( a < 1 ) {
			System.out.println("a는 1보다 크거나 같아야함");
		}
		else if (b < 1) {
			System.out.println("b는 1보다 크거나 같아야함");
		}
		else {
			System.out.println(a+b);
			System.out.println(a-b);
			System.out.println(a*b);
			System.out.println(a/b);
			System.out.println(a%b);
		}
		
	}
}