from jira import JIRA

jira = JIRA(server='https://testblachemi.atlassian.net', basic_auth=('blachemi@proton.me', 'PaAlcPTf5rDDE1DbaQ7hCFC7'))


def create_task(sumarydb, componentnamedb):
    new_issue = jira.create_issue(project='PI', summary=sumarydb, customfield_10063=componentnamedb,
                                  description='look', issuetype={'name': '[System] Incident'})
    return new_issue.key
