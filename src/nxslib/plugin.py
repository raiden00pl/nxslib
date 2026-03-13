"""Module containing nxslib plugin interfaces."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nxslib.dev import Device
    from nxslib.nxscope import NxscopeHandler
    from nxslib.proto.iframe import DParseFrame


class INxscopePlugin:
    """Base interface for nxslib plugins."""

    name: str = "plugin"

    def on_register(self, nxscope: "NxscopeHandler") -> None:
        """Handle plugin registration."""
        del nxscope

    def on_unregister(self) -> None:
        """Handle plugin unregistration."""

    def on_connect(self, dev: "Device") -> None:
        """Handle established nxscope connection."""
        del dev

    def on_disconnect(self) -> None:
        """Handle nxscope disconnection."""

    def on_user_frame(self, frame: "DParseFrame") -> bool | None:
        """Handle a user-defined frame."""
        del frame
        return False
