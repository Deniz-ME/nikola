"""Check that per-day archives build and are correct."""

import os

import pytest

from nikola import __main__ 
from nikola.image_processing import ImageProcessor
from .helper import cd, patch_config
from .test_demo_build import prepare_demo_site
from .test_empty_build import (  # NOQA
    test_archive_exists,
    test_avoid_double_slash_in_rss,
    test_check_files,
    test_check_links,
    test_index_in_sitemap,
)


def test_day_archive(build, output_dir):
    """See that it builds"""
    archive = os.path.join(output_dir, "2012", "03", "30", "index.html")
    assert os.path.isfile(archive)


@pytest.fixture(scope="module")
def build(target_dir):
    """Fill the site with demo content and build it."""
    prepare_demo_site(target_dir)

    patch_config(
        target_dir, ("# CREATE_DAILY_ARCHIVE = False", "CREATE_DAILY_ARCHIVE = True")
    )

    with cd(target_dir):
        __main__.main(["build"])
    ImageProcessor.print_coverage()

