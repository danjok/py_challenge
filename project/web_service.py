__author__ = 'dani'
import web
import pandas as pd

data_json = pd.read_json('../datasets/output_top_cities.json', orient='records')
print 'read', len(data_json)

urls = (
    '/top_cities', 'list_top_cities',
    '/top_cities/(.*)', 'get_top_cities'
)

class list_top_cities:
    def GET(self):
        return data_json.to_json(orient='records')

class get_top_cities:
    def GET(self, n):
        try:
            n=int(n)
        except ValueError:
            n=0
        n = 0 if (n<0) else n
        return data_json[:n].to_json(orient='records')

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()