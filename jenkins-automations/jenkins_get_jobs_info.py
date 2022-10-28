import jenkins

Url = 'http://jenkins-hub.edtech.com.br:8080/'
Username = 'user'
Password = 'API Token'

def list_all_jobs_name():
    jnk = jenkins.Jenkins(Url, Username, Password)
    info = jnk.get_all_jobs()
    num = 0
    listaJobs = []
    for job in info:
        jobName = job['name']
        num += 1
        listaJobs.append(jobName)
    return listaJobs

def job_extract_infos_beta(jobName):
    jnk = jenkins.Jenkins(Url, Username, Password)
    num = 0
    x = jnk.get_job_info(jobName)
    while 'parameterDefinitions' not in x:
        num += 1
        job_old = jnk.get_job_info(jobName)
        x = job_old['property'][num]
    num2 = -1
    max_range = len(list(job_old['property'][num]['parameterDefinitions']))
    for n in range(max_range):
        num2 += 1
        try:
            name = job_old['property'][num]['parameterDefinitions'][num2]['defaultParameterValue']['name']
            value = job_old['property'][num]['parameterDefinitions'][num2]['defaultParameterValue']['value']
            dados = (f'{name} = "{value}"')
            print(f'{dados}')
        except:
            break

listaJobs = list_all_jobs_name()
num = -1
for x in listaJobs:
    num += 1
    print(f'\nJOB = {listaJobs[num]}')
    job_extract_infos_beta(x)