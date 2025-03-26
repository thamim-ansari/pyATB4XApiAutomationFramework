# API Constants - Class which contains all the endpoints.
# Keep the URLs

class APIConstants(object):
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def create_booking_url(self):
        return "https://restful-booker.herokuapp.com/booking"

    def create_auth_token_url(self):
        return "https://restful-booker.herokuapp.com/auth"

    def patch_put_delete_booking_url(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
