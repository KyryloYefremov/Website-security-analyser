import json

from security_header import SecurityHeader


class HeadersList:

    def __init__(self, filepath: str):
        self.headers: list[SecurityHeader] = []
        self.load_headers(filepath)

    def load_headers(self, filepath):
        try:
            with open(filepath, 'r') as file:
                headers_data = json.load(file)
                for header in headers_data:
                    security_header = SecurityHeader(
                        name=header["name"],
                        recommend_message=header["recommendation"],
                        security_score=header["security_score"],
                        safe_value=header["safe_value"]
                    )
                    self.headers.append(security_header)

        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON file: {filepath}")

    def check_headers(self, headers: dict) -> dict:
        report = {
            "total_score": 0,
            "max_score": 0,
            "messages": []
        }

        for header in self.headers:
            is_safe, message = header.check(headers)
            report["messages"].append({
                "name": header.name,
                "is_safe": is_safe,
                "message": message
            })
            if is_safe:
                report["total_score"] += header.security_score
            report["max_score"] += header.security_score

        return report
