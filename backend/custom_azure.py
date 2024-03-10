from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'danikawebsite' # Must be replaced by your <storage_account_name>
    account_key = 'RjWCcS0vuitQtdBic/csCaccOjE4KBpje2Tx7/YcUBhtRvKOOcerU8hactZwmOS/bXU15AD7leAl+AStneuw3Q==' 
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'danikawebsite' # Must be replaced by your storage_account_name
    account_key = 'RjWCcS0vuitQtdBic/csCaccOjE4KBpje2Tx7/YcUBhtRvKOOcerU8hactZwmOS/bXU15AD7leAl+AStneuw3Q==' 
    azure_container = 'static'
    expiration_secs = None
