# CoreHTML Codec

**An HTML codec for Core API.**

[![travis-image]][travis]
[![pypi-image]][pypi]

## Installation

Install using pip:

    $ pip install corehtml-codec

## Overview

This HTML encoding for Core API allows servers to respond in a way that allows for direct Web browser based interaction with the API.

The implementation provided only supports encoding `Document` objects into `HTML`,
and does not support decoding `HTML` output into a `Document` object.

![HTML Encoding](https://raw.githubusercontent.com/encode/corehtml-codec/master/docs/img/html-encoding.png)

## HTML encoding

Elements defined in the HTML encoding specification may include extra classes and attributes, and may be enclosed inside any parent HTML structure. This allows APIs to customize the style with which the browser based interaction is presented.

In order to to be properly supported the rendered HTML should include javascript and styling in order to allow the user to perform any available transitions included in the document.

The media type for this scheme is `text/html`.

The [python client library](https://github.com/core-api/python-client) can be taken as the canonical example for implementing an HTML rendering.

### Document

**Documents are encoded as `table` elements with a `coreapi-document` class.**

The document name and URL are represented in a single row in the `thead` element.

The  `thead` element, SHOULD enclose a single `tr` element, which SHOULD enclose a single `th` element. This element contains the document name and URL. The name and URL SHOULD be included as an `a` element, with the `href` indicating the URL, and the element text indicating the document name.

The document content is represented as the `<tbody>` element enclosing multiple `<tr>` elements.

Each data item in the document is represented as a row, which SHOULD include a single `<th>` and `<td>` element. The `<th>` element SHOULD contain the key of the item, and the `<td>` element SHOULD contain the value of the item.

Each link item in the document is represented as a row, which SHOULD include a single `<th>` element, containing the link.

### Objects

**Objects are encoded as `<table>` elements with a `coreapi-object` class.**

The object content is represented as the `<tbody>` element enclosing multiple `<tr>` elements.

Each data item in the object is represented as a row, which SHOULD include a single `<th>` and `<td>` element. The `<th>` element SHOULD contain the key of the item, and the `<td>` element SHOULD contain the value of the item.

Each link item in the object is represented as a row, which SHOULD include a single `<th>` element, containing the link.

### Arrays

**Documents are encoded as `<table>` elements with a `coreapi-array` class.**

The array content is represented as the `<tbody>` element enclosing multiple `<tr>` elements.

Each row SHOULD containing a single `<th>` element, with a textual context indicating the array index for that row.

Each row SHOULD contain a single `<td>` element, containing the item at that point in the array.

### Links

**Links are encoded as `<a>` elements, with a `coreapi-link` class.**

The key under which the Link is contained by its parent Object or Document SHOULD be contained in the text content of the element.

The URL of the Link SHOULD be contained in the `href` value of the element.

The action value of the Link SHOULD be include in a `data-action` attribute.

The transform value of the Link SHOULD be include in a `data-transform` attribute.

The fields for the Link SHOULD be included in a `data-fields` attribute, which should be a whitespace separated list of the field names.

### Data primitives

**Data primitives are encoded as `<code>` and `<span>` elements.**

The `true`, `false` and `null` primitives SHOULD be enclosed within a `<code>` element, using their textual name as the content. For example `<code>true</code>`.

Number and integer primitives SHOULD be enclosed within a `<code>` element.

String primitives SHOULD be enclosed within a `<span>` element.
The newline character, `'\n'`, MAY be replaced with a `<br/>` element.

### Errors

**Errors are encoded as `<ul>` elements, with a `coreapi-error` class.**

Each message in the error SHOULD be included as a `<li>` element, with the text of the element containing the message value.

[travis-image]: https://secure.travis-ci.org/encode/corehtml-codec.svg?branch=master
[travis]: http://travis-ci.org/encode/corehtml-codec?branch=master
[pypi-image]: https://img.shields.io/pypi/v/corehtml-codec.svg
[pypi]: https://pypi.python.org/pypi/corehtml-codec
