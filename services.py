
from configure import supabase

def upload_file(file, folder="images"):
    """
    Uploads an image or video to Supabase storage and returns the public URL.
    """
    if not file:
        return None

    file_bytes = file.read()
    file_name = file.name
    bucket_name = "media"

    # Delete existing file if exists
    try:
        supabase.storage.from_(bucket_name).remove([f"{folder}/{file_name}"])
    except:
        pass  # Ignore if file doesn't exist

    # Upload to Supabase
    supabase.storage.from_(bucket_name).upload(f"{folder}/{file_name}", file_bytes)

    # Get public URL (returns string)
    public_url = supabase.storage.from_(bucket_name).get_public_url(f"{folder}/{file_name}")
    return public_url
