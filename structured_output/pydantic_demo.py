 from pydantic  import BaseModel
  class Student (BaseModel):
    name : : str
  new_student = Student(name="John Doe")

  student  = Student(**new_student.dict())
  print(student)