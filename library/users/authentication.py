from knox.auth import TokenAuthentication


class BearerAuthentication(TokenAuthentication):
    keyword = 'Bearer'
