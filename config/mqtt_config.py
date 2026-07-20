"""
=========================================================
Hybrid BCI JioSaavn Automation
MQTT Configuration
=========================================================

This module contains all MQTT-specific configuration
used throughout the project.

Imported by:
    - mqtt_client.py
    - publisher.py
    - subscriber.py
    - mqtt_manager.py
    - heartbeat.py
    - platform_detector.py
=========================================================
"""

from dataclasses import dataclass
from config.settings import settings


@dataclass(frozen=True)
class MQTTConfig:
    """
    MQTT Configuration Object
    """

    # =====================================================
    # Broker Configuration
    # =====================================================

    BROKER: str = settings.MQTT_BROKER

    PORT: int = settings.MQTT_PORT

    KEEPALIVE: int = settings.MQTT_KEEPALIVE

    QOS: int = settings.MQTT_QOS

    CLIENT_PREFIX: str = settings.MQTT_CLIENT_PREFIX

    # =====================================================
    # Topics
    # =====================================================

    COMMAND_TOPIC: str = settings.TOPIC_COMMAND

    CONTROL_TOPIC: str = settings.TOPIC_CONTROL

    ACK_TOPIC: str = settings.TOPIC_ACK

    STATUS_TOPIC: str = settings.TOPIC_STATUS

    HEARTBEAT_TOPIC: str = settings.TOPIC_HEARTBEAT

    # =====================================================
    # Connection
    # =====================================================

    CLEAN_SESSION: bool = True

    AUTO_RECONNECT: bool = True

    CONNECTION_TIMEOUT: int = 10

    RECONNECT_DELAY: int = 5

    MAX_RECONNECT_DELAY: int = 60

    # =====================================================
    # Heartbeat
    # =====================================================

    HEARTBEAT_INTERVAL: int = settings.HEARTBEAT_INTERVAL

    # =====================================================
    # Last Will Message
    # =====================================================

    LAST_WILL_TOPIC: str = settings.TOPIC_STATUS

    LAST_WILL_PAYLOAD: str = '{"status":"OFFLINE"}'

    ONLINE_PAYLOAD: str = '{"status":"ONLINE"}'

    # =====================================================
    # Payload Keys
    # =====================================================

    KEY_COMMAND: str = "command"

    KEY_CONFIDENCE: str = "confidence"

    KEY_TIMESTAMP: str = "timestamp"

    KEY_DOMAIN: str = "domain"

    KEY_SOURCE: str = "source"

    KEY_REQUEST: str = "request"

    KEY_STATUS: str = "status"


# Singleton configuration instance
mqtt_config = MQTTConfig()