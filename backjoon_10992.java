import java.util.*;

// 별찍기 문제 10992
public class backjoon_10992 {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    int size = scan.nextInt();

    for (int i = 0; i < size; i++) {
      for (int j = 0; j < size * 2 - 1; j++) {
        if (j == size - i - 1) {
          System.out.print("*");
        } else if (j == size + (i - 1)) {
          System.out.print("*");
        } else if (i == size - 1) {
          System.out.print("*");
        } else if (j == size + i) {
          break;
        } else {
          System.out.print(" ");
        }
      }
      System.out.println("");
    }

    scan.close();
  }
}