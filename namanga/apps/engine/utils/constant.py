from enum import Enum


class AppStatus(Enum):
    REGISTER_USER_SUCCESS = 'REGISTER_USER_SUCCESS', 200, "Register user successful."
    SEND_MAIL_SUCCESS = 'SEND_MAIL_SUCCESS', 200, "Email sent successfully, please check your email."

    ID_INVALID = 'ID_INVALID', 400, "ID model invalid."
    NAME_MANGA_INVALID = "NAME_MANGA_INVALID", 400, "Name manga invalid."
    REGISTER_USER_FAIL = "REGISTER_USER_FAIL", 400, "Register user failed."
    EMAIL_ALREADY_EXIST = "EMAIL_ALREADY_EXIST", 400, "Email already exist."
    EXPIRED_VERIFY_CODE = 'EXPIRED_VERIFY_CODE', 400, 'Your code is expired.'
    INVALID_VERIFY_CODE = "INVALID_VERIFY_CODE", 400, "Your code is invalid."
    USERNAME_ALREADY_EXIST = "USERNAME_ALREADY_EXIST", 400, "Username already exist."
    USER_NOT_HAVE_ENOUGH_PERMISSION = "USER_NOT_HAVE_ENOUGH_PERMISSION", 400, "User does not have enough permission."

    EMAIL_NOT_EXIST = "EMAIL_NOT_EXIST", 404, "Email does not exist."


    # TIMEOUT_CHANGE_PASSWORD = "TIMEOUT_CHANGE_PASSWORD", 400, "Timeout to change password."
    # PASSWORDS_ARE_NOT_THE_SAME = "PASSWORDS_ARE_NOT_THE_SAME", 400, "Password and password confirm are not the same."
    # PASSWORD_RESET_SUCCESS = "PASSWORD_RESET_SUCCESS", 200, "Password reset successfully."
    # CURRENT_PASSWORD_INCORRECT = "CURRENT_PASSWORD_INCORRECT", 400, "Current password is incorrect."
    # VERIFY_CODE_SUCCESS = "VERIFY_CODE_SUCCESS", 200, "Verify code successfully."
    # PASSWORD_2FA_ALREADY_EXISTS = "PASSWORD_2FA_ALREADY_EXISTS", 404, "Password 2FA already exists."
    # CREATE_PASSWORD_2FA = "CREATE_PASSWORD_2FA", 200, "Create 2FA successfully."
    # NO_PASSWORD_2FA_EXIST = "NO_PASSWORD_2FA_EXIST", 404, "No password 2FA exist."
    # INCORRECT_CURRENT_PASSWORD_2FA = "INCORRECT_CURRENT_PASSWORD_2FA", 400, "Current password is incorrect."
    # NEW_PASSWORDS_ARE_NOT_THE_SAME = "NEW_PASSWORDS_ARE_NOT_THE_SAME", 400, "New password are not the same."
    # UPDATE_PASSWORD_2FA_SUCCESS = "UPDATE_PASSWORD_2FA_SUCCESS", 200, "Update password 2FA success."
    # PASSWORD_2FA_MUST_BE_4_CHARACTERS = ("PASSWORD_2FA_MUST_BE_4_CHARACTERS", 400,
    #                                      "Password 2FA must be 4 characters long.")
    # DELETE_ACCOUNT_SUCCESS = "DELETE_ACCOUNT_SUCCESS", 200, "Delete account successfully."
    # ACCOUNT_HAS_BEEN_DELETED_BEFORE = "ACCOUNT_HAS_BEEN_DELETED_BEFORE", 400, "The account has been deleted before."
    # YOU_HAVE_UPDATED_KYC = "YOU_HAVE_UPDATED_KYC", 200, "You have updated kyc."
    # UPDATE_STATUS_KYC_SUCCESS = "UPDATE_STATUS_KYC_SUCCESS", 200, "Update status successfully."
    # INVALID_VALUE_FOR_STATUS_KYC = ("INVALID_VALUE_FOR_STATUS_KYC", 400,
    #                                 "Invalid value for status_kyc. Must be 'true' or 'false'.")
    # USER_IS_ACTIVE = "USER_IS_ACTIVE", 200, "User is active."
    # USER_NOT_HAVE_ENOUGH_PERMISSION = "USER_NOT_HAVE_ENOUGH_PERMISSION", 400, "User does not have enough permission."
    # EMAIL_INVALID = "EMAIL_INVALID", 400, "Email is invalid"
    # ROLE_SYSTEM_INVALID = "ROLE_SYSTEM_INVALID", 400, "Role system invalid"
    # USER_ID_INVALID = "USER_ID_INVALID", 400, "User id invalid"
    # USER_ALREADY_HAS_THAT_ROLE = "USER_ALREADY_HAS_THAT_ROLE", 400, "User already has that role."
    # UPDATE_ROLE_USER_SUCCESS = "UPDATE_ROLE_USER_SUCCESS", 200, "Update role successfully."
    # SET_WALLET_PASSWORD_SUCCESS = "SET_WALLET_PASSWORD_SUCCESS", 200, "Set wallet password successfully."
    # PAYMENT_ALREADY_EXISTS = "PAYMENT_ALREADY_EXISTS", 400, "Payment already exists in the system."
    # PAYMENT_NOT_EXISTS = "PAYMENT_NOT_EXISTS", 404, "Payment not exists."
    # PAYMENT_DELETE_SUCCESS = "PAYMENT_DELETE_SUCCESS", 200, "Payment delete successfully."
    # PAYMENT_ID_INVALID = "PAYMENT_ID_INVALID", 400, "Payment ID invalid."
    # REFERRAL_CODE_NOT_EXISTS = "REFERRAL_CODE_NOT_EXISTS", 404, "Referral code does not exist."

    # ACCOUNT_IS_LOCKED = "ACCOUNT_IS_LOCKED", 400, "Your account is locked."
    # SYSTEM_INFORMATION_ONLY_CREATED_ONCE = "SYSTEM_INFORMATION_ONLY_CREATED_ONCE", 400, "Can only be created once."
    # NO_USERS_PROVIDED = "NO_USERS_PROVIDED", 400, "No users provided."
    # INVALID_USER_IDS = "INVALID_USER_IDS", 400, "Invalid user ids."
    #
    # READ_ALL_NOTIFICATION = 'READ_ALL_NOTIFICATION', 200, "All notifications marked as read."
    # DELETE_NOTIFICATION = 'DELETE_NOTIFICATION', 200, "Notifications marked as deleted."
    # SEND_NOTIFICATION = 'SEND_NOTIFICATION', 200, "Notifications marked as send."
    # DELETE_HISTORY_BALANCE = 'DELETE_HISTORY_BALANCE', 200, "Delete history balance successfully."
    # HISTORY_BALANCE_NOT_EXISTS = 'HISTORY_BALANCE_NOT_EXISTS', 404, "history balance not exists."

    @property
    def message(self):
        return {
            'message': str(self.value[2]),
            'code': str(self.value[1]),
            'data': 'success' if self.value[1] in [200, 201] else 'failed'
        }
