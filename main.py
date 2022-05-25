import json
import os
import sys

from utils.tcp_socket import TcpSocket
from utils.body_parser import body_parser
from utils.response_headers import response_headers
from utils.clear_terminal import clear_terminal
from utils.watch_signal import watch_signal

clear_terminal()
watch_signal()

host = "0.0.0.0"
port = 8001
argv = sys.argv[1:]

options = []
i = int(0)

# Separate argv into option and value pairs
while i < len(argv):
  start = int(i)
  end   = int(i) + 1
  try:
    options.append((argv[start], argv[end]))
  except:
    break
  i = i + 2

# Separate the option and values and check for
# port and host to assign new override values
try:
  for option, value in options:
    # Check and assign port
    if option in ['-p', '--port', 'port']:
      port = int(value)
    # Check and assign host
    if option in ['-h', '--host', 'host']:
      host = str(value)
except:
  print("Error Message ")

tcp = TcpSocket(host, port)
server = tcp.server

# This is for rotating the index pages on each request
current_index = 0
index_pages = ["index1.html", "index2.html", "index3.html"]

# Waiting for an incoming client request
while True:    

  content_type = None

  # Accept incoming client request 
  client_connection, client_address = server.accept()
  print(f"Client: Connected on {client_address[0]}:{client_address[1]}")

  # Get the host 1024 bytes from the buffer and decode
  request = client_connection.recv(1024).decode()
  print(f'\n{request}')

  # This is where you would parse through the request to get the headers
  # and the body of the request where your data might be
  req = body_parser(request)

  # Get the content body ready to respond to client request
  # Either a json, html, html with parsed parameter heading
  # or just a plain message with Hello World
  if req.content_type == "application/json":
    body = {"data": {"message": "Hello World"}}
    body = json.dumps(body)
  elif req.path == "/favicon.ico":
    try:
      with open("favicon.ico", "rb") as file:
        length = os.path.getsize("favicon.ico")
        body = file.read()
        content_type = "image/x-icon"
    except:
      print("Error: Unable to read image")
  else:
    # Select index page
    html_page = index_pages[current_index]
    # Increment current index or reset to zero
    if current_index < len(index_pages)-1:
      current_index = current_index + 1
    else:
      current_index = 0

    try:
      with open(html_page, "r", encoding = 'utf-8') as file:
        body = file.read()
        content_type = "text/html"
    except:
      body = 'Hello World!'

    # Replace {{ HEADING }} in html if parameter heading exists
    # else replace with default values
    if hasattr(req, "params"):
      for k in req.params.keys():
        if k.lower() == "heading":
          # Set and sanitize heading param
          h = req.params["heading"]
          h = h.replace("%20", " ") # space
          h = h.replace("%27", "'") # quote
          h = h.replace("%22", '"') # quotes
          new_heading = h
          body = body.replace("{{ HEADING }}", new_heading)
    else:
      # html pages still have {{ HEADING }} in them and there was
      # no heading parameter passed so set with default values
      if html_page == "index1.html":
        body = body.replace("{{ HEADING }}", "Architects")  

      if html_page == "index2.html":
        body = body.replace("{{ HEADING }}", "Gourmet au Catering")

      if html_page == "index3.html":
        body = body.replace("{{ HEADING }}", "COMING SOON")
  
  if content_type == None:
    if hasattr(req, "content_type"):
      content_type = req.content_type
    else:
      content_type = "text/html"

  # Generate relevant response headers
  headers = response_headers(body, content_type)

  # Combine the headers with the body content
  response = f"{headers}{body}\n\n"

  # Don't print response if it's serving the index.html page
  if content_type != "text/html" and content_type != "image/x-icon":
    print(response)

  # Send response to the client and close the connection
  client_connection.sendall(response.encode())
  client_connection.close()
  print(f'Client: Disconnected {client_address[0]}:{client_address[1]}')
