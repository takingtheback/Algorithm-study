import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
		
		int H = scan.nextInt();
		int M = scan.nextInt();
		scan.close();
		
		if ( H < 0 || H > 23) {
			System.out.println("H는 0보다 크거나 같아야하고, 23보다 작거나 같아야함");
		} else if (M < 0 || M > 59) {
			System.out.println("M는 0보다 크거나 같아야하고, 59보다 작거나 같아야함");
		} else {
			int MM = M - 45;
								
			if (MM >= 0) {
				System.out.println(H + " " + MM);
			} else {
				if (H > 0) {
					System.out.println((H-1) + " " + (60 + MM));
				} else {
					System.out.println("23 " + (60 + MM));
				}
			}
			
			
		}
	}
}
