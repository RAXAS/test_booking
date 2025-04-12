from fixtures import auth, booking_data, booking_update_data, unauthorized_session
from constant import BASE_URL


class TestBooking:

    def test_create_booking(self, booking_data, auth):
        create_booking = auth.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Create Error"
        booking_create_response = create_booking.json()
        booking_id = booking_create_response.get("bookingid")
        assert booking_id is not None, "ID is not Found"

        assert booking_create_response["booking"]["firstname"] == booking_data["firstname"], "Name is not matched"
        assert booking_create_response["booking"]["lastname"] == booking_data["lastname"], "Surname is not matched"
        assert booking_create_response["booking"]["totalprice"] == booking_data["totalprice"], "Total Price is not matched"
        assert booking_create_response["booking"]["depositpaid"] == booking_data["depositpaid"], "Deposit Paid is not matched"
        assert booking_create_response["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"], "Checkin Date is not matched"
        assert booking_create_response["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"], "Checkout Date is not matched"
        assert booking_create_response["booking"]["additionalneeds"] == booking_data["additionalneeds"], "Additional Needs are not matched"

        get_booking = auth.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Error to get booking with ID: {booking_id}"

        delete_booking = auth.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Error to delete booking with ID:{booking_id}"

        check_delete_response = auth.get(f"{BASE_URL}/booking/{booking_id}")
        assert check_delete_response.status_code == 404, f"Booking with ID: {booking_id} was not deleted"

    def test_put_update_booking(self, auth, booking_data, booking_update_data):
        create_booking = auth.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Create Error"
        booking_create_response = create_booking.json()
        booking_id = booking_create_response.get("bookingid")
        assert booking_id is not None, "ID is not Found"

        assert booking_create_response["booking"]["firstname"] == booking_data["firstname"], "Name is not matched"
        assert booking_create_response["booking"]["lastname"] == booking_data["lastname"], "Surname is not matched"
        assert booking_create_response["booking"]["totalprice"] == booking_data["totalprice"], "Total Price is not matched"
        assert booking_create_response["booking"]["depositpaid"] == booking_data["depositpaid"], "Deposit Paid is not matched"
        assert booking_create_response["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"], "Checkin Date is not matched"
        assert booking_create_response["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"], "Checkout Date is not matched"
        assert booking_create_response["booking"]["additionalneeds"] == booking_data["additionalneeds"], "Additional Needs are not matched"

        get_booking = auth.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Error to get booking with ID: {booking_id}"

        update_booking = auth.put(f"{BASE_URL}/booking/{booking_id}", json=booking_update_data)
        assert update_booking.status_code == 200, "Create Error"
        booking_update_response = update_booking.json()

        assert booking_update_response["firstname"] == booking_update_data["firstname"], "Name is not matched"
        assert booking_update_response["lastname"] == booking_update_data["lastname"], "Surname is not matched"
        assert booking_update_response["totalprice"] == booking_update_data["totalprice"], "Total Price is not matched"
        assert booking_update_response["depositpaid"] == booking_update_data["depositpaid"], "Deposit Paid is not matched"
        assert booking_update_response["bookingdates"]["checkin"] == booking_update_data["bookingdates"]["checkin"], "Checkin Date is not matched"
        assert booking_update_response["bookingdates"]["checkout"] == booking_update_data["bookingdates"]["checkout"], "Checkout Date is not matched"
        assert booking_update_response["additionalneeds"] == booking_update_data["additionalneeds"], "Additional Needs are not matched"

        get_booking = auth.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Error to get booking with ID: {booking_id}"
        booking_get_response = get_booking.json()

        assert booking_get_response["firstname"] == booking_update_data["firstname"], "Name is not matched"
        assert booking_get_response["lastname"] == booking_update_data["lastname"], "Surname is not matched"
        assert booking_get_response["totalprice"] == booking_update_data["totalprice"], "Total Price is not matched"
        assert booking_get_response["depositpaid"] == booking_update_data["depositpaid"], "Deposit Paid is not matched"
        assert booking_get_response["bookingdates"]["checkin"] == booking_update_data["bookingdates"]["checkin"], "Checkin Date is not matched"
        assert booking_get_response["bookingdates"]["checkout"] == booking_update_data["bookingdates"]["checkout"], "Checkout Date is not matched"
        assert booking_get_response["additionalneeds"] == booking_update_data["additionalneeds"], "Additional Needs are not matched"

        delete_booking = auth.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Error to delete booking with ID:{booking_id}"

        check_delete_response = auth.get(f"{BASE_URL}/booking/{booking_id}")
        assert check_delete_response.status_code == 404, f"Booking with ID: {booking_id} was not deleted"

    def test_patch_update_booking(self, auth, booking_data, booking_update_data):
        create_booking = auth.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Create Error"
        booking_create_response = create_booking.json()
        booking_id = booking_create_response.get("bookingid")
        assert booking_id is not None, "ID is not Found"

        assert booking_create_response["booking"]["firstname"] == booking_data["firstname"], "Name is not matched"
        assert booking_create_response["booking"]["lastname"] == booking_data["lastname"], "Surname is not matched"
        assert booking_create_response["booking"]["totalprice"] == booking_data["totalprice"], "Total Price is not matched"
        assert booking_create_response["booking"]["depositpaid"] == booking_data["depositpaid"], "Deposit Paid is not matched"
        assert booking_create_response["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"], "Checkin Date is not matched"
        assert booking_create_response["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"], "Checkout Date is not matched"
        assert booking_create_response["booking"]["additionalneeds"] == booking_data["additionalneeds"], "Additional Needs are not matched"

        get_booking = auth.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Error to get booking with ID: {booking_id}"

        update_booking = auth.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_update_data)
        assert update_booking.status_code == 200, "Create Error"
        booking_update_response = update_booking.json()

        assert booking_update_response["firstname"] == booking_update_data["firstname"], "Name is not matched"
        assert booking_update_response["lastname"] == booking_update_data["lastname"], "Surname is not matched"
        assert booking_update_response["totalprice"] == booking_update_data["totalprice"], "Total Price is not matched"
        assert booking_update_response["depositpaid"] == booking_update_data["depositpaid"], "Deposit Paid is not matched"
        assert booking_update_response["bookingdates"]["checkin"] == booking_update_data["bookingdates"]["checkin"], "Checkin Date is not matched"
        assert booking_update_response["bookingdates"]["checkout"] == booking_update_data["bookingdates"]["checkout"], "Checkout Date is not matched"
        assert booking_update_response["additionalneeds"] == booking_update_data["additionalneeds"], "Additional Needs are not matched"

        get_booking = auth.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Error to get booking with ID: {booking_id}"
        booking_get_response = get_booking.json()

        assert booking_get_response["firstname"] == booking_update_data["firstname"], "Name is not matched"
        assert booking_get_response["lastname"] == booking_update_data["lastname"], "Surname is not matched"
        assert booking_get_response["totalprice"] == booking_update_data["totalprice"], "Total Price is not matched"
        assert booking_get_response["depositpaid"] == booking_update_data["depositpaid"], "Deposit Paid is not matched"
        assert booking_get_response["bookingdates"]["checkin"] == booking_update_data["bookingdates"]["checkin"], "Checkin Date is not matched"
        assert booking_get_response["bookingdates"]["checkout"] == booking_update_data["bookingdates"]["checkout"], "Checkout Date is not matched"
        assert booking_get_response["additionalneeds"] == booking_update_data["additionalneeds"], "Additional Needs are not matched"

        delete_booking = auth.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Error to delete booking with ID:{booking_id}"

        check_delete_response = auth.get(f"{BASE_URL}/booking/{booking_id}")
        assert check_delete_response.status_code == 404, f"Booking with ID: {booking_id} was not deleted"

    def test_get_booking_with_firstname(self, auth, booking_data):
        create_booking = auth.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Create Error"
        booking_create_response = create_booking.json()
        booking_id = booking_create_response.get("bookingid")
        booking_firstname = booking_create_response["booking"]["firstname"]
        assert booking_id is not None, "ID is not Found"

        get_booking = auth.get(f"{BASE_URL}/booking?firstname={booking_firstname}")
        get_booking_response = get_booking.json()
        assert booking_id in [item["bookingid"] for item in get_booking_response], f"ID {booking_id} not found in response"

    def test_get_booking_with_lastname(self, auth, booking_data):
        create_booking = auth.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Create Error"
        booking_create_response = create_booking.json()
        booking_id = booking_create_response.get("bookingid")
        booking_lastname = booking_create_response["booking"]["lastname"]
        assert booking_id is not None, "ID is not Found"

        print(booking_lastname)
        get_booking = auth.get(f"{BASE_URL}/booking?lastname={booking_lastname}")
        get_booking_response = get_booking.json()
        assert booking_id in [item["bookingid"] for item in get_booking_response], f"ID {booking_id} not found in response"

    def test_get_booking_with_checkin(self, auth, booking_data):
        booking_data.update()
        create_booking = auth.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Create Error"
        booking_create_response = create_booking.json()
        booking_id = booking_create_response.get("bookingid")
        booking_checkin = booking_create_response["booking"]["bookingdates"]["checkin"]
        assert booking_id is not None, "ID is not Found"

        get_booking = auth.get(f"{BASE_URL}/booking?checkin={booking_checkin}")
        get_booking_response = get_booking.json()
        assert booking_id in [item["bookingid"] for item in get_booking_response], f"ID {booking_id} not found in response" # Тут найден баг - не отображается ID созданного букинга в списке

    def test_get_booking_with_checkout(self, auth, booking_data):
        booking_data.update()
        create_booking = auth.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Create Error"
        booking_create_response = create_booking.json()
        booking_id = booking_create_response.get("bookingid")
        booking_checkout = booking_create_response["booking"]["bookingdates"]["checkout"]
        assert booking_id is not None, "ID is not Found"

        print(booking_checkout)
        print(booking_id)
        get_booking = auth.get(f"{BASE_URL}/booking?checkout={booking_checkout}")
        get_booking_response = get_booking.json()
        print(get_booking_response)
        assert booking_id in [item["bookingid"] for item in get_booking_response], f"ID {booking_id} not found in response"

    def test_get_all_bookings(self, auth, booking_data):
        create_booking = auth.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Create Error"
        booking_create_response = create_booking.json()
        booking_id = booking_create_response.get("bookingid")
        assert booking_id is not None, "ID is not Found"

        get_all_bookings = auth.get(f"{BASE_URL}/booking")
        get_all_bookings_response = get_all_bookings.json()
        assert get_all_bookings.status_code == 200, "Status code not 200"
        assert get_all_bookings_response != [], "Response is empty"

        delete_booking = auth.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Error to delete booking with ID:{booking_id}"

        check_delete_response = auth.get(f"{BASE_URL}/booking/{booking_id}")
        assert check_delete_response.status_code == 404, f"Booking with ID: {booking_id} was not deleted"

    def test_delete_without_auth(self, auth, booking_data, unauthorized_session):
        create_booking = auth.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Create Error"
        booking_create_response = create_booking.json()
        booking_id = booking_create_response.get("bookingid")
        assert booking_id is not None, "ID is not Found"

        delete_booking = unauthorized_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 403, f"Booking deleted without auth:{booking_id}"
















# https://restful-booker.herokuapp.com/booking?checkin=2025-04-15