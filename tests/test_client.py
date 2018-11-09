from spinnaker import SpinnakerClient

class TestClient(object):
    def test_init(self):
        x = SpinnakerClient()
        assert x is not None
