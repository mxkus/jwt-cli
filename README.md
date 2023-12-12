# jwt.py

This is a Python script that decodes JWT (JSON Web Tokens). It uses the `click` library for command-line interfaces and `pygments` for syntax highlighting.

## Installation

Before running the script, you need to install the required Python packages. You can do this by running the following commands:

```bash
pip install click
pip install pygments
```

## Usage
You can use this script from the command line by passing a JWT as an argument. Here's an example:
```bash
python jwt.py <your-jwt-token>
```

The script will then decode the JWT and print the header, payload, and signature in a nicely formatted and colorized JSON format.

## Example
The example unfortunately doesn't show the highlighting :D But trust me.
### Code
```bash
$ python jwt.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

Decoded JWT Elements:

Header:
{
  "alg": "HS256",
  "typ": "JWT"
}


Payload:
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}


Signature:
{
  "signature": "b'I\\xf9J\\xc7\\x04IH\\xc7\\x8a(]\\x90O\\x87\\xf0\\xa4\\xc7\\x89\\x7f~\\x8f:N\\xb2%V\\x9dB\\xcb0\\xe5'"
}
```
