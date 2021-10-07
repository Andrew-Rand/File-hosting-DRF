from typing import Dict, Any


def create_std_response(result: dict = None, status_code: int = None, info: Dict[str, Any] = None, total_count: int = 0) -> dict:
    return {
        'data': {
            'status_code': status_code,
            'info': info,
            'result': result,
            'total_count': total_count
        }
    }
