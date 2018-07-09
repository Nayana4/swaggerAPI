#!/usr/bin/env python3

import connexion

from fenet_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'MetaData'})
    app.run(port=5000)


if __name__ == '__main__':
    main()
