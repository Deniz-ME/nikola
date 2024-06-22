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

"""Copy page sources into the output."""

import os

from nikola.plugin_categories import Task
from nikola import utils


class Sources(Task):
    """Copy page sources into the output."""

    branch_coverage = {
    "branch_1": False,
    "branch_2": False,  
    "branch_3": False, 
    "branch_4": False,
    "branch_5": False   
    }

    name = "render_sources"

    def gen_tasks(self):
        """Publish the page sources into the output."""
        kw = {
            "translations": self.site.config["TRANSLATIONS"],
            "output_folder": self.site.config["OUTPUT_FOLDER"],
            "default_lang": self.site.config["DEFAULT_LANG"],
            "show_untranslated_posts": self.site.config['SHOW_UNTRANSLATED_POSTS'],
        }

        self.site.scan_posts()
        yield self.group_task()
        if self.site.config['COPY_SOURCES']:
            self.branch_coverage["branch_1"] = True
            for lang in kw["translations"]:
                for post in self.site.timeline:
                    if not kw["show_untranslated_posts"] and lang not in post.translated_to:
                        self.branch_coverage["branch_2"] = True
                        continue
                    if post.meta('password'):
                        self.branch_coverage["branch_3"] = True
                        continue
                    output_name = os.path.join(
                        kw['output_folder'], post.destination_path(
                            lang, post.source_ext(True)))
                    # do not publish PHP sources
                    if post.source_ext(True) == post.compiler.extension():
                        self.branch_coverage["branch_4"] = True
                        continue
                    source = post.translated_source_path(lang)
                    if source is not None and os.path.isfile(source):
                        self.branch_coverage["branch_5"] = True
                        yield {
                            'basename': 'render_sources',
                            'name': os.path.normpath(output_name),
                            'file_dep': [source],
                            'targets': [output_name],
                            'actions': [(utils.copy_file, (source, output_name))],
                            'clean': True,
                            'uptodate': [utils.config_changed(kw, 'nikola.plugins.task.sources')],
                        }
    
    def report_coverage(self):
        for branch, hit in self.branch_coverage.items():
            print(f"{branch}: {'covered' if hit else 'not covered'}")

    def reset_coverage(self):
        for key in self.branch_coverage:
            self.branch_coverage[key] = False 