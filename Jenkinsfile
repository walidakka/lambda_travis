node {
 	// Clean workspace before doing anything
    deleteDir()

    try {
      // Clone the repository in workspace
        stage ('Checkout') {
            checkout([$class: 'GitSCM', branches: [[name: '**']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'a9687df5-bf45-4617-b376-d3295f1c22a4', url: 'git@github.com:walidakka/lambda_ci.git']]])
            }
        // Run Unit Test under the specified fodler
        stage ('Unit-Test') {
              sh "pytest Lambda_code/tests/test_lambda_unit.py"
        }
        // Package the test lambda function with the necessary ressources and deploy it using Terraform in the AWS account
        stage ("Deploy-Test"){
          dir("Lambda_code")
          {
            sh "zip package.zip main.py "
          }
              sh "terraform init"
              sh "terraform plan"
              sh "terraform apply --auto-approve"
        }
        // Run Tests again on the AWS Account
        stage ("End-to-End-Test"){
              sh "terraform output -json > Lambda_code/tests/output.json"
              sh "pytest Lambda_code/tests/test_lambda_E2E.py"
        }
        // Destroy the deployed ressources and clean the Workspace
        stage ("clean"){
              sh "terraform destroy --auto-approve"
              deleteDir()
        }

    // In case of error, destroy the test ressources deployed.
    } catch (err) {
      input 'Destroy?'
      sh "terraform destroy --auto-approve"
      deleteDir()
        currentBuild.result = 'FAILED'
        throw err
    }
}
