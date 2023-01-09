from rest_framework.test import APITestCase, APIRequestFactory
from flight.views import FlightView

class FlightViewTstCase(APITestCase):

    
    # def setUp(self):
    #     self.factory = APIRequestFactory()

    def test_flight_list_as_non_authenticate_user(self):
        factory = APIRequestFactory()
        request = factory.get('/flight/flights/')
        response = FlightView.as_view({'get':'list'})(request)
        self.assertEquals(response.status_code, 200)

