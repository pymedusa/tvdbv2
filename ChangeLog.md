CHANGES
=======

Unreleased
-----

* Remove pbr
  * Clean up
  * Remove pbr
  * Update changelog
* Updates
  * Update metadata
  * Remove the need for `contextlib2` dependency
  * Update requirements
* Use response.json() instead of json.loads(...)
* Enforce unicode, handle both unicode and bytes input
  * Flake8 & Import Order
  * Enforce unicode in swagger_types
  * Update docstrings
  * Fix "301 Moved Permanently" responses
  * SearchApi.search_series_get returns SearchSeries
  * Fix to_path_value unicode/bytes mess
  * Futurise, re-add unicode_literals
  * Unify line continuation style
  * Remove useless .replace()

1.0.1
-----

* Add the api base url for lazy authentication to the auth/tvdb.py constructor, as we might want to overwrite it
* Update changelog through pbr

1.0.0
-----

* Bumping version to 1.0.0
* Set status value in ApiException if response object is available.
* Replace dict creation with dict literal
* Replace list creations with list literals.
* Add encoding declaration
* Reformat for PEP8
* Replace str case with six text_type.
* Use HTTPConnection from six.
* Add option of passing session object to tvdbv2 lib
* Changed the urllib3 exception with requests.
* added IndexerAuthFailed exception. Can be useful if we start providing the user with a helpful message that probably their tvdb api key is wrong.
* Add jwt TVDBAuth hook
* Added modules for jwt token authenticatio.
* Enabled lazy authentication.
* Replaced urllib3 with requests
* Added a session parameter, making it possible to pass a requests session object.
* Added the user_agent as a parameter
* Initial version of the tvdbv2 swagger python api client
