from fetch_articles import load_articles

articles = load_articles()
for i, article in enumerate(articles[:3]):  # print first 3 articles
    print(f"\nArticle {i+1}:\nTitle: {article['title']}\nContent: {article['content'][:150]}...")
