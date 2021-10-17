class Candidate:
    dismissal_reason_dict = {
        'FamilyReasons': 'Family reasons',
        'LowSalary': 'Low salary',
        'BadTeamMicroclimate': 'Bad team microclimate',
        'LackManagementUnderstanding': 'Lack management understanding',
        'other': 'Other',
        'NotWorked': 'Null',
        'Working': 'Working'
    }
    dismissal_reason = ''

    def dismissal_reasons(self):
        print('Choose your dismissal reason (if you are already working - input enter): ')
        for key, value in self.dismissal_reason_dict.items():
            print("{0}: {1}".format(key, value))
        Candidate.dismissal_reason = input()
        if Candidate.dismissal_reason in Candidate.dismissal_reason_dict:
            Candidate.dismissal_reason = Candidate.dismissal_reason_dict[Candidate.dismissal_reason]
            return Candidate.dismissal_reason
        else:
            print('You have no dismissal reason')
            Candidate.dismissal_reason = Candidate.dismissal_reason_dict['Working']
            return Candidate.dismissal_reason
