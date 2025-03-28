from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from anvil.tables import app_tables
import anvil.users


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.product = app_tables.products.search(Amount=10)[0]['Name']
    self.init_components(**properties)
    anvil.users.login_with_form()
    # Any code you write here will run before the form opens.
