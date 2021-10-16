class Person:

    candidate = ''
    id = 0
    first_name = ''
    last_name = ''
    job_title = ''
    job_description = ''
    job_salary = ''

    def full_name(self):
        print(f'{self.first_name} {self.last_name}')

    def dismissal_reasons(self):
        self.dismissal_reason_dict = {
            'FamilyReasons': 'Family reasons',
            'LowSalary': 'Low salary',
            'BadTeamMicroclimate': 'Bad team microclimate',
            'LackManagementUnderstanding': 'Lack management understanding',
            'other': 'Other',
            'NotWorked': 'Null',
            'Working': 'Working'
        }
        print('Choose your dismissal reason: ')
        for key, value in self.dismissal_reason_dict.items():
            print("{0}: {1}".format(key, value))
        dismissal_reason = input()
        if dismissal_reason == 'FamilyReasons':
            self.dismissal_reason = self.dismissal_reason_dict['FamilyReasons']
        elif dismissal_reason == 'LowSalary':
            self.dismissal_reason = self.dismissal_reason_dict['LowSalary']
        elif dismissal_reason == 'BadTeamMicroclimate':
            self.dismissal_reason = self.dismissal_reason_dict['BadTeamMicroclimate']
        elif dismissal_reason == 'LackManagementUnderstanding':
            self.dismissal_reason = self.dismissal_reason_dict['LackManagementUnderstanding']
        elif dismissal_reason == 'other':
            self.dismissal_reason = self.dismissal_reason_dict['other']
        elif dismissal_reason == 'NotWorked':
            self.dismissal_reason = self.dismissal_reason_dict['NotWorked']
        elif dismissal_reason == 'Working':
            self.dismissal_reason = self.dismissal_reason_dict['Working']
        return self.dismissal_reason
