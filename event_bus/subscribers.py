"""
=========================================================
Hybrid BCI JioSaavn Automation
Subscribers Registration
=========================================================

Registers all event subscribers with the EventBus.

=========================================================
"""

import logging

from event_bus.event_types import EventTypes


def register_subscribers(
    event_bus,
    decision_manager,
    execution_manager,
    analytics_manager,
    history_manager,
    scheduler,
    context_manager,
):
    """
    Register all subscribers.

    Parameters
    ----------
    event_bus : EventBus
    decision_manager : DecisionManager
    execution_manager : ExecutionManager
    analytics_manager : AnalyticsManager
    history_manager : HistoryManager
    scheduler : Scheduler
    context_manager : ContextManager
    """

    logging.info("Registering Event Subscribers...")

    # =====================================================
    # Prediction Events
    # =====================================================

    event_bus.subscribe(
        EventTypes.PREDICTION_GENERATED,
        decision_manager.handle_prediction
    )

    event_bus.subscribe(
        EventTypes.PREDICTION_FILTERED,
        decision_manager.handle_filtered_prediction
    )

    event_bus.subscribe(
        EventTypes.PREDICTION_SMOOTHED,
        decision_manager.handle_smoothed_prediction
    )

    # =====================================================
    # Decision Events
    # =====================================================

    event_bus.subscribe(
        EventTypes.DECISION_READY,
        execution_manager.execute
    )

    # =====================================================
    # Execution Events
    # =====================================================

    event_bus.subscribe(
        EventTypes.EXECUTION_COMPLETED,
        analytics_manager.log_execution
    )

    event_bus.subscribe(
        EventTypes.EXECUTION_COMPLETED,
        history_manager.save_execution
    )

    event_bus.subscribe(
        EventTypes.EXECUTION_COMPLETED,
        scheduler.schedule_next
    )

    # =====================================================
    # Platform Events
    # =====================================================

    event_bus.subscribe(
        EventTypes.PLATFORM_CHANGED,
        context_manager.update_platform
    )

    # =====================================================
    # Player Events
    # =====================================================

    event_bus.subscribe(
        EventTypes.SONG_STARTED,
        context_manager.song_started
    )

    event_bus.subscribe(
        EventTypes.SONG_PAUSED,
        context_manager.song_paused
    )

    event_bus.subscribe(
        EventTypes.SONG_CHANGED,
        context_manager.song_changed
    )

    event_bus.subscribe(
        EventTypes.VOLUME_CHANGED,
        context_manager.volume_changed
    )

    # =====================================================
    # MQTT Events
    # =====================================================

    event_bus.subscribe(
        EventTypes.MQTT_CONNECTED,
        analytics_manager.mqtt_connected
    )

    event_bus.subscribe(
        EventTypes.MQTT_DISCONNECTED,
        analytics_manager.mqtt_disconnected
    )

    # =====================================================
    # Session Events
    # =====================================================

    event_bus.subscribe(
        EventTypes.SESSION_STARTED,
        analytics_manager.session_started
    )

    event_bus.subscribe(
        EventTypes.SESSION_STOPPED,
        analytics_manager.session_stopped
    )

    logging.info("All subscribers registered successfully.")