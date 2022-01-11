# HINT: you'll probably want to import
# more from here over the course of the
# implementation
from flask import (
    Flask,
    Response,
    request
)

from store import Store


Store = Store.initialize()


app = Flask(__name__)


class ValidationError(Exception):
    pass


class ShortenerValidationForm:

    def __init__(self, params):
        self.url = params.get('url')

    def validate(self):
        # TODO: create these methods. they are purposefully
        # not present on this class.
        # HINT: they should raise ValidationError if validation
        # fails.

        # HINT: validate that the URL is present
        self.validate_presence()
        # HINT: validate link is a URL with some off-the-shelf regex
        self.validate_url()


# TODO: shorten a long URL with whatever
# algo your heart desires.
def shorten(url):
    raise NotImplementedError


@app.route("/shorten", methods=['POST'])
def shorten_route():
    '''Shortens a link, persists it to the DB, and returns the shortened link.

    To e.g. call with curl:

        curl --data "url=https://google.com" <<your flask server>>/shorten
    '''

    validation_form = ShortenerValidationForm(request.form)

    # TODO: fill out the validate() method above.
    try:
        validation_form.validate()
    except ValidationError:
        return Response(
            status=422,
            mimetype='application/json'
        )

    # TODO: implement some algorithm in the
    # `shorten` function above
    shortened = shorten(validation_form.url)

    # TODO: fill this method in in `Store`.
    # it will crash for now.
    Store.create(
        long_link=validation_form.url,
        short_link=shortened
    )

    response = { 'shortened_link': shortened }

    return response


@app.route("/<short_link>")
def redirect_route(short_link):
    '''Redirects the user from short_link to long_link.

    To e.g. call with curl:

        curl <<your flask server>>/<<the short link ID>>
    '''

    # TODO: implement `find` method in Store.
    # HINT: think about what should happen if no link is
    # found.
    long_link = Store.find(short_link)

    # TODO: redirect to the long link
    raise NotImplementedError
