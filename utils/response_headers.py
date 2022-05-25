import datetime

def response_headers(body, content_type="text/html"):
  s = ''
  s = s + f'HTTP/1.1 200 OK\n'
  s = s + f'Date: {datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")} GMT\n'
  s = s + f'Server: Sumerian Server v1.0\n'
  s = s + f'Content-Type: {content_type}\n'
  s = s + f'Content-Length: {len(body)}\n\n'

  return s