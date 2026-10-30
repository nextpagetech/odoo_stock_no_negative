{
    "name": "Stock No Negative",
    "version": "18.0.1.0.2",
    "category": "Inventory",
    "license": "AGPL-3",
    "summary": "Prevent negative stock with product, category and location exceptions",
    "description": """
Prevent stockable products from going negative during inventory operations.
Stock validation is blocked when an internal or transit location would become
negative, while controlled exceptions can be enabled by product, product
category, or stock location.

This distribution is based on the OCA stock_no_negative module originally
authored by Akretion and maintained in the Odoo Community Association ecosystem.
""",
    "author": "Next Page Technologies Pvt Ltd, Akretion, OCA",
    "maintainer": "Next Page Technologies Pvt Ltd",
    "website": "https://nextpagetechnologies.com",
    "support": "hello@nextpagetechnologies.com",
    "depends": ["stock"],
    "data": [
        "views/product_product_views.xml",
        "views/stock_location_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
