import inspect
import sys
from pathlib import Path
from typing import Callable, List
from loguru import logger


def _add_class_name(record):
    """Patch logger records to include the caller's class name."""
    if record["extra"].get("classname") is not None:
        return
    frame = inspect.currentframe()
    try:
        while frame:
            frame = frame.f_back
            if frame and frame.f_globals.get("__name__") not in (
                "loguru._logger",
                __name__,
            ):
                cls = frame.f_locals.get("self") or frame.f_locals.get("cls")
                if cls is not None:
                    record["extra"]["classname"] = (
                        cls.__name__ if isinstance(cls, type) else type(cls).__name__
                    )
                else:
                    record["extra"]["classname"] = "Global"
                break
        else:
            record["extra"]["classname"] = "Global"
    finally:
        del frame


def setup_logging(
    log_base_path="logs",
    patchers: List[Callable] = [],
    rotation: str = "1 day",
    compression: str = "zip",
    level: str = "INFO",
    app_retention: str = "7 days",
    meter_retention: str = "30 days",
    **kwargs,
) -> None:
    log_path = Path(log_base_path)
    log_path.mkdir(exist_ok=True)

    def default_patcher(record):
        for patcher in patchers or []:
            patcher(record)

    patchers.append(_add_class_name)
    logger.remove()
    logger.configure(patcher=default_patcher)

    # Common format string (DRY principle)
    log_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{extra[classname]}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "{message} | <blue>Context: {extra}</blue>"
    )

    log_kwargs = {
        "rotation": rotation,
        "compression": compression,
        "format": log_format,
        "level": level,
        **kwargs,
    }

    # 2. Console (Everything INFO+)
    logger.add(sys.stderr, format=log_format, level="INFO", colorize=True)

    # 3. Application Logs (Daily Rotation)
    logger.add(
        log_path / "application_{time:YYYY-MM-DD}.log",
        filter=lambda r: r["extra"].get("type") == "app",
        retention=app_retention,
        **log_kwargs,
    )

    # 4. Metering Logs
    logger.add(
        log_path / "metering_{time:YYYY-MM-DD}.log",
        filter=lambda r: r["extra"].get("type") == "meter",
        retention=meter_retention,
        **log_kwargs,
    )
