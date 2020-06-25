import os
import tornado.ioloop
import tornado.web
import newspaper
import nltk
import json

nltk.download('punkt')


class LinkHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))
        paper = data.get("link")
        article = newspaper.Article(paper)

        article.download()
        article.parse()

        article.nlp()

        self.write(article.summary)


application = tornado.web.Application([
    (r"/link", LinkHandler),
])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
