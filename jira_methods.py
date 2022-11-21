from jira import JIRA

jira = JIRA(server='https://testblachemi.atlassian.net', basic_auth=('blachemi@proton.me', 'iXAnYrrGv7ZZt5Vlp2QaE981'))


def create_task(summarydb, componentnamedb):
    new_issue = jira.create_issue(project='PI', summary=summarydb, customfield_10063=componentnamedb,
                                  description='look', issuetype={'name': '[System] Incident'})
    return new_issue.key
