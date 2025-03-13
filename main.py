from utils import get_top_hacker_news
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    stories = get_top_hacker_news()
    logger.info(stories)

if __name__ == "__main__":
    main()
