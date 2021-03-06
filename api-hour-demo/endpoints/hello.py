import logging
import asyncio

from api_hour.plugins.aiohttp import JSON


LOG = logging.getLogger(__name__)

"""
You handle inputs with outside world here
"""

async def hello(request):
    return JSON({
        'index': 'hello!'
    })

# Endpoint example with a Service

# from ..services.hello import get_random_record
#
# async def db(request):
#     """Test type 2: Single database query"""
#     container = request.app['ah_container']
#
#     return JSON((await get_random_record(container)))
#
