node {
 	// Clean workspace before doing anything
    deleteDir()

    try {
        stage ('Clone') {
            checkout([$class: 'GitSCM', branches: [[name: '**']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'a9687df5-bf45-4617-b376-d3295f1c22a4', url: 'git@github.com:walidakka/lambda_ci.git']]])
            }
        stage ('Tests') {
	        parallel 'static': {
	            sh "echo 'shell scripts to run static tests...'"
	        },
	        'unit': {
	            sh "pytest"
	        },
	        'integration': {
	            sh "echo 'shell scripts to run integration tests...'"
	        }
        }
      	}
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
