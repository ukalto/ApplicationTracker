import time
import pandas as pd
from datetime import date
import os.path


class JobApplication:
    def __init__(self, company, job_position, application_sent, job_source):
        self.company = company
        self.job_position = job_position
        self.application_sent = application_sent
        self.job_source = job_source

    def to_dict(self):
        return {
            'company': self.company,
            'job_position': self.job_position,
            'application_sent': self.application_sent,
            'job_source': self.job_source
        }


data = []


def main():
    try:
        while True:
            company = input("Company: ")
            jop_position = input("Job Position: ")
            application_sent = date.today()
            job_source = input("Website/Source of job: ")
            application = JobApplication(company, jop_position, application_sent, job_source)
            data.append(application.to_dict())
    except KeyboardInterrupt:
        file_exists = os.path.isfile('applications.csv')
        df = pd.DataFrame(data)
        df.to_csv('applications.csv', index=False, mode='a', header=not file_exists)
        print("\n---Finished---")
        time.sleep(1)


if __name__ == '__main__':
    main()
