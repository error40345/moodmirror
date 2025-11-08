"""LiteLLM integration patches to handle event-loop lifecycle changes."""

from __future__ import annotations

import asyncio
from typing import Optional

try:
    from litellm.litellm_core_utils.logging_worker import LoggingWorker
except ImportError:  # pragma: no cover - LiteLLM is an optional dependency
    LoggingWorker = None  # type: ignore[assignment]


def _is_loop_closed(loop: Optional[asyncio.AbstractEventLoop]) -> bool:
    """Best-effort check to see if an event loop is closed."""
    if loop is None:
        return True
    try:
        return loop.is_closed()
    except Exception:
        return True


def patch_litellm_logging_worker() -> None:
    """
    Monkey-patch LiteLLM's LoggingWorker to tolerate new event loops.

    LiteLLM keeps a global LoggingWorker instance whose queue is bound to the
    event loop that first initializes it. When ROMA spins up new event loops
    (e.g., GEPA threads invoking asyncio.run), the original queue raises
    `RuntimeError: <Queue> is bound to a different event loop`.

    The patched start() detects when the queue belongs to a different or closed
    loop, cancels the stale worker task, and forces the queue to be recreated
    on the current loop before delegating to the original start().
    """
    if LoggingWorker is None:
        return

    if getattr(LoggingWorker, "_roma_patch_applied", False):
        return

    original_start = LoggingWorker.start

    def patched_start(self: LoggingWorker) -> None:  # type: ignore[override]
        try:
            current_loop = asyncio.get_running_loop()
        except RuntimeError:
            # No running loop (shouldn't happen for async workflows); fall back
            return original_start(self)

        queue = getattr(self, "_queue", None)
        if queue is not None:
            queue_loop = getattr(queue, "_loop", None)
            if queue_loop is not current_loop or _is_loop_closed(queue_loop):
                worker_task = getattr(self, "_worker_task", None)
                if worker_task is not None and not worker_task.done():
                    try:
                        worker_task.cancel()
                    except Exception:
                        pass
                self._worker_task = None
                self._queue = None

        return original_start(self)

    LoggingWorker.start = patched_start  # type: ignore[assignment]
    LoggingWorker._roma_patch_applied = True  # type: ignore[attr-defined]


__all__ = ["patch_litellm_logging_worker"]
