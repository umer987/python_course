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
     @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        """Create a Product instance from dictionary data."""
        return cls(
            sku=data["sku"],
            name=data["name"],
            description=data["description"],
            category=data["category"],
            quantity=data["quantity"],
            min_quantity=data["min_quantity"],
            max_quantity=data["max_quantity"],
            cost_price=Decimal(data["cost_price"]),
            selling_price=Decimal(data["selling_price"]),
            supplier=data["supplier"],
            location=data["location"],
            barcode=data["barcode"],
            weight=data["weight"],
            dimensions=data["dimensions"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            tags=data.get("tags", []),
            images=data.get("images", []),
            reviews=data.get("reviews", []),
            sales_history=data.get("sales_history", [])
        )
    
def is_low_stock(self) -> bool:
        """Check if product is below minimum quantity."""
        return self.quantity <= self.min_quantity
    
    def is_overstocked(self) -> bool:
        """Check if product exceeds maximum quantity."""
        return self.quantity >= self.max_quantity
    
    def calculate_profit_margin(self) -> Decimal:
        """Calculate profit margin percentage."""
        if self.selling_price == 0:
            return Decimal('0')
        profit = self.selling_price - self.cost_price
        return (profit / self.selling_price * Decimal('100')).quantize(Decimal('0.01'), ROUND_HALF_UP)
