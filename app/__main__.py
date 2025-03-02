from app.services import TechnoStore
from app.config import config
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Запуск приложения с параметром debug.')
    parser.add_argument('--debug', action='store_true', help='Запустить приложение в режиме debug.')
    args = parser.parse_args()
    techno_store: TechnoStore = TechnoStore(config=config)
    techno_store.run(debug=args.debug)

