# coding: utf-8
from coreapi import Document, Link, Error
from html_codec import HTMLCodec


# Tests for HTML rendering

def test_html_document_rendering():
    doc = Document(content={'string': 'abc', 'int': 123, 'bool': True})
    content = HTMLCodec().dump(doc)
    assert 'coreapi-document' in content
    assert '<span>abc</span>' in content
    assert '<code>123</code>' in content
    assert '<code>true</code>' in content


def test_html_object_rendering():
    doc = Document(content={'object': {'a': 1, 'b': 2}})
    content = HTMLCodec().dump(doc)
    assert 'coreapi-object' in content
    assert '<th>a</th>' in content
    assert '<th>b</th>' in content


def test_html_array_rendering():
    doc = Document(content={'array': [1, 2]})
    content = HTMLCodec().dump(doc)
    assert 'coreapi-array' in content
    assert '<th>0</th>' in content
    assert '<th>1</th>' in content


def test_html_link_rendering():
    doc = Document(content={'link': Link(url='/test/')})
    content = HTMLCodec().dump(doc)
    assert 'coreapi-link' in content
    assert 'href="/test/"' in content


def test_html_error_rendering():
    doc = Error(content={'message': ['something failed']})
    content = HTMLCodec().dump(doc)
    assert 'coreapi-error' in content
    assert 'something failed' in content
