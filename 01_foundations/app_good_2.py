print("GOOD-2: Import + explicit execution")

from refactored_service import UserService

service = UserService('{"name": "Rahul", "age": 24}')
result = service.process()

print(result)