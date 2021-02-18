from zeep import Client

client = Client(wsdl='http://www.dneonline.com/calculator.asmx?wsdl')
print(client.service.Add(12, 10))

client = Client(wsdl='http://www.dneonline.com/calculator.asmx?wsdl')
print(client.service.Divide(12, 2))

client = Client(wsdl='http://www.dneonline.com/calculator.asmx?wsdl')
print(client.service.Multiply(12, 2))

client = Client(wsdl='http://www.dneonline.com/calculator.asmx?wsdl')
print(client.service.Subtract(12, 2))