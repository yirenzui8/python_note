#-*-conding:utf-8-*-


import web

urls = (
    "/","index"
)

render = web.template.render('templates/')

class index:
    def GET(self):
        return render.index(name)
if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()