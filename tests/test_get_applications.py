import pytest
from spinnaker import SpinnakerClient

class TestGetApplications(object):
    def test_get_non_existing_application(self):
        with pytest.raises(Exception):
            x = SpinnakerClient("http://localhost:8084")
            result = x.get_application('non_existing')


    def test_get_existing_application(self):
        x = SpinnakerClient("http://localhost:8084")
        result = x.get_application('testxlr')
        assert result['name'] == 'testxlr'

    def test_get_applications(self):
        x = SpinnakerClient("http://localhost:8084")
        result = x.get_applications()
        assert len(result) > 0
