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
def add_review(self, customer: str, rating: int, comment: str) -> None:
        """Add a customer review."""
        self.reviews.append({
            "customer": customer,
            "rating": rating,
            "comment": comment,
            "date": datetime.now().isoformat()
        })
    
    def get_average_rating(self) -> float:
        """Calculate average rating from reviews."""
        if not self.reviews:
            return 0.0
        total = sum(r["rating"] for r in self.reviews)
        return round(total / len(self.reviews), 1)

class InventoryManager:
    """Manages inventory operations with advanced features."""
    
    def __init__(self, data_file: str = "inventory.json"):
        self.data_file = data_file
        self.products: Dict[str, Product] = {}
        self.transactions: List[Dict] = []
        self.load_data()
        self._generate_barcodes()
    
    def _generate_barcodes(self) -> None:
        """Generate missing barcodes for products."""
        for product in self.products.values():
            if not product.barcode:
                product.barcode = self.generate_barcode()
        self.save_data()
@staticmethod
    def generate_barcode() -> str:
        """Generate a random 12-digit barcode."""
        return ''.join(random.choices(string.digits, k=12))
    
    @staticmethod
    def generate_sku(category: str, name: str) -> str:
        """Generate a SKU from category and name."""
        prefix = category[:3].upper()
        name_part = ''.join(word[0].upper() for word in name.split()[:2])
        random_part = ''.join(random.choices(string.digits, k=4))
        return f"{prefix}-{name_part}-{random_part}"
    def add_product(self, product: Product) -> bool:
        """Add a new product to inventory."""
        if product.sku in self.products:
            return False
        self.products[product.sku] = product
        self.save_data()
        return True
    
    def get_product(self, sku: str) -> Optional[Product]:
        """Retrieve a product by SKU."""
        return self.products.get(sku)

  def get_product_by_barcode(self, barcode: str) -> Optional[Product]:
        """Find product by barcode."""
        for product in self.products.values():
            if product.barcode == barcode:
                return product
        return None


     old_quantity = product.quantity
        product.quantity = quantity
        product.updated_at = datetime.now().isoformat()
        
        # Log transaction
        self.transactions.append({
            "sku": sku,
            "product_name": product.name,
            "type": transaction_type,
            "old_quantity": old_quantity,
            "new_quantity": quantity,
            "change": quantity - old_quantity,
            "timestamp": datetime.now().isoformat(),
            "user": "system"
        })
    
    def update_quantity(self, sku: str, quantity: int, transaction_type: str = "adjustment") -> bool:
        """Update product quantity and log transaction."""
        product = self.get_product(sku)
        if not product:
            return False
 self.save_data()
        return True
    
    def add_stock(self, sku: str, amount: int) -> bool:
        """Add stock to a product."""
        product = self.get_product(sku)
        if not product:
            return False
        new_quantity = product.quantity + amount
        return self.update_quantity(sku, new_quantity, "restock")
    
