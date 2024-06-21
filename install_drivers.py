from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


driver_path_chrome = ChromeDriverManager().install()
driver_path_edge = EdgeChromiumDriverManager().install()
driver_path_firefox = GeckoDriverManager().install()