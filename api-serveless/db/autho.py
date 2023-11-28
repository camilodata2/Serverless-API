class AuthHandler:
    def __init__(self):
        self.error = None
        self.status_code = None
        self.token = None
        self.payload = None
        self.rsa_key = None

    def handle_auth_error(self):
        response = jsonify(self.error)
        response.status_code = self.status_code
        return response

    def get_token_auth_header(self, app):
        """Obtains the Access Token from the Authorization Header
        """
        request = app.current_request
        auth = request.headers.get("Authorization", None)
        if not auth:
            self.error = {"code": "authorization_header_missing",
                          "description": "Authorization header is expected"}
            self.status_code = 401
            raise AuthError(self.error, self.status_code)

        parts = auth.split()

        if parts[0].lower() != "bearer":
            self.error = {"code": "invalid_header",
                          "description": "Authorization header must start with Bearer"}
            self.status_code = 401
            raise AuthError(self.error, self.status_code)
        elif len(parts) == 1:
            self.error = {"code": "invalid_header",
                          "description": "Token not found"}
            self.status_code = 401
            raise AuthError(self.error, self.status_code)
        elif len(parts) > 2:
            self.error = {"code": "invalid_header",
                          "description": "Authorization header must be Bearer token"}
            self.status_code = 401
            raise AuthError(self.error, self.status_code)

        self.token = parts[1]
        return self.token

    def requires_auth(self, f, app):
        """Determines if the Access Token is valid
        """
        @wraps(f)
        def decorated(*args, **kwargs):
            self.get_token_auth_header(app)
            jsonurl = urlopen("https://" + AUTH0_DOMAIN + "/.well-known/jwks.json")
            jwks = json.loads(jsonurl.read())
            unverified_header = jwt.get_unverified_header(self.token)
            self.rsa_key = {}
            for key in jwks["keys"]:
                if key["kid"] == unverified_header["kid"]:
                    self.rsa_key = {
                        "kty": key["kty"],
                        "kid": key["kid"],
                        "use": key["use"],
                        "n": key["n"],
                        "e": key["e"]
                    }
            if self.rsa_key:
                try:
                    self.payload = jwt.decode(
                        self.token,
                        self.rsa_key,
                        algorithms=ALGORITHMS,
                        audience=API_AUDIENCE,
                        issuer="https://" + AUTH0_DOMAIN + "/"
                    )
                except jwt.ExpiredSignatureError:
                    self.error = {"code": "token_expired",
                                  "description": "token is expired"}
                    self.status_code = 401
                    raise AuthError(self.error, self.status_code)
                except jwt.JWTClaimsError:
                    self.error = {"code": "invalid_claims",
                                  "description": "incorrect claims, please check the audience and issuer"}
                    self.status_code = 401
                    raise AuthError(self.error, self.status_code)
                except Exception:
                    self.error = {"code": "invalid_header",
                                  "description": "Unable to parse authentication token."}
                    self.status_code = 401
                    raise AuthError(self.error, self.status_code)

                app.current_request.context.update(self.payload)
                return f(*args, **kwargs)
            self.error = {"code": "invalid_header",
                          "description": "Unable to find appropriate key"}
            self.status_code = 401
            raise AuthError(self.error, self.status_code)

        return decorated
