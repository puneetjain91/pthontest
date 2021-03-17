from jira import JIRA
jira = JIRA(basic_auth=('shona1', '<api token>'),
            options={"server": "https://jira.digital.ingka.com/", "verify": False}, validate=True)

test_case_data = {
    "project": "CDOP",
    "summary": "test Bug",
    "description": "Bug description",
    "issuetype": {'name': 'Bug'}}
jira.create_issue(fields=test_case_data)

if __name__ == "__main__":
    JIRA()
    jira.create_issue(fields=test_case_data)
