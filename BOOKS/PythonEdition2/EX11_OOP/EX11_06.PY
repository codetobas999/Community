class PublicEmp:
        def __init__(self, salary):
            self.salary = salary

class ProtectedEmp:
        def __init__(self, salary):
            self._salary = salary

class Emp(ProtectedEmp):
    def getsalary(self):
        return self._salary

class PrivateEmp:
    def __init__(self, salary):
            self.__salary = salary

    def getsalary(self):
        return self.__salary

myemp1 = PublicEmp(10000)
print("เงินเดือนของ PublicEmp เท่ากับ {0:,.2f} บาท".format(myemp1.salary))

myemp2 = Emp(20000)
print("เงินเดือนของ ProtectedEmp เท่ากับ {0:,.2f} บาท".format(myemp2.getsalary()))

myemp3 = PrivateEmp(30000)
print("เงินเดือนของ PrivateEmp เท่ากับ {0:,.2f} บาท".format(myemp3.getsalary()))

