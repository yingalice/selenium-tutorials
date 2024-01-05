package _03_java_waits.pageLoadTimeout;

import java.time.Duration;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class Amazon {
  ChromeDriver driver;
  String url = "https://amazon.com";

  @BeforeClass
  public void invokeBrowser() {
    driver = new ChromeDriver();
    driver.manage().window().maximize();
    driver.manage().deleteAllCookies();
    // pageLoadTimeout - Time to wait for page to load
    driver.manage().timeouts().pageLoadTimeout(Duration.ofSeconds(60));
    driver.get(url);
  }

  @Test
  public void verifyTitleOfHomePage() {
    // Solve captcha manually
    try {
      TimeUnit.SECONDS.sleep(5);
    } catch (InterruptedException e) {
      System.out.println(e);
    }
    String actualTitle = driver.getTitle();
    String expectedTitle = "Amazon.com. Spend less. Smile more.";
    Assert.assertEquals(actualTitle, expectedTitle);
  }

  @AfterClass
  public void closeBrowser() {
    driver.quit();
  }
}