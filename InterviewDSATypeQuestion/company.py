company = {
    'employees':
        {'John': {'age': '35', 'job_title': 'Manager'},
         'Emma': {'age': '28', 'job_title': 'Software Engineer'},
         'Kelly': {'age': '41', 'job_title': 'Senior Developer'},
         'Sam': {'age': '30', 'job_title': 'Software Engineer'},
         'Mark': {'age': '37', 'job_title': 'Senior Manager'},
         'Sara': {'age': '32', 'job_title': 'Software Engineer'}
         }
}
age = 0
age += int(company['employees']['Sam']['age'])
age += int(company['employees']['Sara']['age'])
print("avg is : " , age / 2)
