import os, requests, logging

logging.basicConfig(level=logging.DEBUG)

def token(request):
    auth = request.headers.get("Authorization")#request.authorization

    logging.debug(auth)

    token = request.headers.get("Authorization")

    if not token:
        return None, ("missing credentials", 401)

    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/validate",
        headers={"Authorization": token},
    )
    logging.debug(response)

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)