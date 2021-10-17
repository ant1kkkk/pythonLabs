class Candidate:
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
        print('Choose your dismissal reason (if you are already working - input enter): ')
        for key, value in self.dismissal_reason_dict.items():
            print("{0}: {1}".format(key, value))
        self.dismissal_reason = input()
        if self.dismissal_reason in self.dismissal_reason_dict:
            self.dismissal_reason = self.dismissal_reason_dict[self.dismissal_reason]
            return self.dismissal_reason
        elif self.dismissal_reason not in self.dismissal_reason_dict:
            print('You have no dismissal reason')
            self.dismissal_reason = self.dismissal_reason_dict['Working']
            return self.dismissal_reason
