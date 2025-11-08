"""Event model definitions for the async task scheduler."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Optional


class EventType(Enum):
    """Event categories routed through the scheduler."""

    READY = auto()
    COMPLETED = auto()
    FAILED = auto()
    SUBGRAPH_COMPLETE = auto()
    STOP = auto()


@dataclass(order=True)
class TaskEvent:
    """Small payload describing a scheduler event."""

    priority: int
    event_type: EventType = field(compare=False)
    task_id: Optional[str] = field(default=None, compare=False)
    dag_id: Optional[str] = field(default=None, compare=False)
    data: Optional[Any] = field(default=None, compare=False)

    def with_data(self, data: Any) -> "TaskEvent":
        """Return a copy carrying extra data without mutating in-place."""

        return TaskEvent(
            priority=self.priority,
            event_type=self.event_type,
            task_id=self.task_id,
            dag_id=self.dag_id,
            data=data,
        )
