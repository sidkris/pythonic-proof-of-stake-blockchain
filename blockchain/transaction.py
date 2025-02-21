import uuid
import time 
from typing import Final 

class Transaction:

    def __init__(self, sender_public_key : str, receiver_public_key : str, transaction_amount : int, transaction_type : str) -> None:

        """
        
        Initialize a new transaction.
        
        sender_public_key: Public key of the transaction sender
        receiver_public_key: Public key of the transaction receiver
        transaction_amount: Amount to be transferred
        transaction_type: Type of transaction being performed
        
        """

        self.sender_public_key : str = sender_public_key
        self.receiver_public_key : str = receiver_public_key
        self.transaction_amount : int = transaction_amount
        self.transaction_type : str = transaction_type
        self.id : Final[str] = uuid.uuid1().hex
        self.time_stamp : Final[float] = time.time()
        self.signature : str = ""


    def to_json(self):
        return self.__dict__
