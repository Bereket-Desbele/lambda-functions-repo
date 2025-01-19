def lambda_handler(event, context):
    """
    Post Authentication trigger handler
    """
    print("Post Authentication triggered for user:", event['userName'])
    
    # Add your post-authentication logic here
    # e.g., update last login time, track login statistics, etc.
    
    return event