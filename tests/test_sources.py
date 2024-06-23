import pytest
from nikola.plugins.task.sources import Sources
from unittest.mock import MagicMock

@pytest.fixture(scope="module")
def source_mock_post():
    
    sources = Sources()
    sources.site = MagicMock()
    sources.site.config = {
        "TRANSLATIONS": {"en": True, "fr": True},
        "OUTPUT_FOLDER": "/fake/output",
        "DEFAULT_LANG": "en",
        "SHOW_UNTRANSLATED_POSTS": False,
        "COPY_SOURCES": True
    }

    mock_post = MagicMock()
    mock_post.meta = lambda key: True if key == 'password' else None # This is for that if password is filled in, in meta it will hit true and thus will execute the if statement.
    mock_post.translated_to = {"en"}  # We have two languages and only translated to 'en' and no 'fr' so we are able to hit the if statement
    sources.site.timeline = [mock_post]
    return sources

def test_mock_post(source_mock_site):
    source_mock_site.reset_coverage()
    list(source_mock_site.gen_tasks())
    source_mock_site.report_coverage()
