#!/usr/bin/env python
"""
Note: QRZ paid subscription is required, currently $29.95/year
https://www.qrz.com/page/current_spec.html
"""
import six
import os
import requests
import xmltodict
from six.moves.configparser import ConfigParser,NoSectionError,NoOptionError
from getpass import getpass
#
if six.PY2:
    ConnectionError = OSError


class QRZerror(Exception):
    pass


class CallsignNotFound(Exception):
    pass


class QRZ(object):
    def __init__(self, cfg=None):
        if cfg:
            self._cfg = ConfigParser()
            self._cfg.read(cfg)
        else:
            self._cfg = None
        self._session = None
        self._session_key = None


    def _get_session(self):
        try:
            username = self._cfg.get('qrz', 'username')
            password = self._cfg.get('qrz', 'password')
        except (NoSectionError,NoOptionError,AttributeError):
            username = os.environ.get('QRZ_USER')
            password = os.environ.get('QRZ_PASSWORD')

        if not username or not password:
            raise ValueError('must enter username and password')

        url = 'https://xmldata.qrz.com/xml/current/?username={}&password={}'.format(username, password)
        url = 'https://xmldata.qrz.com/xml/current/'
        self._session = requests.Session()
#        self._session.verify = False
        r = self._session.get(url)
        if r.status_code == 200:
            raw = xmltodict.parse(r.content)
            try:
                self._session_key = raw['QRZDatabase']['Session']['Key']
                if self._session_key:
                    return True
            except KeyError:
                print(raw)

        raise ConnectionError("Could not get QRZ session")


    def callsign(self, callsign, retry=True):
        if self._session_key is None:
            self._get_session()
        url = """http://xmldata.qrz.com/xml/current/?s={0}&callsign={1}""".format(self._session_key, callsign)
        r = self._session.get(url)
        if r.status_code != 200:
            raise ConnectionError("Error Querying: Response code {}".format(r.status_code))
        raw = xmltodict.parse(r.content).get('QRZDatabase')
        if not raw:
            raise QRZerror('Unexpected API Result')
        if raw['Session'].get('Error'):
            errormsg = raw['Session'].get('Error')
            if 'Session Timeout' in errormsg or 'Invalid session key' in errormsg:
                if retry:
                    self._session_key = None
                    self._session = None
                    return self.callsign(callsign, retry=False)
            elif "not found" in errormsg.lower():
                raise CallsignNotFound(errormsg)
            raise QRZerror(raw['Session'].get('Error'))
        else:
            ham = raw.get('Callsign')
            if ham:
                return ham

        raise Exception("Unhandled Error during Query")
