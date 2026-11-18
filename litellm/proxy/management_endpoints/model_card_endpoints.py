"""
Fetch a model card (README / JSON metadata) from a provider URL so the admin UI can show it.
"""

from typing import Final

import httpx
from fastapi import APIRouter, Query
from fastapi.responses import PlainTextResponse

router: Final = APIRouter()


@router.get(
    "/model/card/fetch",
    tags=["model management"],
    response_class=PlainTextResponse,
)
async def fetch_model_card(url: str = Query(..., description="Model card URL")):
    """
    Return the raw model card found at `url`.
    """
    async with httpx.AsyncClient(follow_redirects=True, timeout=10) as client:
        resp = await client.get(url)
    return PlainTextResponse(resp.text, status_code=resp.status_code)
