from typing import Any, Optional

import pydantic


class CommonResponseSchema(pydantic.BaseModel):
    message: str
    status: str


class ErrorResponseSchema(CommonResponseSchema):
    error_details: str


class DataResponseSchema(CommonResponseSchema):
    data: Optional[Any]
