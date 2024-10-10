def upload_to(instance, filename):

    return f"uploads/{instance.__class__.__name__.lower()}/{filename}"
