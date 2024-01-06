package _04_java_testNG.seleniumIntegration;

import org.openqa.selenium.chrome.ChromeDriver;

public class BaseClass {
  ChromeDriver driver;

  public void invokeBrowser() {
    driver = new ChromeDriver();
    driver.manage().window().maximize();
    driver.manage().deleteAllCookies();
    driver.get("https://test.qatechhub.com");
  }

  public String getTitleOfThePage() {
    String titleOfThePage = driver.getTitle();
    return titleOfThePage;
  }

  public void closeBrowser() {
    driver.quit();
  }
}
