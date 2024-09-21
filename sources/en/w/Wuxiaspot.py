# -*- coding: utf-8 -*-
import logging

from lncrawl.templates.Wuxiaspot import WuxiaspotTemplate

logger = logging.getLogger(__name__)


class WuxiaspotCrawler(WuxiaspotTemplate):
    base_url = [
        "https://www.wuxiaspot.com",
    ]

    def initialize(self) -> None:
        self.cleaner.bad_css.update(
            [
                'div[align="left"]',
                'img[src*="proxy?container=focus"]',
            ]
        )
