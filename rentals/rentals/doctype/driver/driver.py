# Copyright (c) 2026, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Driver(Document):
    pass
    # def autoname(self):
    #     if self.age>0:
    #         frappe.throw("Age")
    # def before_save(self):
    #     if self.last_name:
    #         self.full_name = f"{self.first_name} {self.last_name}"
    #     else:
    #         self.full_name = self.first_name
    # def send_alert(self):
    #     print("sending message")