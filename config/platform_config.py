"""
=========================================================
Hybrid BCI JioSaavn Automation
Platform Configuration
=========================================================

This module contains all platform-related settings.

Supported Platforms
-------------------
1. Android APK
2. JioSaavn Website

Imported By
-----------
platform_manager.py
android_adapter.py
website_adapter.py
platform_detector.py
execution_manager.py
=========================================================
"""

from dataclasses import dataclass
from config.settings import settings


@dataclass(frozen=True)
class PlatformConfig:
    """
    Platform Configuration
    """

    # =====================================================
    # Platform Selection
    # =====================================================

    PLATFORM_MODE = settings.PLATFORM_MODE
    DEFAULT_PLATFORM = settings.DEFAULT_PLATFORM

    # Available Platforms
    ANDROID = "ANDROID"
    WEBSITE = "WEBSITE"
    AUTO = "AUTO"

    SUPPORTED_PLATFORMS = (
        ANDROID,
        WEBSITE
    )

    # =====================================================
    # Detection
    # =====================================================

    ENABLE_PLATFORM_DETECTION = settings.ENABLE_PLATFORM_DETECTION

    DETECTION_INTERVAL = settings.PLATFORM_CHECK_INTERVAL

    DETECTION_TIMEOUT = settings.NETWORK_TIMEOUT

    # =====================================================
    # Priority
    # =====================================================

    # Used when both Android APK and Website are available

    PLATFORM_PRIORITY = [
        ANDROID,
        WEBSITE
    ]

    # =====================================================
    # Automatic Fallback
    # =====================================================

    ENABLE_FALLBACK = True

    FALLBACK_PLATFORM = WEBSITE

    # =====================================================
    # Android Settings
    # =====================================================

    ANDROID_PACKAGE = "com.synaptimesh.bci"

    JIOSAAVN_PACKAGE = "com.jio.media.jiobeats"

    MQTT_ENABLED = True

    WAIT_FOR_ACK = True

    ACK_TIMEOUT = 5

    # =====================================================
    # Website Settings
    # =====================================================

    WEBSITE_NAME = "JioSaavn"

    WEBSITE_URL = settings.WEBSITE_URL

    BROWSER = settings.BROWSER

    HEADLESS = settings.HEADLESS

    PAGE_LOAD_TIMEOUT = settings.PAGE_LOAD_TIMEOUT

    # =====================================================
    # Browser Detection
    # =====================================================

    CHECK_BROWSER_RUNNING = True

    CHECK_ACTIVE_TAB = True

    CHECK_LOGIN = False

    # =====================================================
    # Retry
    # =====================================================

    MAX_PLATFORM_RETRY = 3

    RETRY_DELAY = 2

    # =====================================================
    # Logging
    # =====================================================

    LOG_PLATFORM_SELECTION = True

    LOG_PLATFORM_SWITCH = True


# Singleton instance
platform_config = PlatformConfig()