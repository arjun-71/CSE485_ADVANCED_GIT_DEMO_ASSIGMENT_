def login(username, password):
    
    if not username or not password:
        return "Username and password are required"
    
    if username == "admin" and password == "password":
        return "Login successful"
    return "Invalid credentials"

print("adding code for selective staging")
