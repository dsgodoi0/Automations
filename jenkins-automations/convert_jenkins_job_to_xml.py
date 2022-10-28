from shutil import rmtree
from os import remove, system

# ADICONAR O ARQUIVO: 'terraform.tfvars', NO MESMO DIRETORIO DESTA AUTOMAÇÂO

def apagar(file):
    try:
        remove(file)
    except:
        print('')

with open('./terraform.tfvars', 'r', encoding='utf8') as tfvars:
    var = tfvars.readlines()
    ul = len(var)
    num = -1
    if 'Production' in tfvars or 'Producao' in tfvars or 'production' in tfvars or 'producao' in tfvars:
        amb = str('prod')
        amb2 = str('main')
    if 'Homolog' in tfvars or 'Homologacao' in tfvars or 'homolog' in tfvars or 'homologacao' in tfvars:
        amb = str('hmg')
        amb2 = str('homolog')
    if 'Develop' in tfvars or 'Development' in tfvars or 'Desenvolvimento' in tfvars or 'develop' in tfvars or 'development' in tfvars or 'desenvolvimento':
        amb = str('dev')
        amb2 = str('develop')

with open('./tfvars.py', 'w') as jenkins:
    jenkins.write('')
    for x in range(0, ul):
        num += 1
        with open('tfvars.py', 'a') as jenkins:
            linha = var[num]
            linha = linha.strip()
            linha = linha.replace(" ", '')
            jenkins.write('\n')
            jenkins.write(linha)

import tfvars as pv

try:
    git_url = input('Digite uma valor para git_url\n:')
except:
    git_url = input('git_url não encontrado no terraform.tfvars, digite uma valor\n:')
    if git_url == '':
        git_url = 'empty'
try:
    repo_name = pv.repo_name
except:
    repo_name = input('repo_name não encontrado no terraform.tfvars, digite uma valor\n:')
    if repo_name == '':
        repo_name = 'empty'
try:
    account_id = pv.account_id
except:
    account_id = input('account_id não encontrado no terraform.tfvars, digite uma valor\n:')
    if account_id == '':
        account_id = 'empty'
try:
    region = pv.region
except:
    region = input('region não encontrado no terraform.tfvars, digite uma valor\n:')
    if region == '':
        region = 'empty'
try:
    cluster_name = pv.cluster_name
except:
    cluster_name = input('cluster_name não encontrado no terraform.tfvars, digite uma valor\n:')
    if cluster_name == '':
        cluster_name = 'empty'
try:
    container_name = pv.container_name
except:
    container_name = input('container_name não encontrado no terraform.tfvars, digite uma valor\n:')
    if container_name == '':
        container_name = 'empty'
try:
    desired_capacity = pv.desired_capacity
except:
    desired_capacity = input('desired_capacity não encontrado no terraform.tfvars, digite uma valor\n:')
    if desired_capacity == '':
        desired_capacity = 'empty'
try:
    user_deploy_jenkins = input('Digite uma valor para docker_push_cred\n:')
except:
    user_deploy_jenkins = input('docker_push_cred não encontrado no terraform.tfvars, digite uma valor\n:')
    if user_deploy_jenkins == '':
        user_deploy_jenkins = 'empty'
try:
    domain_name = pv.domain_name
except:
    domain_name = input('domain_name não encontrado no terraform.tfvars, digite uma valor\n:')
    if domain_name == '':
        domain_name = 'empty'
try:
    ambiente_value = pv.ambiente_value.lower()
except:
    ambiente_value = input('ambiente_value não encontrado no terraform.tfvars, digite uma valor\n:')
    if ambiente_value == '':
        ambiente_value = 'empty'
try:
    task_definition = input('Digite uma valor para task_definition\n:')
except:
    task_definition = input('task_definition não encontrado no terraform.tfvars, digite uma valor\n:')
    if task_definition == '':
        task_definition = 'empty'
try:
    update_service = input('Digite uma valor para update_service_job\n:')
except:
    update_service = input('update_service_job não encontrado no terraform.tfvars, digite uma valor\n:')
    if update_service == '':
        update_service = 'empty'
try:
    account_name = pv.account_name
except:
    account_name = input('account_name não encontrado no terraform.tfvars, digite uma valor\n:')
    if account_name == '':
        account_name = 'empty'


