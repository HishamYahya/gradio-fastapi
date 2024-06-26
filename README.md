# Gradio-FastAPI: Publicly Share and Demo Your FastAPI Apps Through Gradio Tunneling

This repository provides a simple and efficient way to tunnel any FastAPI application through a public Gradio URL. By leveraging this tool, developers can quickly demo and share their FastAPI applications with others without the need for complex server configurations or deployment processes. Ideal for quick prototyping, testing, and collaborative development, this solution ensures your FastAPI app is accessible from anywhere with minimal setup.

## Features
- **Seamless Integration**: Easily connect your FastAPI app to a public Gradio URL.
- **Quick Setup**: Get your FastAPI app running publicly in just a few steps.
- **Convenient Sharing**: Share your app with collaborators via a simple URL.
- **Efficient Prototyping**: Perfect for quick demos, testing, and feedback collection.

## Installation
```bash
pip install gradio-fastapi
```

## Usage
1. Import the tunnel lifespan function initializer in your FastAPI app:
    ```python
    from gradio_fastapi import gradio_lifespan_init
    ```

2. Set the lifespan of the App:
   1. If you do not already have a lifespan function defined: 
      ```python  
      app = FastAPI(lifespan=gradio_lifespan_init())
      ```
   2. If you do
      ```python
      app = FastAPI(lifespan=gradio_lifespan_init(my_lifespan))
      ```

3. Run your app and get the public Gradio URL for sharing logged using uvicorn:
    ```bash
    fastapi dev main.py
    ```

## Example
Check out example.py for a sample FastAPI application using this tunnel.

## Contributions
Feel free to open issues or submit pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License.
