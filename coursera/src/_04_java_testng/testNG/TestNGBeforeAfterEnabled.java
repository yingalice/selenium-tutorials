package _04_java_testNG.testNG;

import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class TestNGBeforeAfterEnabled {
  @Test
  public void testcase1() {
    System.out.println("@Test 1st Test Case");
  }

  @Test (enabled = false)
  public void testcase2() {
    System.out.println("@Test 2nd Test Case");
  }

  @Test
  public void testcase3() {
    System.out.println("@Test 3rd Test Case");
  }

  @BeforeMethod
  public void setup() {
    // Example: Login to app
    System.out.println("@BeforeMethod Before every test case");
  }

  @AfterMethod
  public void teardown() {
    // Example: Logout from app
    System.out.println("@AfterMethod After every test case");
  }

  @BeforeClass
  public void preSetup() {
    // Example: Invoke browser, set browser settings, initialize report
    System.out.println("@BeforeClass First statement to execute in this class");
  }

  @AfterClass
  public void postCleanup() {
    // Example: Close browser, stop report
    System.out.println("@AfterClass Last statement to execute in this class");
  }
}