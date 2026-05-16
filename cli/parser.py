import argparse
from cli.commands import handle_history, handle_token, handle_upload , handle_version

def create_parser():
    parser = argparse.ArgumentParser(description="GoFile CLI Application")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    version_parser = subparsers.add_parser("version", help="Show the version of the application")
    version_parser.add_argument("--version", action="version", version="GoFile CLI 1.0")
    version_parser.set_defaults(func=handle_version)  # No action needed, version is handled by argparse

    upload_parser = subparsers.add_parser("upload", help="Upload a file directly from the command line")
    upload_parser.add_argument("file_path", metavar="FILE_PATH", help="Path to the file to upload")
    upload_parser.set_defaults(func=handle_upload)  # You would need to implement handle_upload in commands.py

    history_parser = subparsers.add_parser("history", help="View upload history directly from the command line")
    history_parser.set_defaults(func=handle_history)

    token_parser = subparsers.add_parser("token", help="Set API token directly from the command line")
    token_parser.add_argument("api_token", metavar="API_TOKEN", help="The API token to set")
    token_parser.set_defaults(func=handle_token)

    return parser