from abc import ABC, abstractmethod
class Package:
    def __init__(self, weight: int|float, price: int|float) :
        self.weight = weight
        self.price = price
class LogisticsStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, package):
        pass
class USALogistics(LogisticsStrategy):
    def calculate_fee(self, package: Package):
        return 10 + package.weight * 5
class UKLogistics(LogisticsStrategy):
    def calculate_fee(self, package: Package):
        if  package.price > 100:
            return package.price * 0
        else:
            return package.weight * 8
class MLSLogistics(LogisticsStrategy):
    def calculate_fee(self,package: Package):
        return 15
class LogisticsFactory:
    @staticmethod
    def get_strategy(strategy: str) -> LogisticsStrategy:
        strategy = strategy
        if strategy == "UK":
            return UKLogistics()
        elif strategy == "USA":
            return USALogistics()
        elif strategy == "MLS":
            return MLSLogistics()
if __name__ == "__main__":
    package_a = Package(weight=2.5, price=50)  
    package_b = Package(weight=3.0, price=120) 
    package_c = Package(weight=1.5, price=20)
    strategy_usa = LogisticsFactory.get_strategy("USA")
    strategy_uk = LogisticsFactory.get_strategy("UK")
    strategy_my = LogisticsFactory.get_strategy("MLS")
    print(f"USA Shipping Fee: ${strategy_usa.calculate_fee(package_a)}")        # 22.5
    print(f"UK Shipping Fee: ${strategy_uk.calculate_fee(package_b)}")          # 0
    print(f"Malaysia Shipping Fee: ${strategy_my.calculate_fee(package_c)}")    # 15
