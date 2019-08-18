class Article:

    artcl_count = 0

    def __init__(self, HTML):
        self.title = HTML.h2.get_text().replace('\n', ' ')
        self.link = "https://www.reuters.com" + str(HTML.a['href'])
        self.descrp = HTML.p.get_text().replace('\n', ' ')

        Article.artcl_count += 1