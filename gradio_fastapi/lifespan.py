import logging
import secrets
from typing import Callable
from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.types import Lifespan

from gradio_fastapi.tunneling import setup_tunnel



def gradio_lifespan_init(lifespan=None, port=8000) -> Callable[[FastAPI], Lifespan]:
    """
    Lifespan initializer that sets up a tunnel to a public Gradio URL linked the given port.

    This initializer also acts as a wrapper to any lifespan you already have defined.

    If there's no lifespan defined, simply set the lifespan of your FastAPI app like so:
    ```
    app = FastAPI(lifespan=gradio_lifespan_init())
    ```
    Otherwise:
    ```
    app = FastAPI(lifespan=gradio_lifespan_init(lifespan))
    ```
    """
    @asynccontextmanager
    async def out_lifespan(app: FastAPI):
        logger = logging.getLogger("uvicorn.error")
        logger.info("Setting up Gradio tunnel...")
        address = setup_tunnel("localhost", port, secrets.token_urlsafe(32), None)
        logger.info(f"Running on public URL: {address}")
        if lifespan:
            yield next(lifespan(app))
        else:
            yield

    return out_lifespan
