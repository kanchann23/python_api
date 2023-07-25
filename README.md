# Python HTTP Server with Random Password Generator

This is a simple Python HTTP server that provides two endpoints: `/ping` and `/password`. The `/ping` endpoint responds with "ping-pong", and the `/password` endpoint generates a random password using the `gen_pass()` function from the `passw` package.

## Requirements

- Python 3.x

## How to Use

1. Clone the repository to your local machine:

   git clone https://github.com/kanchann23/python_api


2. Install required dependencies. (Make sure the `passw` package is installed):

   ```
   pip install passw
   
   ```
 
4. Run the server:


 ```

     python server.py

```

   
4. Access the server endpoints:

- Ping endpoint: `http://localhost:8080/ping`
- Password endpoint: `http://localhost:8080/password`

## Customization

- The password length can be customized in the `gen_pass()` function inside the `password` endpoint handler.
- The server address and port can be modified in the `server_address` variable in the `run_server()` function.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.







