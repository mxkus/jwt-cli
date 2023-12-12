# pip install click
# pip install pygments
import base64
import json
import click
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter


@click.command()
@click.argument("token")
def decode_jwt(token):
    try:
        tt = token.split(".")
        header = base64.b64decode(tt[0] + "==")
        payload = base64.b64decode(tt[1] + "==")
        signature = base64.b64decode(tt[2] + "==")

        click.echo("\nDecoded JWT Elements:")
        click.echo("\nHeader:")
        click.echo(highlight(json.dumps(json.loads(header), indent=2), JsonLexer(), TerminalFormatter()))

        click.echo("\nPayload:")
        click.echo(highlight(json.dumps(json.loads(payload), indent=2), JsonLexer(), TerminalFormatter()))

        click.echo("\nSignature:")
        click.echo(highlight(json.dumps({"signature": str(signature)}, indent=2), JsonLexer(), TerminalFormatter()))

    except Exception as e:
        click.echo(f"Error decoding JWT: {str(e)}", err=True)


if __name__ == "__main__":
    decode_jwt()
