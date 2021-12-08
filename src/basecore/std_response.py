from typing import Dict, Any, Tuple


def create_std_response(
        result: Dict[str, Any] = None,
        error_detail: Tuple[Any, ...] = None,
        total_count: int = 0) -> Dict[str, Any]:
    return {
        'data': {
            'error_detail': error_detail,
            'result': result,
            'total_count': total_count
        }
    }
