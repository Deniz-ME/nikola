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

"""Render pages into output."""

import os

from nikola.plugin_categories import Task
from nikola.utils import config_changed, LOGGER


class RenderPages(Task):
    """Render pages into output."""

    branch_coverage = {
    "branch_1": False,
    "branch_2": False,  
    "branch_3": False, 
    "branch_4": False,
    "branch_5": False   
    }

    name = "render_pages"

    def gen_tasks(self):
        """Build final pages from metadata and HTML fragments."""
        kw = {
            "post_pages": self.site.config["post_pages"],
            "translations": self.site.config["TRANSLATIONS"],
            "filters": self.site.config["FILTERS"],
            "show_untranslated_posts": self.site.config['SHOW_UNTRANSLATED_POSTS'],
            "demote_headers": self.site.config['DEMOTE_HEADERS'],
        }

        print("This is the pages file")
        self.site.scan_posts()
        yield self.group_task()
        index_paths = {}
        for lang in kw["translations"]:
            index_paths[lang] = False
            if not self.site.config["DISABLE_INDEXES"]:
                self.branch_coverage["branch_1"] = True                
                index_paths[lang] = os.path.normpath(os.path.join(self.site.config['OUTPUT_FOLDER'],
                                                     self.site.path('index', '', lang=lang)))

        for lang in kw["translations"]:
            for post in self.site.timeline:
                if not kw["show_untranslated_posts"] and not post.is_translation_available(lang):
                    self.branch_coverage["branch_2"] = True
                    continue
                if post.is_post:
                    self.branch_coverage["branch_3"] = True
                    context = {'pagekind': ['post_page']}
                else:
                    self.branch_coverage["branch_4"] = True
                    context = {'pagekind': ['story_page', 'page_page']}
                for task in self.site.generic_page_renderer(lang, post, kw["filters"], context):
                    if task['name'] == index_paths[lang]:
                        self.branch_coverage["branch_5"] = True
                        # Issue 3022
                        LOGGER.error(
                            "Post {0!r}: output path ({1}) conflicts with the blog index ({2}). "
                            "Please change INDEX_PATH or disable index generation.".format(
                                post.source_path, task['name'], index_paths[lang]))
                    task['uptodate'] = task['uptodate'] + [config_changed(kw, 'nikola.plugins.task.pages')]
                    task['basename'] = self.name
                    task['task_dep'] = ['render_posts']
                    yield task


    def report_coverage(self):
        for branch, hit in self.branch_coverage.items():
            print(f"{branch}: {'covered' if hit else 'not covered'}")