nose-gae-index
==============

This is a Nose plugin that updates the Google App Engine index configuration
(index.yaml) with datastore queries used in tests. It is a very useful way to
generate the index configuration if you ensure that every datastore method is
tested.

[NoseGAE](http://code.google.com/p/nose-gae/) is highly recommended for use
with this plugin.

Remember not to use queries that require indexes in the tests themselves, or
they will be added to the configuration file as well!

Installation
-----------

    python setup.py install

Usage
-----

    nosetests --with-gae --with-gae-index
