"""Test file for SMTP mail functionality with Zeptomail."""

from utkit.communication.mail.smtp import SMTPConfig, MailMessage, send_mail


def test_plain_text_email():
    """Test sending plain text email."""
    
    config = SMTPConfig(
        host="smtp.zeptomail.in",
        port=587,
        username="emailapikey",
        password="PHtE6r0NQent2jZ68RkIs6frRJKkMo59r+1hfQJPtNpBXqIGHk1R/o0pxjbkrRx4UaZKRf+TyI5gub/IsLjXIG2/NzxMXmqyqK3sx/VYSPOZsbq6x00btV4TdEbbVI7scdBv1iDSv9zcNA==",
    )
    
    message = MailMessage(
        subject="Test Plain Text Email",
        from_address="noreply@openworksuite.com",
        to=["tinspj1997@gmail.com"],
        text="This is a plain text email.\nIt supports multiple lines.",
    )
    
    try:
        send_mail(config, message)
        print("✓ Plain text email sent successfully!")
    except Exception as e:
        print(f"✗ Error sending email: {e}")


def test_html_email():
    """Test sending HTML email."""
    
    config = SMTPConfig(
        host="smtp.zeptomail.in",
        port=587,
        username="emailapikey",
        password="PHtE6r0NQent2jZ68RkIs6frRJKkMo59r+1hfQJPtNpBXqIGHk1R/o0pxjbkrRx4UaZKRf+TyI5gub/IsLjXIG2/NzxMXmqyqK3sx/VYSPOZsbq6x00btV4TdEbbVI7scdBv1iDSv9zcNA==",
    )
    
    message = MailMessage(
        subject="Test Email",
        from_address="noreply@openworksuite.com",
        to=["tinspj1997@gmail.com"],
        html="<p>Test email sent successfully.</p>",
    )
    
    try:
        send_mail(config, message)
        print("✓ HTML email sent successfully!")
    except Exception as e:
        print(f"✗ Error sending email: {e}")


def test_html_email_with_cc_and_reply_to():
    """Test HTML email with CC and Reply-To headers."""
    
    config = SMTPConfig(
        host="smtp.zeptomail.in",
        port=587,
        username="emailapikey",
        password="PHtE6r0NQent2jZ68RkIs6frRJKkMo59r+1hfQJPtNpBXqIGHk1R/o0pxjbkrRx4UaZKRf+TyI5gub/IsLjXIG2/NzxMXmqyqK3sx/VYSPOZsbq6x00btV4TdEbbVI7scdBv1iDSv9zcNA==",
    )
    
    message = MailMessage(
        subject="Test Email with CC",
        from_address="noreply@openworksuite.com",
        to=["tinspj1997@gmail.com"],
        cc=["cc@example.com"],
        html="<h1>Hello</h1><p>This is a test email with CC.</p>",
        reply_to="support@openworksuite.com",
    )
    
    try:
        send_mail(config, message)
        print("✓ Email with CC and Reply-To sent successfully!")
    except Exception as e:
        print(f"✗ Error sending email: {e}")


def test_multipart_email():
    """Test email with both plain text and HTML fallback."""
    
    config = SMTPConfig(
        host="smtp.zeptomail.in",
        port=587,
        username="emailapikey",
        password="PHtE6r0NQent2jZ68RkIs6frRJKkMo59r+1hfQJPtNpBXqIGHk1R/o0pxjbkrRx4UaZKRf+TyI5gub/IsLjXIG2/NzxMXmqyqK3sx/VYSPOZsbq6x00btV4TdEbbVI7scdBv1iDSv9zcNA==",
    )
    
    message = MailMessage(
        subject="Multipart Email",
        from_address="noreply@openworksuite.com",
        to=["tinspj1997@gmail.com"],
        text="This is a plain text version for clients that don't support HTML.",
        html="<p>This is the <strong>HTML</strong> version of the email.</p>",
    )
    
    try:
        send_mail(config, message)
        print("✓ Multipart email (text + HTML) sent successfully!")
    except Exception as e:
        print(f"✗ Error sending email: {e}")


def test_otp_email_example():
    """Test OTP email similar to your implementation."""
    
    config = SMTPConfig(
        host="smtp.zeptomail.in",
        port=587,
        username="emailapikey",
        password="PHtE6r0NQent2jZ68RkIs6frRJKkMo59r+1hfQJPtNpBXqIGHk1R/o0pxjbkrRx4UaZKRf+TyI5gub/IsLjXIG2/NzxMXmqyqK3sx/VYSPOZsbq6x00btV4TdEbbVI7scdBv1iDSv9zcNA==",
    )
    
    otp = "123456"
    html = (
        "<div style='font-family:sans-serif;'>"
        "<p>Use the OTP below to complete your signup:</p>"
        f"<h2 style='letter-spacing:4px'>{otp}</h2>"
        "<p>This OTP expires in <strong>10 minutes</strong>.</p>"
        "<p>If you did not request this, please ignore this email.</p>"
        "</div>"
    )
    
    message = MailMessage(
        subject="Your OTP for signup",
        from_address="noreply@openworksuite.com",
        to=["tinspj1997@gmail.com"],
        html=html,
    )
    
    try:
        send_mail(config, message)
        print("✓ OTP email sent successfully!")
    except Exception as e:
        print(f"✗ Error sending email: {e}")


if __name__ == "__main__":
    print("Testing Zeptomail SMTP integration...\n")
    
    print("Test 1: Plain text email")
    test_plain_text_email()
    
    print("\nTest 2: HTML email")
    test_html_email()
    
    print("\nTest 3: HTML email with CC and Reply-To")
    test_html_email_with_cc_and_reply_to()
    
    print("\nTest 4: Multipart email (text + HTML)")
    test_multipart_email()
    
    print("\nTest 5: OTP email example")
    test_otp_email_example()
