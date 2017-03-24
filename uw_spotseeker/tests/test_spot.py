from uw_spotseeker import Spotseeker
from uw_spotseeker.utilities import fdao_spotseeker_override
from restclients_core.exceptions import (
    DataFailureException)
from unittest import TestCase
import dateutil.parser


@fdao_spotseeker_override
class SpotseekerTestSpot(TestCase):

    def test_get_all_spots(self):
        spotseeker = Spotseeker()
        all_spots = spotseeker.all_spots()
        self.assertEqual(len(all_spots), 3)

    def test_get_spot(self):
        spotseeker = Spotseeker()
        spot_data = spotseeker.get_spot_by_id(123)

        self.assertEqual(spot_data.spot_id, "123")
        self.assertEqual(spot_data.name, "Test Spot")
        self.assertEqual(spot_data.uri, "/api/v1/spot/123")
        self.assertEqual(spot_data.latitude, 3.60)
        self.assertEqual(spot_data.longitude, 1.34)
        self.assertEqual(spot_data.height_from_sea_level, 0.10)
        self.assertEqual(spot_data.building_name, "Test Building")
        self.assertEqual(spot_data.floor, 0)
        self.assertEqual(spot_data.room_number, "456")
        self.assertEqual(spot_data.capacity, 0)
        self.assertEqual(spot_data.display_access_restrictions, "none")
        self.assertEqual(spot_data.organization, "Test Org")
        self.assertEqual(spot_data.manager, "Mr Test Org")
        self.assertEqual(spot_data.etag, "686897696a7c876b7e")
        self.assertEqual(spot_data.external_id, "asd123")
        self.assertEqual(spot_data.last_modified,
                         dateutil.parser.parse("2012-07-13T05:00:00+00:00"))

        self._assert_spot_types(spot_data.spot_types, ["study_room", "cafe"])
        # self.assertEqual(len(spot_data.images), 1)
        # self.assertEqual(spot_data.images[0].image_id, "1")
        # self.assertEqual(spot_data.images[0].url,
        #                  "/api/v1/spot/123/image/1")
        # self.assertEqual(spot_data.images[0].content_type, "image/jpeg")
        # self.assertEqual(spot_data.images[0].width, 0)
        # self.assertEqual(spot_data.images[0].height, 0)
        # self.assertEqual(spot_data.images[0].creation_date,
        #                  parse_datetime("Sun, 06 Nov 1994 08:49:37 GMT"))
        # self.assertEqual(spot_data.images[0].modification_date,
        #                  parse_datetime("Mon, 07 Nov 1994 01:49:37 GMT"))
        # self.assertEqual(spot_data.images[0].upload_user,
        #                  "user name")
        # self.assertEqual(spot_data.images[0].upload_application,
        #                  "application name")
        # self.assertEqual(spot_data.images[0].thumbnail_root,
        #                  "/api/v1/spot/123/image/1/thumb")
        # self.assertEqual(spot_data.images[0].description,
        #                  "Information about the image")
        # self.assertEqual(spot_data.images[0].display_index, 0)
        #
        self.assertEqual(len(spot_data.spot_availability), 7)
        self._assert_spot_extended_info(spot_data.extended_info, [
            ("field2", 0),
            ("field3", 0.0),
            ("whiteboards", True)
        ])

    def _assert_spot_types(self, spot_types, type_stings):
        spot_types = [spot_type.name for spot_type in spot_types]
        self.assertEqual(set(spot_types), set(type_stings))

    def _assert_spot_extended_info(self, spot_ei_data, ei_tuples):
        spot_ei_tuples = [(spot_ei.key, spot_ei.value)
                          for spot_ei
                          in spot_ei_data]
        self.assertEqual(set(spot_ei_tuples), set(ei_tuples))
