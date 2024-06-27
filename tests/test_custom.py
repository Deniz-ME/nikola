"""
Simple custom tests.

More advanced tests should be in a separate module.
"""


def test_color_formatter():
    "Test the ColorfulFormatter class."
    import logging
    from nikola.log import ColorfulFormatter
    
    formatter = ColorfulFormatter()
    # Test cases for each logging level and the colorful toggle
    test_cases = [
        (logging.DEBUG, False), (logging.DEBUG, True),
        (logging.INFO, False), (logging.INFO, True),
        (logging.WARNING, False), (logging.WARNING, True),
        (logging.ERROR, False), (logging.ERROR, True)
    ]

    dict_colors = {
        logging.DEBUG: "\033[37m{}\033[0m",
        logging.ERROR: "\033[1;31m{}\033[0m",
        logging.WARNING: "\033[1;33m{}\033[0m",
        logging.INFO: "\033[1m{}\033[0m",
    }

    for level, colorState in test_cases:
        # Create a LogRecord for the current level
        log_record = logging.LogRecord(
            name="test",
            level=level,
            pathname=__file__,
            lineno=10,
            msg="Test message",
            args=None,
            exc_info=None
        )

        formatter._colorful = colorState

        # Call format and print the result for verification
        formatted_message = formatter.format(log_record)
        print(f"Level: {log_record.levelname}, Colorful: {colorState}, Output: {formatted_message}")
        
        if colorState:
            assert formatted_message == dict_colors[level].format("Test message")
        else:
            assert formatted_message == "Test message"
    
    ColorfulFormatter.print_colorful_wrap_coverage()
    
