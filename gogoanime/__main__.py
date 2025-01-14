import click
from gogoanime.download import download

@click.command()
@click.argument('url', required=True)
@click.option('--output', '-o', default='.', help='Directory to save the anime.')
@click.option('--quality', '-q', default='720p', help='Video quality (e.g., 720p, 1080p).')


def main(url, output, quality):



    # url = 'https://ggredi.info/download.php?url=aHR0cHM6LyAdeqwrwedffryretgsdFrsftrsvfsfsr9odGd0c2AawehyfcghysfdsDGDYdgdsfsdfwstdgdsgtertR0cXZsLmFuZjU5OC5jb20vdXNlcjEzNDIvNTMxOGJhZDQ4YWQ2MTQ0MThhOWZlMTIwMzg5NmJjMzUvRVAuMS52MC4xNzI4MTQ1NTA2LjEwODBwLm1wND90b2tlbj1rT2thTmFoaG5nNENsMk9FckVYSDRnJmV4cGlyZXM9MTczNDI1NTY5NCZpZD0yMzQzODQmdGl0bGU9KDE5MjB4MTA4MC1nb2dvYW5pbWUpYmxlYWNoLXNlbm5lbi1rZXNzZW4taGVuLXNvdWtva3UtdGFuLWVwaXNvZGUtMS5tcDQ='
    # path = "video/file2.mp4"
    download(url, output)


if __name__ == "__main__":
    main()