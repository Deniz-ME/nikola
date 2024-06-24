from nikola.log import configure_logging, print_coverage_configure, reset_coverage_configure, LoggingMode,  StrictModeExceptionHandler
from unittest.mock import patch
import logging
import pytest

@pytest.mark.skip(reason="None")
def test_normal_mode_debug():
    #reset_coverage_configure()
    with patch('nikola.log.DEBUG', True):
        configure_logging(logging_mode=LoggingMode.NORMAL)
        assert logging.root.level == logging.DEBUG
        foundHandler = False
        for handler in logging.root.handlers:
            if isinstance(handler, logging.StreamHandler):
                foundHandler = True
        assert foundHandler
        #print_coverage_configure()
        
@pytest.mark.skip(reason="None")
def test_normal_mode_no_debug():
    #reset_coverage_configure()
    configure_logging(logging_mode=LoggingMode.NORMAL)
    assert logging.root.level == logging.INFO
    foundHandler = False
    for handler in logging.root.handlers:
        if isinstance(handler, logging.StreamHandler):
            foundHandler = True
    assert foundHandler
    #print_coverage_configure()

@pytest.mark.skip(reason="None")
def test_quiet_mode_debug():
    #reset_coverage_configure()
    with patch('nikola.log.DEBUG', True):
        configure_logging(logging_mode=LoggingMode.QUIET)
        assert logging.root.level == logging.DEBUG
        assert not logging.root.handlers
        #print_coverage_configure()
  
@pytest.mark.skip(reason="None")
def test_quiet_mode_no_debug():
    #reset_coverage_configure()
    configure_logging(logging_mode=LoggingMode.QUIET)
    assert logging.root.level == logging.INFO
    assert not logging.root.handlers
    #print_coverage_configure()

@pytest.mark.skip(reason="None")
def test_strict_mode_debug():
    #reset_coverage_configure()
    with patch('nikola.log.DEBUG', True):
        configure_logging(logging_mode=LoggingMode.STRICT)
        assert logging.root.level == logging.DEBUG
        foundHandler = False
        foundHandler2 = False 
        for handler in logging.root.handlers:
            if isinstance(handler, logging.StreamHandler):
                foundHandler = True
            if isinstance(handler, StrictModeExceptionHandler):
                foundHandler2 = True
        assert foundHandler
        assert foundHandler2
        #print_coverage_configure()

@pytest.mark.skip(reason="None")
def test_strict_mode_no_debug():
    #reset_coverage_configure()
    configure_logging(logging_mode=LoggingMode.STRICT)
    assert logging.root.level == logging.INFO
    foundHandler = False
    foundHandler2 = False 
    for handler in logging.root.handlers:
        if isinstance(handler, logging.StreamHandler):
            foundHandler = True
        if isinstance(handler, StrictModeExceptionHandler):
            foundHandler2 = True
    assert foundHandler
    assert foundHandler2
    #print_coverage_configure()
    
    
def test_combined():
    reset_coverage_configure()
    test_normal_mode_debug()
    test_normal_mode_no_debug()
    test_quiet_mode_debug()
    test_quiet_mode_no_debug()
    test_strict_mode_debug()
    test_strict_mode_no_debug
    print_coverage_configure()

