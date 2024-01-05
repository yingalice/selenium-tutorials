package _02_java.seleniumScripts;
import org.openqa.selenium.chrome.ChromeDriver;

public class WorkingWithChrome {
  ChromeDriver driver;
  String url = "http://demo.guru99.com/v4";

  public void invokeBrowser() {
    driver = new ChromeDriver();
    driver.manage().window().maximize();
    driver.get(url);
  }

  public void getTitle() {
    String titleOfThePage = driver.getTitle();
    System.out.println("Title of the Page - " + titleOfThePage);
  }

  public void closeBrowser() {
    driver.quit();
  }

  public static void main(String[] args) {
    WorkingWithChrome wc = new WorkingWithChrome();
    wc.invokeBrowser();
    wc.getTitle();
    wc.closeBrowser();
  }
}
