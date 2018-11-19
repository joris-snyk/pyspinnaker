import pytest
import requests_mock
from spinnaker import SpinnakerClient

class TestGetApplications(object):

    @classmethod
    @requests_mock.Mocker()
    def setup_class(cls, requests_mock):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        requests_mock.register_uri('GET', 'http://localhost:8084/applications/non_existing', json={"error":"Not Found"}, status_code=404)
        requests_mock.register_uri('GET', 'http://localhost:8084/applications/testxlr', json={"name":"testxlr"}, status_code=200)
        requests_mock.register_uri('GET', 'http://localhost:8084/applications', json=[{"name":"testxlr"}], status_code=200)

    def test_get_non_existing_application(self):
        with pytest.raises(Exception):
            x = SpinnakerClient("http://localhost:8084")
            x.get_application('non_existing')


    def test_get_existing_application(self):
        x = SpinnakerClient("http://localhost:8084")
        result = x.get_application('testxlr')
        assert result['name'] == 'testxlr'

    def test_get_applications(self):
        x = SpinnakerClient("http://localhost:8084")
        result = x.get_applications()
        assert len(result) > 0
