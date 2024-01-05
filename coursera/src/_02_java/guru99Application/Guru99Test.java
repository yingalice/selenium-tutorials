package _02_java.guru99Application;

import java.time.Duration;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class Guru99Test {
  ChromeDriver driver;
  WebDriverWait wait;
  String url = "http://demo.guru99.com/v4";
  
  @BeforeTest
  public void invokeBrowser() {
    driver = new ChromeDriver();
    wait = new WebDriverWait(driver, Duration.ofSeconds(5));
    driver.manage().window().maximize();
    driver.get(url);
  }

  @Test(priority = 0)
  public void dismissCookies() {
    wait.until(ExpectedConditions.frameToBeAvailableAndSwitchToIt(By.id("ccpa-consent-notice")));
    wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("close"))).click();
    driver.switchTo().defaultContent();
  }

  @Test(priority = 100)
  public void verifyTitleOfThePage() {
    String actualTitle = driver.getTitle();
    String expectedTitle = "Guru99 Bank Home Page";
    Assert.assertEquals(actualTitle, expectedTitle);
  }

  @Test(priority = 200)
  public void verifyLoginToGuru99Application() {
    WebElement userId = driver.findElement(By.name("uid"));
    WebElement userPassword = driver.findElement(By.name("password"));
    WebElement loginButton = driver.findElement(By.name("btnLogin"));

    userId.sendKeys("mngr546003");
    userPassword.sendKeys("bEhYrAs");
    loginButton.click();

    String expectedTitle = "Guru99 Bank Manager HomePage";
    wait.until(ExpectedConditions.titleIs(expectedTitle));
    Assert.assertEquals(expectedTitle, driver.getTitle());
  }

  @Test(priority = 300)
  public void addCustomer() {
    driver.findElement(By.linkText("New Customer")).click();
    driver.findElement(By.name("name")).sendKeys("Alice Ying");
    driver.findElement(By.xpath("//input[@value='f']")).click();
    driver.findElement(By.name("dob")).sendKeys("01/01/2000");
    driver.findElement(By.name("addr")).sendKeys("123 Main Street\nSuite 301B");
    driver.findElement(By.name("city")).sendKeys("Pleasantville");
    driver.findElement(By.name("state")).sendKeys("CA");
    driver.findElement(By.name("pinno")).sendKeys("123456");
    driver.findElement(By.name("telephoneno")).sendKeys("8882053829");
    driver.findElement(By.name("emailid")).sendKeys("abc@gmail.com");
    driver.findElement(By.name("password")).sendKeys("Rand@123");
    driver.findElement(By.name("sub")).click();

    String expectedTitle = "Guru99 Bank Customer Registration Page";
    wait.until(ExpectedConditions.titleIs(expectedTitle));
    Assert.assertEquals(expectedTitle, driver.getTitle());
  }

  @Test(priority = 400)
  public void getCustomerId() {
    String customerId = driver.findElement(By.xpath("//td[text()='Customer ID']/following-sibling::td[1]")).getText();
    System.out.println("Customer ID - " + customerId);
  }

  @AfterTest
  public void closeWindows() {
    driver.quit();
  }
}