from utils.response import Response

def body_parser(request):

  res = Response()
  # Split request by the return / newline
  req = request.split("\r\n")

  # Break apart the status line into status, method, and originalUrl
  res.status = req.pop(0)
  res.method = res.status.split(" ")[0]
  res.original_url = res.status.split(" ")[1]

  # Get query and arguments if they exist in the request
  if "?" in res.original_url:

    # Break apart the original url into path, query, and params
    res.path = res.original_url.split("?")[0]
    res.query = res.original_url.split("?")[1]
    res.params = dict(x.split("=") for x in res.query.split("&"))

  else:

    # Set the path as the original url because there's no query or params
    res.path = res.original_url

  # Get the hostname from the headers
  res.hostname = [s for s in req if "Host:" in s].pop().replace("Host: ", "")
  
  # Get the content type from the headers if it exists
  try:
    res.content_type = [s for s in req if "Content-Type:" in s].pop().replace("Content-Type: ", "")
  except:
    res.content_type = "text/html"

  res.body = request.split("\r\n\r\n")[1]

  return res

