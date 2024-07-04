class SecurityHeader:

    def __init__(self, name, recommend_message, security_score, safe_value):
        self.name = name
        self.recommend_message = recommend_message
        self.security_score = security_score
        self.safe_value = safe_value

    def check(self, headers: dict) -> (bool, str):
        if self.name in headers:
            if headers[self.name] in self.safe_value:
                return True, f"{self.name} is enable."
            return False, self.recommend_message
        return False, f"{self.name} is missing. {self.recommend_message}"
