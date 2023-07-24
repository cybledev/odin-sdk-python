class APIException(Exception):
    def __init__(self, status_code: int, message: str) -> None:
        """
        Custom exception class for API errors.

        Args:
            status_code (int): The status code associated with the exception.
            message (str): A descriptive error message.

        Returns:
            None
        """
        self.status_code = status_code
        self.message = message
        super().__init__('{} {}'.format(status_code, message))
