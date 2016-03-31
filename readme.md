![medusa-name-logo-green-snakes](https://cloud.githubusercontent.com/assets/1867464/13375559/ede197ae-dd70-11e5-8cd0-b0eb239c977e.png)

A tvdb version2 API client, generated using swagger's codegen

#### Usage
 - For ease of demonstration i've configured the following variables before going into the API's methods.
  base_url = 'https://api-beta.thetvdb.com'
  client_id = 'username' (optional! Only required for the /user routes)
  client_secret = 'pass' (optional! Only required for the /user routes)
  apikey = "0629B785CE550C8D"
 
 - Setup the authentication string thats needed later: 
```python
authentication_string = {"apikey":apikey, "username":"", "userpass":""}
```

 - Create a unauthenticated client instance:
```python
unauthenticated_client = ApiClient(base_url)
```
 
 - Create an AuthenticationApi object instance
```python
auth_api = AuthenticationApi(unauthenticated_client)
```

 - Get the Bearer token using the authentication_string
```python
access_token = auth_api.login_post(authentication_string)
```

 - Setup the authenticated client instance:
```python
auth_client = ApiClient(base_url, 'Authorization', 'Bearer ' + access_token.token)
```

 - Now your able to use the API's query endpoints like:
```python
SearchApi(auth_client).search_series_get(name='Breaking Bad')
SeriesApi(auth_client).series_id_get(80379)
```