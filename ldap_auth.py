from ldap3 import Server, Connection, ALL, NTLM

def authenticate_user(username, password):
    try:
        # This connects to your local Windows domain controller
        server = Server('localhost', get_info=ALL)

        # Use the correct domain and username
        conn = Connection(
            server,
            user=f'nour\\asus',  # ← your domain is 'nour'
            password=password,
            authentication=NTLM,
            auto_bind=True
        )

        print(f"✅ LDAP authentication successful for {username}")
        return True

    except Exception as e:
        print(f"❌ LDAP authentication failed: {e}")
        return False
