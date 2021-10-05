def create_std_response(result: dict = None, error_code: int = None, total_count: int = 0) -> dict:
    return {
        'data': {
            'error': error_code,
            'result': result,
            'total_count': total_count
        }
    }
