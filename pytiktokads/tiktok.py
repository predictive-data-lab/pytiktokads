import logging
from typing import Optional, Iterable, ClassVar, Any, List, Callable
from urllib.parse import urljoin, urlencode
import requests
import enum
import aiohttp 

BASE_URL = 'https://ads.tiktok.com/open_api/'
VERSION = 'v1.3'  # API version

class TikTokAds:
    logger: logging.Logger = logging.getLogger(__name__)

    def __init__(
            self,
            access_token