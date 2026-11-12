
class Supplier():
    def __init__(self, supplier_id: str, name: str , contact_email: str ):
        self._supplier_id = supplier_id
        self._name = name
        self._contact_email = contact_email

    #A supplier should be able to provide information about itself. Add a display_information() method.
    def display_information(self) -> None:
        print(
            f"Supplier ID: {self._supplier_id} | "
            f"Name: {self._name} | "
            f"Contact Email: {self._contact_email} | "
            )