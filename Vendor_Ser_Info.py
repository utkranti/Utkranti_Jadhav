from abc import ABC,abstractmethod

class Vendor_Service(ABC):

    @abstractmethod
    def add_product(self,prod):
        pass

    @abstractmethod
    def get_product(self,pid):
        pass

    @abstractmethod
    def update_product(self,prod):
        pass

    @abstractmethod
    def remove_product(self,pid):
        pass

    @abstractmethod
    def get_all_products(self):
        pass
