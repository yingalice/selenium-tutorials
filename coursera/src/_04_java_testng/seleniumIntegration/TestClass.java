package _04_java_testNG.seleniumIntegration;

import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class TestClass {
  BaseClass base = new BaseClass();

  @BeforeClass
  public void setup() {
    base.invokeBrowser();
  }

  @AfterClass
  public void teardown() {
    base.closeBrowser();
  }

  // Test case must have at least 1 Assert statement, 
  // otherwise it's considered bogus, because it would never fail
  @Test
  public void verifyTitleOfThePage() {
    String titleOfThePage = base.getTitleOfThePage();
    String expectedTitle = "Test QA Tech Hub – Learning By Doing is the best way to learn!";
    Assert.assertEquals(titleOfThePage, expectedTitle);
    // System.out.println("Title of the page is: " + titleOfThePage);
  }

  // Reports include:
  // - console
  // - Eclipse format
  // - XML (Eclipse: refresh to get test-output folder.  testng-results.xml)
  // - HTML (Eclipse: refresh to get test-output folder.  emailable-report.html)
}
