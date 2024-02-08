from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Literal, \
    Number, Operator, Other, Punctuation, Text, Generic, Whitespace

__all__ = ['PearlStyle']
class PearlStyle(Style):
    name = 'pearl'
    plain = '#F2F2F2'
    styles = {
        Whitespace: plain,
        Generic: plain,
        Literal: plain,
        Other: plain,
        Punctuation: plain,
        Text: plain,

        Comment: '#FFFFB3',
        Number: '#FFFFB3',
        String: '#79D338',
        Operator: '#6BC4CF',  # math operators, "is", ==, etc.
        Operator.Word: '#6BC4CF',

        Keyword: '#DBC0E0',  # key words
        Keyword.Constant: '#EC93C5',
        Keyword.Type: '#8BE9FD',
        
        Name: '#FFFFFF',  # general naming
        Name.Attribute: '#FFFFFF',  # class variable names
        Name.Builtin: '#FFFFFF',  # built in types
        Name.Builtin.Pseudo: '#DBC0E0',  # self
        Name.Function: '#8BE9FD',  # function names
        Name.Function.Magic: '#8BE9FD',  # special py methods
        Name.Class: '#00E0E0',  # class name
        Name.Label: '#FFFFFF',  # none, true, false
        Name.Tag: '#FF79C6',  # types
        Name.Exception: '#DBC0E0', # exceptions
        Name.Variable: '#00E0E0'  # variable names
    }