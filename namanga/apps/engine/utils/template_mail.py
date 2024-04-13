class TemplateMail(object):
    SUBJECT_MAIL_VERIFICATION = 'Verify Your Account Registration with OTP Code'

    CONTENT_MAIL_VERIFICATION = lambda full_name, otp_code: F"""<div>
    <p>Hello {full_name}</p>
    <p> We have received a request to reset the password for your NAMANGA account. To proceed with the password reset
      process, please use the following OTP (One-Time Password) code: {otp_code}.</p>
    <p> Thank you for choosing Velociti.</p>
    <p>Best regards,</p>
    <p> NAMANGA Team</p>
  </div>"""
