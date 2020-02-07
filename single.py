from download import setup_download_dir, get_links, download_link
import logging
import os
from rq import Queue
from time import time
from redis import Redis
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



def main():
    ts = time()
    client_id = os.getenv('client_id')
    if not client_id:
        raise Exception("Couldn't find client_id environment variable!")
    download_dir = setup_download_dir()
    links = get_links(client_id)
    q = Queue(connection=Redis(host='localhost', port=6532))
    for link in links:
       q.enqueue(download_link, download_dir, link)

if __name__ == "__main__":
    main()
