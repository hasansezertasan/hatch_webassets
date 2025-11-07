"""Entry point for the hatch-webassets plugin."""

from __future__ import annotations

from hatch_webassets.hooks import hatch_register_build_hook

__all__ = ["hatch_register_build_hook"]
