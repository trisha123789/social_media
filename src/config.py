

import os
from supabase import create_client, Client

def get_supabase() -> Client:
    url = os.getenv("SUPABASE_URL", "https://hyfhlknzspcklfprrrqe.supabase.co")
    key = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh5Zmhsa256c3Bja2xmcHJycnFlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgxNzAwNDYsImV4cCI6MjA3Mzc0NjA0Nn0.cxStLsbvUlXsaRmJN0c8mUA5LRYStskXR5GjW5UkJ3g")
    return create_client(url, key)
