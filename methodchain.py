class A:
    _prop = None

    def __init__(self, payload: str):
        self._prop = payload
        print(f"program {self._prop}")

    def authenticate(self, payload: str):
        self._prop = payload
        print(f"{a._prop}")
        return self

    def authorize(self, payload: str):
        self._prop = payload
        print(f"{a._prop}")
        return self

    def validate(self, payload: str):
        self._prop = payload
        print(f"{a._prop}")
        return self

    def cache(self, payload: str):
        self._prop = payload
        print(f"{a._prop}")
        return self


if __name__ == "__main__":
    a = A("starts")
    a.authenticate("auth requested").authorize(
        "authorize requested").validate("validation requested").cache("cache requested")
