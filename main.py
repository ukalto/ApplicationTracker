import time
import pandas as pd
from datetime import date
import os.path


class JobApplication:
    def __init__(self, company, job_position, application_sent, job_source, answer, interview, interview_datetime, reason_for_no):
        self.company = company
        self.job_position = job_position
        self.application_sent = application_sent
        self.job_source = job_source
        self.answer = answer
        self.interview = interview
        self.interview_datetime = interview_datetime
        self.reason_for_no = reason_for_no

    def to_dict(self):
        return {
            'company': self.company,
            'job_position': self.job_position,
            'application_sent': self.application_sent,
            'job_source': self.job_source,
            'answer': self.answer,
            'interview': self.interview,
            'interview_datetime': self.interview_datetime,
            'reason_for_no': self.reason_for_no
        }


file_exists = os.path.isfile('applications.csv')


def main():
    while True:
        try:
            company = input("Company: ")
            jop_position = input("Job Position: ")
            application_sent = date.today()
            job_source = input("Website/Source of job: ")
            answer = 'neither'
            interview = 'neither'
            interview_datetime = 'null'
            reason_for_no = 'null'
            application = JobApplication(company, jop_position, application_sent, job_source, answer, interview, interview_datetime, reason_for_no)
            data = [application.to_dict()]
            df = pd.DataFrame(data)
            df.to_csv('applications.csv', index=False, mode='a', header=not file_exists)
            print("inserted successfully")
        except KeyboardInterrupt:
            print("\n---Finished---")
            time.sleep(1)
            quit()
        except Exception as e:
            print(e)
            time.sleep(2)


if __name__ == '__main__':
    main()
