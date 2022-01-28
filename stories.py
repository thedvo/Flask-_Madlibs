"""Madlibs Stories."""

from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

stories = Flask(__name__)
stories.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(stories)


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


# @stories.route('/')
# def show_form():
#     return render_template('base.html')


# @stories.route('/story')
# def get_story():
#     place = request.args.get('place')
#     noun = request.args.get('noun')
#     verb = request.args.get('verb')
#     adjective = request.args.get('adjective')
#     plural_noun = request.args.get('plural_noun')

#     return render_template('story.html', place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)


@stories.route('/')
def show_form():
    prompts = story.prompts

    return render_template('form.html', prompts=prompts)


@stories.route('/story')
def get_story():

    text = story.generate(request.args)

    return render_template('story.html', text=text)
