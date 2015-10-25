from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from sphinx.util.compat import make_admonition
from sphinx.locale import _


def setup(app):
    app.add_node(exercise,
                 html=(visit_exercise, depart_exercise))
    app.add_node(exercisehint,
                 html=(visit_hint, depart_hint))

    app.add_directive('exercise', ExerciseDirective)
    app.add_directive('exercisehint', ExerciseHintDirective)

    return {'version': '0.1'}   # identifies the version of our extension


## exercise directive

class exercise(nodes.Admonition, nodes.Element):
    pass

def visit_exercise(self, node):
    self.body.append(self.starttag(
        node, 'div', CLASS=('admonition exercise')))
    node.insert(0, nodes.title('exercise', 'Exercise'))
    self.set_first_last(node)

def depart_exercise(self, node):
    self.depart_admonition(node)

class ExerciseDirective(BaseAdmonition):
    node_class = exercise


## exercisehint directive

class exercisehint(nodes.Part, nodes.TextElement):
    pass

def visit_hint(self, node):
    self.body.append(self.starttag(node, 'p', CLASS="exercise-hint") + \
        '<button>Hint</button><span class="hidden">')

def depart_hint(self, node):
    self.body.append('</span></p>')

class ExerciseHintDirective(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}

    def run(self):
        if not self.arguments:
            return []
        subnode = exercisehint()
        inodes, messages = self.state.inline_text(self.arguments[0],
                                                  self.lineno)
        subnode.extend(inodes)
        return [subnode] + messages
