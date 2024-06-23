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

def test_star_whitelist():
    obj = ImageProcessor()
    whitelist = {'*': '*'}
    assert obj.filter_exif(1, whitelist) == 1

def test_no_dict_value():
    obj = ImageProcessor()
    exif = {0: 100}
    whitelist = {0: '*'}
    result = obj.filter_exif(exif, whitelist)
    assert result == {0: 100}

def test_not_in_whitelist():
    obj = ImageProcessor()
    exif = {0: {2: 'hello'}, 1: {3: 200}}
    whitelist = {5: '*'}
    obj.filter_exif(exif, whitelist)

def test_in_whitelist():
    obj = ImageProcessor()
    exif = {0: {2: 'hello'}, 1: {3: 200}}
    whitelist = {0: '*'}
    obj.filter_exif(exif, whitelist)
    
def test_last_if():
    obj = ImageProcessor()
    exif = {0: {2: 'hello'}, 1: {3: 200}}
    whitelist = {0: {2: 'hello'}}
    obj.filter_exif(exif, whitelist)
    ImageProcessor.print_coverage()
