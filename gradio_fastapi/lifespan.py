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
        tunnel = setup_tunnel("localhost", port, secrets.token_urlsafe(32), None)
        try:
            address = tunnel.start_tunnel()
            logger.info(f"Running on public URL: {address}")
        except Exception as e:
            logger.error(f"Unable to start Gradio tunnel: {str(e)}")
        if lifespan:
            yield next(lifespan(app))
        else:
            yield

        if tunnel.proc is not None:
            logger.info(f"Killing Gradio tunnel {tunnel.local_host}:{tunnel.local_port} <> {tunnel.url}")
            tunnel.kill()

    return out_lifespan
