from typing import Any

from django.core.exceptions import ValidationError


class JpgSignature:
    jpg_format = "jpg"
    jpg_signature = ("FF D8 FF E0", "FF D8 FF E1", "FF D8 FF E2", "FF D8 FF E8")
    jpg_offset_signature = 0  # смещение сигнатуры относительно начала файла


def validate_typefile(value: Any) -> bool:
    file_to_validate = value.read(32)
    hex_file = " ".join(['{:02X}'.format(byte) for byte in file_to_validate])

    validation_res = []

    for signature in JpgSignature.jpg_signature:
        offset = JpgSignature.jpg_offset_signature * 2 + JpgSignature.jpg_offset_signature  # 2chars for bytes + number of whitespaces between bytes
        if signature == hex_file[offset:len(signature) + offset].upper():
            validation_res.append(JpgSignature.jpg_format)
    return not validation_res == []
