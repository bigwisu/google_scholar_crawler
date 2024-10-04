"""
Google Scholar crawler using scholarly and scraperapi. 
Modified and corrected by Wisu Suntoyo from original code by Byunghyun Ban.
"""

from scholarly import scholarly as S
from scholarly import ProxyGenerator

# You should issue your API key from https://www.scraperapi.com/
SCRAPER_API_KEY = "YOUR SCRAPER API KEY"

def _set_new_proxy():
    """
    Set new proxy by using scraperapi.com
    """
    pg = ProxyGenerator()
    success = pg.ScraperAPI(SCRAPER_API_KEY)
    S.use_proxy(pg)
    return


def crawl_abstracts(keyword, outfile=None, max_iter=1000):
    """
    Crawl google scholar and retrieve author_id, year, author, title, venue, citations, pub_url, gsrank, container_type, abstract.
    The query will be sorted by relevance.
    """
    _set_new_proxy()
    search_query = S.search_pubs(keyword)
    print("Crawling Started with keyword <" + keyword + ">.\n")

    if not outfile:
        outfile = "crawler.csv"
    o_file = open(outfile, 'w')

    header = "index\tauthor_id\tyear\tauthor\ttitle\tvenue\tcitations\tpub_url\tgsrank\tcontainer_type\tabstract\n"

    o_file.write(header)

    idx = 0
    err_count = 0

    for i in range(max_iter):
        while True:
          
          if err_count > 5:
            return

          try:
            
            idx += 1

            article = next(search_query)

            citations = article["num_citations"]
            pub_url = article["pub_url"]
            gsrank = article["gsrank"]
            container_type = article["container_type"]
            author_id = ', '.join(article["author_id"])

            bibliography = article["bib"]

            year = bibliography["pub_year"]
            author = ', '.join(bibliography["author"])
            title = bibliography["title"]
            venue = bibliography["venue"]
            abstract = bibliography["abstract"]

            print(str(idx) + ' - ' + title)

            o_file.write(str(idx) + "\t")
            o_file.write(author_id + "\t")
            o_file.write(year + "\t")
            o_file.write(author + "\t")
            o_file.write(title + "\t")
            o_file.write(venue + "\t")
            o_file.write(str(citations) + "\t")
            o_file.write(pub_url + "\t")
            o_file.write(str(gsrank) + "\t")
            o_file.write(container_type + "\t")
            o_file.write(abstract + "\n")

          except Exception as e:
            err_count += 1
            print("Skipping error & refresh proxy")
            _set_new_proxy()
            continue

    o_file.close()

    print("\n\nProcess Done!")
    print("Total " + str(idx) + " articles are crawled.")
    print("Results are saved in <" + outfile + ">.")