

class WalletNotFoundException(Exception):

    """Exception raised when requested wallet is not found."""


class InsufficientFundsException(Exception):

    """Exception raised when sender has insufficient funds."""