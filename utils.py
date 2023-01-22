from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = kavenegarAPI('6C69334F6B764F714559675A4F6C4A4C7949624A4646586B66426F6C2B547061384F446F473252553175513D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'{code}کد تایید شما '
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
