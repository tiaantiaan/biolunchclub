import webapp2
import LunchClub


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        instance = LunchClub.NextLunch()		
        self.response.write(instance.printlist())




application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
