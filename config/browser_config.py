"""
=========================================================
Hybrid BCI JioSaavn Automation
Browser Configuration
=========================================================

This module contains all browser automation settings.

Used By
-------
browser_controller.py
browser_detector.py
website_adapter.py
jiosaavn_controller.py
search.py
playback.py
volume.py
=========================================================
"""

from dataclasses import dataclass
from pathlib import Path

from config.settings import settings


@dataclass(frozen=True)
class BrowserConfig:
    """
    Browser Automation Configuration
    """

    # =====================================================
    # Browser Selection
    # =====================================================

    BROWSER = settings.BROWSER
    HEADLESS = settings.HEADLESS

    SUPPORTED_BROWSERS = [
        "chrome",
        "edge",
        "firefox"
    ]

    # =====================================================
    # Website
    # =====================================================

    WEBSITE_NAME = "JioSaavn"

    WEBSITE_URL = settings.WEBSITE_URL

    # =====================================================
    # Timeouts
    # =====================================================

    PAGE_LOAD_TIMEOUT = settings.PAGE_LOAD_TIMEOUT

    IMPLICIT_WAIT = 10

    EXPLICIT_WAIT = 20

    SCRIPT_TIMEOUT = 30

    # =====================================================
    # Browser Window
    # =====================================================

    WINDOW_WIDTH = 1400

    WINDOW_HEIGHT = 900

    START_MAXIMIZED = True

    # =====================================================
    # Browser Behaviour
    # =====================================================

    DISABLE_NOTIFICATIONS = True

    DISABLE_POPUPS = True

    AUTO_ACCEPT_COOKIES = True

    KEEP_BROWSER_OPEN = True

    # =====================================================
    # Selenium
    # =====================================================

    ENABLE_WEBDRIVER_MANAGER = True

    REUSE_BROWSER_SESSION = True

    ENABLE_JAVASCRIPT = True

    # =====================================================
    # Retry Settings
    # =====================================================

    MAX_RETRIES = 3

    RETRY_DELAY = 2

    # =====================================================
    # Login
    # =====================================================

    REQUIRE_LOGIN = False

    AUTO_LOGIN = False

    USERNAME = ""

    PASSWORD = ""

    # =====================================================
    # Search
    # =====================================================

    DEFAULT_SEARCH_DELAY = 2

    SEARCH_BOX_TIMEOUT = 15

    SEARCH_RESULT_TIMEOUT = 15

    # =====================================================
    # Playback
    # =====================================================

    PLAY_BUTTON_TIMEOUT = 15

    NEXT_BUTTON_TIMEOUT = 10

    PREVIOUS_BUTTON_TIMEOUT = 10

    PLAY_PAUSE_TIMEOUT = 10

    # =====================================================
    # Volume
    # =====================================================

    ENABLE_VOLUME_CONTROL = True

    DEFAULT_VOLUME_STEP = 5

    # =====================================================
    # CSS Selector File
    # =====================================================

    SELECTOR_FILE = (
        Path(__file__).resolve().parent.parent
        / "website"
        / "selectors.json"
    )

    # =====================================================
    # Browser Detection
    # =====================================================

    CHECK_ACTIVE_TAB = True

    CHECK_CURRENT_URL = True

    CHECK_BROWSER_RUNNING = True

    # =====================================================
    # Logging
    # =====================================================

    SAVE_SCREENSHOTS = False

    SCREENSHOT_FOLDER = (
        Path(__file__).resolve().parent.parent
        / "logs"
        / "screenshots"
    )

    LOG_BROWSER_ACTIONS = True

    LOG_BROWSER_ERRORS = True


# Singleton Instance
browser_config = BrowserConfig()