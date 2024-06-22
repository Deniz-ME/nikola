import pytest
from nikola.plugins.task.pages import RenderPages
from unittest.mock import MagicMock

@pytest.fixture(scope="module")
def pages_mock_site():
    pages = RenderPages()
    pages.site = MagicMock()
    pages.site.config = {
        "TRANSLATIONS": {"en": True, "fr": True}, # We have english and french so that we can test for the if statement.
        "OUTPUT_FOLDER": "/fake/output",
        "DEFAULT_LANG": "en",
        "SHOW_UNTRANSLATED_POSTS": False,
        "COPY_SOURCES": True,
        "post_pages": [("index.html", "posts", "post.tmpl")],  
        "FILTERS": {},
        "DEMOTE_HEADERS": False, 
        "DISABLE_INDEXES": False 
    }

    mock_post = MagicMock()
    mock_post.translated_to = {"en"} # We have two languages and only translated to 'en' and no 'fr' so we are able to hit the if statement
    mock_post.is_translation_available = lambda lang: lang in mock_post.translated_to # This checks if there is a translation based on the language.
    pages.site.timeline = [mock_post]
    return pages

def test_mock_post(pages_mock_site):
    pages_mock_site.reset_coverage()
    list(pages_mock_site.gen_tasks())
    pages_mock_site.report_coverage()