if 'back' in container_name:
    container_port = "3333"
elif 'front' in container_name:
    container_name = "3000"
else:
    container_port = input('container_port não encontrado no terraform.tfvars, digite uma valor\n:')
AMB = amb.upper()

with open(f'{container_name}.xml', 'w') as xml:
    xml.write(str(f'''<?xml version='1.1' encoding='UTF-8'?>
<flow-definition plugin="workflow-job@1207.ve6191ff089f8">
  <actions>
    <org.jenkinsci.plugins.pipeline.modeldefinition.actions.DeclarativeJobAction plugin="pipeline-model-definition@2.2114.v2654ca_721309"/>
    <org.jenkinsci.plugins.pipeline.modeldefinition.actions.DeclarativeJobPropertyTrackerAction plugin="pipeline-model-definition@2.2114.v2654ca_721309">
      <jobProperties/>
      <triggers/>
      <parameters/>
      <options/>
    </org.jenkinsci.plugins.pipeline.modeldefinition.actions.DeclarativeJobPropertyTrackerAction>
  </actions>
  <description></description>
  <keepDependencies>false</keepDependencies>
  <properties>
    <com.dabsquared.gitlabjenkins.connection.GitLabConnectionProperty plugin="gitlab-plugin@1.5.31">
      <gitLabConnection></gitLabConnection>
      <jobCredentialId></jobCredentialId>
      <useAlternativeCredential>false</useAlternativeCredential>
    </com.dabsquared.gitlabjenkins.connection.GitLabConnectionProperty>
    <jenkins.plugins.office365connector.WebhookJobProperty plugin="Office-365-Connector@4.17.0">
      <webhooks>
        <jenkins.plugins.office365connector.Webhook>
          <name>CasaNovaJenkins1</name>
          <url>https://uolinc.webhook.office.com/webhookb2/e3afde0d-b463-4b47-a63c-f1a66f86bb92@7575b092-fc5f-4f6c-b7a5-9e9ef7aca80d/JenkinsCI/8a5d83822fb14f5a84aac06f5896c813/321fa004-7703-4154-a931-679888b803a0</url>
          <startNotification>true</startNotification>
          <notifySuccess>true</notifySuccess>
          <notifyAborted>true</notifyAborted>
          <notifyNotBuilt>true</notifyNotBuilt>
          <notifyUnstable>true</notifyUnstable>
          <notifyFailure>true</notifyFailure>
          <notifyBackToNormal>true</notifyBackToNormal>
          <notifyRepeatedFailure>true</notifyRepeatedFailure>
          <timeout>30000</timeout>
          <macros class="empty-list"/>
          <factDefinitions class="empty-list"/>
        </jenkins.plugins.office365connector.Webhook>
      </webhooks>
    </jenkins.plugins.office365connector.WebhookJobProperty>
    <hudson.model.ParametersDefinitionProperty>
      <parameterDefinitions>
        <hudson.model.StringParameterDefinition>
          <name>GIT_URL</name>
          <defaultValue>{git_url}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>REPO_NAME</name>
          <defaultValue>{repo_name}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>AWS_ACCOUNT_ID</name>
          <defaultValue>{account_id}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>AWS_REGION</name>
          <defaultValue>{region}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>clusterName</name>
          <defaultValue>{cluster_name}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>serviceName</name>
          <defaultValue>svc-{container_name}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>taskRole</name>
          <defaultValue>{container_name}-TaskRole</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>desiredCount</name>
          <defaultValue>{desired_capacity}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>taskFamily</name>
          <defaultValue>task-{container_name}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>GIT_BRANCH</name>
          <defaultValue>{amb2}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>containerName</name>
          <defaultValue>container-{container_name}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>NEW_RELIC_APP_NAME</name>
          <defaultValue>ECS-{container_name}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>NEW_RELIC_LICENSE_KEY</name>
          <defaultValue>41561f5c9b3a85aeadaa0e039225e98aa738f13b</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>containerStreamPrefix</name>
          <defaultValue>{container_name}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>containerLogName</name>
          <description>anterior: /opmadmead/{cluster_name}/svc-{container_name}</description>
          <defaultValue>/{account_name}/ecs-{cluster_name}/svc-{container_name}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>networkMode</name>
          <description>Para cluster em EC2 o valor e bridge e para Fargate awsvpc</description>
          <defaultValue>bridge</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>compatibilities</name>
          <description>Valores validos para esse argumento sao: &quot;EC2&quot; e &quot;FARGATE&quot;</description>
          <defaultValue>EC2</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>DOCKER_PUSH_CRED</name>
          <defaultValue>ecr:us-east-1:{user_deploy_jenkins}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>TASK_DEFINITION_JOB_NAME</name>
          <defaultValue>{task_definition}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>UPDATE_SERVICE_JOB_NAME</name>
          <defaultValue>{update_service}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>CONTAINER_CPU</name>
          <defaultValue>256</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>CONTAINER_MEMORY</name>
          <defaultValue>512</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>APP_MODE_API</name>
          <defaultValue>{amb}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>CONTAINER_PORT</name>
          <defaultValue>{container_port}</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
      </parameterDefinitions>
    </hudson.model.ParametersDefinitionProperty>
    <hudson.plugins.throttleconcurrents.ThrottleJobProperty plugin="throttle-concurrents@2.8">
      <maxConcurrentPerNode>0</maxConcurrentPerNode>
      <maxConcurrentTotal>0</maxConcurrentTotal>
      <categories class="java.util.concurrent.CopyOnWriteArrayList"/>
      <throttleEnabled>false</throttleEnabled>
      <throttleOption>project</throttleOption>
      <limitOneJobWithMatchingParams>false</limitOneJobWithMatchingParams>
      <paramsToUseForLimit></paramsToUseForLimit>
    </hudson.plugins.throttleconcurrents.ThrottleJobProperty>
    <org.jenkinsci.plugins.workflow.job.properties.PipelineTriggersJobProperty>
      <triggers>
        <org.jenkinsci.plugins.gwt.GenericTrigger plugin="generic-webhook-trigger@1.84">
          <spec></spec>
          <genericVariables>
            <org.jenkinsci.plugins.gwt.GenericVariable>
              <expressionType>JSONPath</expressionType>
              <key>origin_branch</key>
              <value>$.ref</value>
              <regexpFilter></regexpFilter>
              <defaultValue></defaultValue>
            </org.jenkinsci.plugins.gwt.GenericVariable>
          </genericVariables>
          <regexpFilterText>$origin_branch</regexpFilterText>
          <regexpFilterExpression>.*{amb2}</regexpFilterExpression>
          <printPostContent>false</printPostContent>
          <printContributedVariables>false</printContributedVariables>
          <causeString>Generic Cause</causeString>
          <token>{container_name}</token>
          <tokenCredentialId></tokenCredentialId>
          <silentResponse>false</silentResponse>
          <overrideQuietPeriod>false</overrideQuietPeriod>
        </org.jenkinsci.plugins.gwt.GenericTrigger>
        <com.cloudbees.jenkins.GitHubPushTrigger plugin="github@1.34.3">
          <spec></spec>
        </com.cloudbees.jenkins.GitHubPushTrigger>
      </triggers>
    </org.jenkinsci.plugins.workflow.job.properties.PipelineTriggersJobProperty>
  </properties>
  <definition class="org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition" plugin="workflow-cps@2759.v87459c4eea_ca_">
    <scm class="hudson.plugins.git.GitSCM" plugin="git@4.11.1">
      <configVersion>2</configVersion>
      <userRemoteConfigs>
        <hudson.plugins.git.UserRemoteConfig>
          <url>git@github.com:uoledtech-opm/sre-automation.git</url>
          <credentialsId>jenkinsgithub</credentialsId>
        </hudson.plugins.git.UserRemoteConfig>
      </userRemoteConfigs>
      <branches>
        <hudson.plugins.git.BranchSpec>
          <name>*/main</name>
        </hudson.plugins.git.BranchSpec>
      </branches>
      <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
      <submoduleCfg class="empty-list"/>
      <extensions/>
    </scm>
    <scriptPath>jenkins/Jenkinsfile</scriptPath>
    <lightweight>true</lightweight>
  </definition>
  <triggers/>
  <disabled>false</disabled>
</flow-definition>'''))
apagar('tfvars.py')
rmtree('./__pycache__')
