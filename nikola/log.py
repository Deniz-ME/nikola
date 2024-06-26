# -*- coding: utf-8 -*-

# Copyright © 2012-2024 Roberto Alsina and others.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Logging support."""

import enum
import logging
import warnings

from nikola import DEBUG

__all__ = (
    "get_logger",
    "LOGGER",
)


# Handlers/formatters
class ApplicationWarning(Exception):
    """An application warning, raised in strict mode."""

    pass


class StrictModeExceptionHandler(logging.StreamHandler):
    """A logging handler that raises an exception on warnings."""

    def emit(self, record: logging.LogRecord) -> None:
        """Emit a logging record."""
        if record.levelno >= logging.WARNING:
            raise ApplicationWarning(self.format(record))


colorful_wrap_coverage = {
    "wrap_in_color_1": False,
    "wrap_in_color_2": False,
    "wrap_in_color_3": False,
    "wrap_in_color_4": False,
    "wrap_in_color_5": False
}


class ColorfulFormatter(logging.Formatter):
    """Stream handler with colors."""

    _colorful = False

    def format(self, record: logging.LogRecord) -> str:
        """Format a message and add colors to it."""
        message = super().format(record)
        return self.wrap_in_color(record).format(message)

    def wrap_in_color(self, record: logging.LogRecord) -> str:
        """Return the colorized string for this record."""
        if not self._colorful:
            colorful_wrap_coverage["wrap_in_color_1"] = True
            return "{}"
        if record.levelno >= logging.ERROR:
            colorful_wrap_coverage["wrap_in_color_2"] = True
            return "\033[1;31m{}\033[0m"
        elif record.levelno >= logging.WARNING:
            colorful_wrap_coverage["wrap_in_color_3"] = True
            return "\033[1;33m{}\033[0m"
        elif record.levelno >= logging.INFO:
            colorful_wrap_coverage["wrap_in_color_4"] = True
            return "\033[1m{}\033[0m"
        colorful_wrap_coverage["wrap_in_color_5"] = True
        return "\033[37m{}\033[0m"
    
    def print_colorful_wrap_coverage():
        for branch, covered in colorful_wrap_coverage.items():
            print(f"{branch} is {'covered' if covered else 'not covered'}")


# Initial configuration
class LoggingMode(enum.Enum):
    """Logging mode options."""
    
    NORMAL = 0
    STRICT = 1
    QUIET = 2

branch_coverage_configure = {
    "branch_1": False, 
    "branch_2": False,  
    "branch_3": False, 
    "branch_4": False   
    }


def configure_logging(logging_mode: LoggingMode = LoggingMode.NORMAL) -> None:
    """Configure logging for Nikola.

    This method can be called multiple times, previous configuration will be overridden.
    """
    if DEBUG:
        branch_coverage_configure["branch_1"] = True
        logging.root.level = logging.DEBUG
    else:
        branch_coverage_configure["branch_2"] = True
        logging.root.level = logging.INFO

    if logging_mode == LoggingMode.QUIET:
        branch_coverage_configure["branch_3"] = True
        logging.root.handlers = []
        return

    handler = logging.StreamHandler()
    handler.setFormatter(
        ColorfulFormatter(
            fmt="[%(asctime)s] %(levelname)s: %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )

    handlers = [handler]
    if logging_mode == LoggingMode.STRICT:
        branch_coverage_configure["branch_4"] = True
        handlers.append(StrictModeExceptionHandler())

    logging.root.handlers = handlers

def print_coverage_configure():
    print("\n")
    for branch, hit in branch_coverage_configure.items():
        print(f"configure {branch} was {'hit' if hit else 'not hit'}")

def reset_coverage_configure():
    for key in branch_coverage_configure:
        branch_coverage_configure[key] = False

configure_logging()



# For compatibility with old code written with Logbook in mind
# TODO remove in v9
def patch_notice_level(logger: logging.Logger) -> logging.Logger:
    """Patch logger to issue WARNINGs with logger.notice."""
    logger.notice = logger.warning
    return logger


# User-facing loggers
def get_logger(name: str, handlers=None) -> logging.Logger:
    """Get a logger with handlers attached."""
    logger = logging.getLogger(name)
    if handlers is not None:
        for h in handlers:
            logger.addHandler(h)
    return patch_notice_level(logger)


LOGGER = get_logger("Nikola")


# Push warnings to logging
def showwarning(message, category, filename, lineno, file=None, line=None):
    """Show a warning (from the warnings module) to the user."""
    try:
        n = category.__name__
    except AttributeError:
        n = str(category)
    get_logger(n).warning("{0}:{1}: {2}".format(filename, lineno, message))


warnings.showwarning = showwarning
