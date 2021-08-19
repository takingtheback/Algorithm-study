
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println(solution("JAN"));
	}

	
	  public static int solution(String name) {
		    int answer = 0;
		      int len = name.length();

		      // 제일 짧은 좌, 우 이동은 그냥 맨 오른쪽으로 이동할 때
		      int min = len - 1;

		      for (int i = 0; i < len; i++) {
		        // 조이스틱 상, 하 이동
		        char c = name.charAt(i);
		        int mov = (c - 'A' < 'Z' - c + 1) ? (c - 'A') : ('Z' - c + 1);
		        answer += mov;

		        // 조이스틱 좌, 우 이동
		        int nextIndex = i + 1;
		        // 다음 단어가 A이고, 단어가 끝나기 전까지 nextIndex 증가
		        while (nextIndex < len && name.charAt(nextIndex) == 'A')
		          nextIndex++;

		        min = Math.min(min, (i * 2) + len - nextIndex);
		      }

		      answer += min;
		      return answer;
		    }
}
