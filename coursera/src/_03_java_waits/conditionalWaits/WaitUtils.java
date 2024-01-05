package _03_java_waits.conditionalWaits;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.support.ui.WebDriverWait;

public class WaitUtils {
  public static void waitTillElementVisible(WebDriver driver, int timeoutInSeconds, By by) {
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(timeoutInSeconds));
    wait.until(ExpectedConditions.visibilityOfElementLocated(by));
  }

  public static void willTillAnAlertIsPresent(WebDriver driver, int timeoutInSeconds) {
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(timeoutInSeconds));
    wait.until(ExpectedConditions.alertIsPresent());
  }

  public static void waitTillElementClickable(WebDriver driver, int timeoutInSeconds, By by) {
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(timeoutInSeconds));
    wait.until(ExpectedConditions.elementToBeClickable(by));
  }

  public static void waitTillElementIsInvisible(WebDriver driver, int timeoutInSeconds, By by) {
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(timeoutInSeconds));
    wait.until(ExpectedConditions.invisibilityOfElementLocated(by));
  }

  public static void waitTillElementVisibleWithFluentWait(WebDriver driver, int pollingTimeInMillis, int timeoutInSeconds, By by) {
    Wait<WebDriver> wait = new FluentWait<>(driver)
      .withTimeout(Duration.ofSeconds(timeoutInSeconds))
      .pollingEvery(Duration.ofMillis(pollingTimeInMillis))
      .ignoring(NoSuchElementException.class);
    wait.until(ExpectedConditions.visibilityOfElementLocated(by));
  }
}