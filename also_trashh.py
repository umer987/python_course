import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP
from collections import defaultdict
import hashlib
import random
import string

@dataclass
class Product:
    """Represents a product in the inventory."""
    sku: str
    name: str
    description: str
    category: str
    quantity: int
    min_quantity: int
    max_quantity: int
    cost_price: Decimal
    selling_price: Decimal
    supplier: str
    location: str
    barcode: str
    weight: float
    dimensions: str
    created_at: str
    updated_at: str
    tags: List[str] = field(default_factory=list)
    images: List[str] = field(default_factory=list)
    reviews: List[Dict] = field(default_factory=list)
    sales_history: List[Dict] = field(default_factory=list)
    
