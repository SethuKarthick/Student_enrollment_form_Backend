from rest_framework.test import APITestCase


class TestStudentInfo(APITestCase):
    url = "http://localhost:8000/api/studentlists/"

    def test_post_studentInfo(self):
        data = {
            "first_name": "StudentTest",
            "last_name": "test1",
            "gender": "Male",
            "dob": "2021-01-01",
            "grade": "S",
            "schoollastattend": "9th",
            "address": "abc MGR Street",
            "father_name": "Student_Test_Father",
            "mother_name": "Student_Test_Mother",
            "phone": "1245368988",
            "email": "studenttset@gmail.com"
        }
        response = self.client.post(self.url, data=data)
        result = response.json
        print(response.status_code)
        self.assertEqual(response.status_code, 201)

    def test_get_studentInfo(self):
        response = self.client.get(self.url)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)


