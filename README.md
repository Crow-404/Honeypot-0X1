# Honeypot-0X1

# Python SSH Honeypot Script

This Python script sets up a basic SSH honeypot using `paramiko` to handle SSH connections. It listens for incoming connections on port 22 and manages multiple clients concurrently using threading.

## Key Features:
- **Handles SSH Connections**: Utilizes `paramiko.Transport` to manage SSH connections from clients.
- **Multithreading**: Each connection is handled in a separate thread, allowing for concurrent management of multiple clients.
- **Fake Authentication**: Implements both password-based and public key-based authentication, but all login attempts are set to fail (modifiable for real authentication).

## How It Works:
1. **Socket Setup**: The script opens a socket to listen for incoming connections on port 22 (default SSH port).
2. **Server Key**: A 2048-bit RSA key is generated for the server to authenticate itself to clients.
3. **Connection Handling**: When a client connects, a new thread is created to handle the connection using `paramiko.Transport`.
4. **Authentication**: The honeypot implements fake password and public key authentication, automatically failing all login attempts.

## How to Run:

### 1. Install Dependencies:

- **Windows**:  
  Open Command Prompt and run:  
  ```bash
  pip install paramiko
  ```

- **Linux**:  
  Open a terminal and run:  
  ```bash
  pip install paramiko
  ```

### 2. Run the Script:

```bash
python honeypot.py
```

---
 I make it to explan how simple honeypot works,
Feel free to give any feedback to make it better.
