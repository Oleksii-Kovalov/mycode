

def app(environ, start_response):
        import pprint
        pprint.pprint(environ)

        data = b"""<html>
        
        <body>
        <form action="/" method="post">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <label for="lname">Last name:</label>
  <input type="text" id="lname" name="lname"><br><br>
  <input type="submit" value="Submit">
</form>
</body>
</html>
        """





        start_response("200 OK", [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])
