import pytest
import requests_mock
from spinnaker import SpinnakerClient

class TestGetApplications(object):

    @requests_mock.Mocker()
    def test_get_non_existing_application(self, requests_mock):
        requests_mock.register_uri('GET', 'http://localhost:8084/applications/non_existing', json={"error":"Not Found"}, status_code=404)
        with pytest.raises(Exception):
            x = SpinnakerClient("http://localhost:8084")
            x.get_application('non_existing')

    @requests_mock.Mocker()
    def test_get_existing_application(self, requests_mock):
        requests_mock.register_uri('GET', 'http://localhost:8084/applications/testxlr', json={"name":"testxlr"}, status_code=200)
        x = SpinnakerClient("http://localhost:8084")
        result = x.get_application('testxlr')
        assert result['name'] == 'testxlr'

    @requests_mock.Mocker()
    def test_get_applications(self, requests_mock):
        requests_mock.register_uri('GET', 'http://localhost:8084/applications', json=[{"name":"testxlr"}], status_code=200)
        x = SpinnakerClient("http://localhost:8084")
        result = x.get_applications()
        assert len(result) > 0
