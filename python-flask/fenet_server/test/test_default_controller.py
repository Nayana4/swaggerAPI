# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from fenet_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_fecontent_get_sc_image(self):
        """Test case for fecontent_get_sc_image

        Gets security content image
        """
        headers = [('range', 'range_example')]
        response = self.client.open(
            '/fenet/MetaData/1.0.0/fecontent/{scParameters}'.format(scParameters='scParameters_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_femeta_get_meta_data(self):
        """Test case for femeta_get_meta_data

        Gets Meta Data
        """
        headers = [('range', 'range_example')]
        response = self.client.open(
            '/fenet/MetaData/1.0.0/femeta/{metaParameters}'.format(metaParameters='metaParameters_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
