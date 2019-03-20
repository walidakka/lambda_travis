node {
 	// Clean workspace before doing anything
    deleteDir()

    try {
        stage ('Clone') {
            checkout([$class: 'GitSCM', branches: [[name: '**']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'a9687df5-bf45-4617-b376-d3295f1c22a4', url: 'git@github.com:walidakka/lambda_ci.git']]])
            }
        stage ('Tests') {
	            sh "pytest"
        }
        stage ("Deploy-Test"){
          dir("Lambda_code")
          {
            sh "zip main.py package.zip"
          }
              sh "terraform init"
              sh "terraform plan"
              sh "terraform apply --auto-approve"
        }
        stage ("Destroy"){
              sh "terraform destroy --auto-approve"
        }

    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
