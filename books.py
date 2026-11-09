import argparse
import json

def search_books(query, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [b for b in data if query in b.get('author', '') or query in b.get('title', '')]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Поиск книг")
    parser.add_argument('action', choices=['search'])
    parser.add_argument('query', help="Поисковый запрос")
    parser.add_argument('file', help="JSON файл с базой")
    args = parser.parse_args()

    if args.action == 'search':
        results = search_books(args.query, args.file)
        print(results)