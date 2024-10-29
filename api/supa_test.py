import hashlib
from supabase import create_client, Client

# Supabes data connection: URL, Key

SUPABASE_URl = "https://csolefhztjtngelrjwqu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNzb2xlZmh6dGp0bmdlbHJqd3F1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzAxNjY2MDQsImV4cCI6MjA0NTc0MjYwNH0.6pzdE3adf19gzR2e9h9UzG-qpunbTr_g0HCfDWDsIyc"

# Connect to SupaBase Client

supabase: Client = create_client(SUPABASE_URl, SUPABASE_KEY)

# GET and Save Data Fuction

def save_data(e,p):
    #Encripto Password
    enc_pass = hashlib.sha256(p.encode()).hexdigest()
    
    # Insert into users model
    response = supabase.table('users').insert({"email": e, "password": enc_pass }).execute()
    
    if response.data:
        print(f"User has been save successfuly: {response.data}")
    elif response.error:
        print(f"Error saving user: {response.error}" )
  

# Main

email = input("User E-mail: ")
passwd = input("User Password:")
save_data(email,passwd)
