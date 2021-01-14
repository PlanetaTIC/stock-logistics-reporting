# Copyright 2020 PlanetaTIC <info@planetatic.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Valued Picking Group Report",
    "summary": "Adding Valued Picking Group on Delivery Slip report",
    "version": "12.0.1.0.0",
    "author": "PlanetaTIC, "
              "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/stock-logistics-reporting",
    "category": "Warehouse Management",
    "license": "AGPL-3",
    "depends": [
        "stock_picking_report_valued",
        "stock_picking_group",
    ],
    "data": [
        'report/stock_picking_group_report_valued.xml',
    ],
    "installable": True,
}
