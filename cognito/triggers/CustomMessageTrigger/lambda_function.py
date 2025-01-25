def lambda_handler(event, context):
    trigger_source = event['triggerSource']
    user_attributes = event['request']['userAttributes']
    code_parameter = event['request']['codeParameter']
    link_parameter = event['request']['linkParameter']
    username_parameter = event['request']['usernameParameter']

    if trigger_source == "CustomMessage_SignUp":
        event['response']['emailSubject'] = "Welcome to Aurrica!"
        event['response']['emailMessage'] = f"Hello {user_attributes['given_name']}, thank you for signing up. Verify your account by clicking on the link: {link_parameter}."
    elif trigger_source == "CustomMessage_AdminCreateUser":
        event['response']['emailSubject'] = "Welcome to Aurrica!"
        event['response']['emailMessage'] = f"Hello {user_attributes['given_name']}, your account has been created. Your temporary password is {link_parameter}."
    elif trigger_source == "CustomMessage_ResendCode":
        event['response']['emailSubject'] = "Resend Verification Code"
        event['response']['emailMessage'] = f"Hello {user_attributes['given_name']}, here is your verification link: {link_parameter}."
    elif trigger_source == "CustomMessage_ForgotPassword":
        event['response']['emailSubject'] = "Password Reset Request"
        event['response']['emailMessage'] = f"Hello {user_attributes['given_name']}, you requested a password reset. Your verification link is {link_parameter}."

    return event