import time
from api.login import logger
from typing import Awaitable
from fastapi import Response, Request
from starlette.middleware.base import BaseHTTPMiddleware


class ProcessingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next:[[Request], Awaitable[Response]]) -> Response:
        start_time = time.time()
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        logger.info(f"Processing time: {process_time}")
        return response