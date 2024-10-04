"""
Script to crawl Google Scholar for Generative AI related publications across different domains.

Built by Wisu Suntoyo.
"""

import gscrawler as g

queries = [
        # "('Generative AI' OR GenAI OR 'Gen AI') AND healthcare",
        # "('Generative AI' OR GenAI OR 'Gen AI') AND business",
        # "('Generative AI' OR GenAI OR 'Gen AI') AND education",
        # "('Generative AI' OR GenAI OR 'Gen AI') AND marketing",
        # "('Generative AI' OR GenAI OR 'Gen AI') AND personalization",
    ]

i = 0
for query in queries:
    g.crawl_abstracts(query, f"generative-ai-{i}.tsv")
    i += 1