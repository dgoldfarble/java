"""
 ** This data and information is proprietary to, and a valuable trade secret
 ** of, Basis Technology Corp.  It is given in confidence by Basis Technology
 ** and may only be used as permitted under the license agreement under which
 ** it has been distributed, and in no other way.
 **
 ** Copyright (c) 2014 Basis Technology Corporation All rights reserved.
 **
 ** The technical data and information provided herein are provided with
 ** `limited rights', and the computer software provided herein is provided
 ** with `restricted rights' as those terms are defined in DAR and ASPR
 ** 7-104.9(a).
"""

import unittest
import logging
from rosette.api import API, ResultFormat, RaasParameters
import os
import sys
import json


logging.basicConfig(level=logging.DEBUG)

class SentencesTestCase(unittest.TestCase):
 
    def test_sentence_splitting(self):
        port = os.environ['MOCK_SERVICE_PORT']
        url = 'http://localhost:' + port + '/raas'
        url = "http://jugmaster.basistech.net/rest/v1"
        logging.info("URL " + url)
        params = RaasParameters()
        params.content = "Yes, Ma'm! Green eggs and ham?  I am Sam;  I filter Spam."
        params.contentType = "text/plain"
        params.unit = "doc"
        # the mock services can't respond to the individual params.
        op = API(service_url = url).sentences_split()
        result = op.operate(params, None)
        self.assertIsNotNone(result['sentences'])
        self.assertEqual(len(result['sentences']), 3)

    def test_tokenizing(self):
        port = os.environ['MOCK_SERVICE_PORT']
        url = 'http://localhost:' + port + '/raas'
        url = "http://jugmaster.basistech.net/rest/v1"
        logging.info("URL " + url)
        params = RaasParameters()
        params.content = "Yes, Ma'm! Green eggs and ham?  I am Sam;  I filter Spam."
        params.contentType = "text/plain"
        params.unit = "doc"

        op = API(service_url = url).tokenize()
        result = op.operate(params, None)
        self.assertEqual(len(result['tokens']), 18)

    def test_morphology(self):
        port = os.environ['MOCK_SERVICE_PORT']
        url = 'http://localhost:' + port + '/raas'
        url = "http://jugmaster.basistech.net/rest/v1"
        logging.info("URL " + url)
        params = RaasParameters()
        params.content = "Yes, Ma'm! Green eggs and ham?  I am Sam;  I filter Spam."
        params.contentType = "text/plain"
        params.unit = "doc"

        op = API(service_url = url).morphology("part-of-speech,lemmas")
        result = op.operate(params, None)
        print >>sys.stderr, result


        
