from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from app.schemas import CommonResponseSchema, DataResponseSchema, UserResponseSchema
from app.service import SampleService
from app.utils import logger

private_router = APIRouter(prefix="/private", tags=["Sample"])


@private_router.get("/ping", tags=["Health Check"])
def ping():
    function_name = "Ping Private Route- Health Check"
    logger.info(
        message=f"Enter - {function_name}",
        function_name=function_name,
    )
    return JSONResponse(
        CommonResponseSchema(message="Health check ping working for private route", status="Ok").dict(),
        status_code=status.HTTP_200_OK,
    )


@private_router.get("/get-all-users", tags=["User"])
def get_all_users():
    function_name = "Get All Users - Controller"
    logger.info(
        message=f"Enter - {function_name}",
        function_name=function_name,
    )
    try:
        users: list[UserResponseSchema] = SampleService().get_all_users()
        logger.info(
            message=f"Exit - {function_name}",
            function_name=function_name,
        )
        return JSONResponse(
            DataResponseSchema(message="Users fetched successfully", status="Ok", data=users).dict(),
            status_code=status.HTTP_200_OK,
        )
    except Exception as exception:
        logger.error(
            message=f"Exit - {function_name} - Exception Occurred: {exception}",
            function_name=function_name,
        )
        return JSONResponse(
            CommonResponseSchema(message="Health check ping working for private route", status="Ok").dict(),
            status_code=status.HTTP_200_OK,
        )
