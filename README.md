# SSA (Secure Store Application)

SSA (Secure Store Application) is a Python class designed to provide secure storage and management of sensitive data using RSA encryption and JWT tokens.

## Features

- **Encryption**: Encrypts data using RSA encryption to ensure secure transmission and storage.
- **Decryption**: Decrypts encrypted data using the RSA private key.
- **Data Integrity**: Uses JWT tokens to ensure data integrity during transmission and storage.
- **File Management**: Manages encrypted data storage in files.

## Requirements

- Python 3.x
- PyJWT
- rsa

## Usage

1. Import the necessary modules:

  ```python
  import pickle
  import rsa
  import os
  import jwt
  ```
2. Instantiate the StoreManager class by providing a JWT token:

   store_manager = StoreManager(TOKEN)

3. Use the broadcast method to manage data:

  # To store data in a file:
  store_manager.broadcast(path, data)

  # To retrieve data from a file:
  store_manager.broadcast(path)


## Methods
  - broadcast(path, data): Manages data storage and retrieval.
  - __loadKeys(pub_Key=False, priv_key=False): Loads RSA public and private keys.
  - __encript(data): Encrypts data using RSA public key.
  - __decrypt(data): Decrypts encrypted data using RSA private key.
  - __jwEncode(data): Encodes data using JWT token.
  - __jwDecode(data): Decodes JWT token to retrieve data.
  - __dataManager(path, data): Manages data encryption and storage in files.

## Example

  # Instantiate SSA (Secure Store Application)
  ssa_app = StoreManager("my_jwt_token")

  # Store data
  ssa_app.broadcast("data.txt", {"key": "value"})

  # Retrieve data
  retrieved_data = ssa_app.broadcast("data.txt")
  print(retrieved_data)  # Output: {'key': 'value'}


## Note
  Ensure that PyJWT and rsa libraries are installed.
  SSA creates a .env file to store RSA keys. Ensure proper access permissions for security.
  


   
