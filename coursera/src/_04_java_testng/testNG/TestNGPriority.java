package _04_java_testNG.testNG;

import org.testng.annotations.Test;

public class TestNGPriority {
  @Test (priority = 0)
  public void testcase1() {
    System.out.println("Test case 1");
  }

  @Test (priority = 100)
  public void testcase4() {
    System.out.println("Test case 4");
  }

  @Test (priority = -100)
  public void testcase2() {
    System.out.println("Test case 2");
  }

  @Test (priority = 200)
  public void testcase5() {
    System.out.println("Test case 5");
  }
}
