package task3;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class FlipkartProject {
	ChromeDriver driver;
	String url = "https://flipkart.com";
	
	@BeforeClass
	public void invokeBrowser() {
		driver = new ChromeDriver();
		driver.manage().window().maximize();
		driver.manage().deleteAllCookies();
    driver.manage().timeouts().pageLoadTimeout(Duration.ofSeconds(60));
		driver.get(url);
		
    // Login pop-up doesn't appear until refresh
		int retry_limit = 2;
		for (int retry_count = 0; retry_count < retry_limit; retry_count++) {
			try {
				driver.findElement(By.xpath("//div[@tabindex=-1]//span[@role='button']")).click();
				break;
			} catch (NoSuchElementException e) {
				driver.navigate().refresh();
			}
		}
	}
	
	@Test
	public void mouseHover() {
		Actions action = new Actions(driver);
		WebElement electronicsLink = driver.findElement(By.xpath("//div[@aria-label='Electronics']"));
		action.moveToElement(electronicsLink).build().perform();
    // Flipkart not a good example for waits anymore, as mouseover menu appears immediately without delay

		// Conditional waits: Explicit wait and fluent wait
		
		// Explicit wait - Time to wait for specific condition
		// WaitUtils.waitTillElementVisible(driver, 10, By.linkText("Electronics GST Store"));  

		// Fluent wait - Similar to explicit wait, and can define polling time and exceptions to ignore
		WaitUtils.waitTillElementVisibleWithFluentWait(driver, 200, 10, By.linkText("Electronics GST Store")); 
		WebElement storeLink = driver.findElement(By.linkText("Electronics GST Store"));
		action.moveToElement(storeLink).click().build().perform();
	}
	
	@AfterClass
	public void closeBrowser() {
		driver.quit();
	}
}