# Copyright (c) 2023, Atharva and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class user_activities(WebsiteGenerator):
	def before_save(self):
		self.route = self.activity_form 
