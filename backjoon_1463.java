import java.util.*;

// DP_1로 나누기 문제
public class backjoon_1463 {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    int x = input.nextInt();
    int[] xArr = new int[x + 1];
    xArr[0] = xArr[1] = 0;

    for (int i = 2; i <= x; i++) {

      xArr[i] = xArr[i - 1] + 1;

      if (i % 3 == 0) {
        if (xArr[i] > xArr[i / 3] + 1) {
          xArr[i] = xArr[i / 3] + 1;
        }
      }
      if (i % 2 == 0) {
        if (xArr[i] > xArr[i / 2] + 1) {
          xArr[i] = xArr[i / 2] + 1;
        }
      }
    }
    System.out.println(xArr[x]);
    input.close();
  }
}