class Response():
  def __init__(self, **items):
    for i in items: 

      if items[i] == "status":
        self.status = items[i]
      else:
        self.status = ""

      if items[i] == "original_url":
        self.original_url = items[i]
      else:
        self.original_url = ""

      if items[i] == "hostname":
        self.hostname = items[i]
      else:
        self.hostname = ""

      if items[i] == "content_type":
        self.content_type = items[i]
      else:
        self.content_type = ""

      if items[i] == "path":
        self.path = items[i]
      else:
        self.path = ""

      if items[i] == "query":
        self.query = items[i]
      else:
        self.query = ""

      if items[i] == "params":
        self.params = items[i]
      else:
        self.params = ""
  
  def get_status(self):
    return self.status

  def set_status(self, value):
    self.status = value

  def get_method(self):
    return self.method

  def set_method(self, value):
    self.method = value

  def get_original_url(self):
    return self.original_url

  def set_original_url(self, value):
    self.original_url = value

  def get_hostname(self):
    return self.hostname

  def set_hostname(self, value):
    self.hostname = value

  def get_content_type(self):
    return self.content_type

  def set_content_type(self, value):
    self.content_type = value

  def get_path(self):
    return self.path

  def set_path(self, value):
    self.path = value

  def get_query(self):
    return self.query

  def set_query(self, value):
    self.query = value

  def get_params(self):
    return self.params

  def set_params(self, value):
    self.params = value