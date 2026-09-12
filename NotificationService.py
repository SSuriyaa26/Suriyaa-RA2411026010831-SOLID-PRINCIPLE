class NotificationService:

    def send_email(self, recipient, message):

        # Pretend this talks to an SMTP server
        print(
            f"[EMAIL] To: {recipient} | {message}"
        )
