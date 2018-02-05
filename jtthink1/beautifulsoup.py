from bs4 import BeautifulSoup

soup = BeautifulSoup("""
<html>
    <head>test</head>
    <body>
        this is my html
    </body>
</html>
""", "html.parser");

print(soup.html.head);
