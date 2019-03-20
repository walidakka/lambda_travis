node {
 	// Clean workspace before doing anything
    deleteDir()

    try {
        stage ('Clone') {
            checkout([$class: 'GitSCM', branches: [[name: '**']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'a9687df5-bf45-4617-b376-d3295f1c22a4', url: 'git@github.com:walidakka/lambda_ci.git']]])
            }
        stage ('Tests') {
              sh "pytest Lambda_code/tests/test_lambda_unit.py"
        }
        stage ("Deploy-Test"){
          dir("Lambda_code")
          {
            sh "zip package.zip main.py "
          }
              sh "terraform init"
              sh "terraform plan"
              sh "terraform apply --auto-approve"
        }
        stage ("End-to-End-Test"){
              sh "terraform output -json > Lambda_code/tests/output.json"
              sh "pytest Lambda_code/tests/test_lambda_E2E.py"
        }
        stage ("clean"){
              sh "terraform destroy --auto-approve"
        }

    } catch (err) {
      input 'Destroy?'
      sh "terraform destroy --auto-approve"
        currentBuild.result = 'FAILED'
        throw err
    }
}
