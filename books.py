import argparse
import json

def search_books(query, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [b for b in data if query.lower() in b.get('author', '').lower() or query.lower() in b.get('title', '').lower()]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Поиск книг")
    parser.add_argument('action', choices=['search'])
    parser.add_argument('query', help="Поисковый запрос")
    parser.add_argument('file', help="JSON файл с базой")
    args = parser.parse_args()

    if args.action == 'search':
        results = search_books(args.query, args.file)
        print(results)