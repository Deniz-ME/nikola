"""
Simple plugin tests.

More advanced tests should be in a separate module.
"""


def test_command_version():
    """Test `nikola version`."""
    from nikola.plugins.command.version import CommandVersion

    CommandVersion().execute()

def test_command_version_check():
    """Test `nikola version --check`."""
    from nikola.plugins.command.version import CommandVersion
    import io
    import sys
    from nikola import __version__

    capturedOutput = io.StringIO()   
    sys.stdout = capturedOutput

    CommandVersion().execute({'check': True})
    assert "Nikola v" + __version__ in capturedOutput.getvalue()

    CommandVersion().execute({'check': True, 'old': True})
    assert "The latest version of Nikola is v4.2.0" in capturedOutput.getvalue()

    CommandVersion.print_command_version_coverage()
    sys.stdout = sys.__stdout__


def test_importing_plugin_task_galleries():
    import nikola.plugins.task.galleries  # NOQA


def test_importing_plugin_compile_pandoc():
    import nikola.plugins.compile.pandoc  # NOQA
