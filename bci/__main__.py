# import click
# from . import server, client
# from .utils import my_util_functions as my_utils
#
#
# @click.group()
# def cli():
#     pass
#
#
# @cli.command()
# @click.option('--address', default="127.0.0.1:8000", help='address in a format of ip:port')
# @click.option('--sample_path', default="./bci/data", help='path of the mind sample')
# def run_client(address, sample_path):
#     ip, port = address.split(":")
#     formatted_address = (ip, int(port))
#     try:
#         client.run(formatted_address, sample_path)
#     except Exception as error:
#         print(f'ERROR: {error}')
#     pass
#
#
# @cli.command()
# @click.option('--address', default="127.0.0.1:8000", help='address in a format of ip:port')
# # @click.option('--data_dir', default=".", help='data dir')
# def run_server(address):
#     host, port = address.split(':')
#     formatted_address = (host, int(port))
#     try:
#         server.run(formatted_address)
#     except KeyboardInterrupt:
#         print('Server terminated by user (KeyboardInterrupt)')
#
#
# if __name__ == '__main__':
#     my_utils.init_logger("client_server")
#     cli(prog_name='bci')
