# -*- coding: utf-8 -*-

import unittest

from sync_settings.libs import file


class TestJSON(unittest.TestCase):
    def test_encode_json_with_comment_blocks(self):
        content = """
            {
                // gist id
                "gist_id": "123123",
                /**
                   another comment
                 */
                "access_token": "access_token",
                "another": "special char ؎"
            }
        """
        self.assertDictEqual({'gist_id': '123123', 'access_token': 'access_token', 'another': 'special char ؎'},
                             file.encode_json(content))

    def test_encode_json_without_comment_blocks(self):
        content = """
            {
                "gist_id": "123123",
                "access_token": "access_token"
            }
        """
        self.assertDictEqual({'gist_id': '123123', 'access_token': 'access_token'}, file.encode_json(content))
