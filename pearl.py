from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Literal, \
    Number, Operator, Other, Punctuation, Text, Generic, Whitespace

__all__ = ['PearlStyle']
class PearlStyle(Style):
    name = 'pearl'
    plain = '#F2F2F2'
    styles = {
        Whitespace: plain,
        Generic: plain,
        Error: plain,
        Literal: plain,
        Other: plain,
        Punctuation: plain,
        Text: plain,

        Comment: '#FFFFB3',
        Number: '#FFFFB3',
        String: '#79D338',
        Operator: '#56B6C2',

        Keyword: '#DCC6E0',
        Keyword.Constant: '#EC93C5',
        Keyword.Type: '#8BE9FD',
        
        Name: plain,
        Name.Attribute: '#50FA7B',
        Name.Builtin: '#8BE9FD',
        Name.Builtin.Pseudo: plain,
        Name.Class: '#00E0E0',
        Name.Label: '#8BE9FD',
        Name.Tag: '#FF79C6',
        Name.Variable: '#00E0E0'
    }
