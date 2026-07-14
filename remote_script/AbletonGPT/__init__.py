"""Lightweight Remote Script package for AbletonGPT."""

from .command_dispatcher import CommandDispatcher
from .control_surface import AbletonGPTControlSurface
from .socket_server import SocketServer


def create_instance(c_instance: object) -> AbletonGPTControlSurface:
    """Create a Remote Script control surface instance for Ableton."""
    return AbletonGPTControlSurface(c_instance=c_instance)


__all__ = ["AbletonGPTControlSurface", "CommandDispatcher", "SocketServer", "create_instance"]
