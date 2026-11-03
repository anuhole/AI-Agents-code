package tests;

import org.junit.jupiter.api.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import java.util.concurrent.TimeUnit;

public class LoginTests {

    private WebDriver driver;

    @BeforeEach
    public void setUp() {
        // Assuming chromedriver is in PATH or set via system property
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        driver.get("https://www.saucedemo.com");
    }

    @AfterEach
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    @Test
    @DisplayName("Valid login shows inventory list")
    public void testValidLogin() {
        driver.findElement(By.id("user-name")).sendKeys("standard_user");
        driver.findElement(By.id("password")).sendKeys("secret_sauce");
        driver.findElement(By.id("login-button")).click();

        WebElement inventoryList = driver.findElement(By.className("inventory_list"));
        Assertions.assertTrue(inventoryList.isDisplayed(), "Inventory list should be displayed after successful login");
    }

    @Test
    @DisplayName("Wrong password shows error message")
    public void testWrongPassword() {
        driver.findElement(By.id("user-name")).sendKeys("standard_user");
        driver.findElement(By.id("password")).sendKeys("wrong_password");
        driver.findElement(By.id("login-button")).click();

        WebElement errorMsg = driver.findElement(By.cssSelector("[data-test='error']"));
        Assertions.assertTrue(errorMsg.isDisplayed(), "Error message should be displayed for wrong password");
    }

    @Test
    @DisplayName("Empty credentials show error message")
    public void testEmptyCredentials() {
        driver.findElement(By.id("login-button")).click();

        WebElement errorMsg = driver.findElement(By.cssSelector("[data-test='error']"));
        Assertions.assertTrue(errorMsg.isDisplayed(), "Error message should be displayed for empty credentials");
    }
}
