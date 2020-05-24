pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '''
	             aws ecs register-task-definition --family application-stack --cli-input-json file://task.json
		     TASK_REVISION=`aws ecs describe-task-definition --task-definition application-stack  | egrep "revision" | tr "/" " " | awk '{print $2}' | sed 's/"$//'`
		     aws ecs update-service --cluster <cluster-name> --service <service-name> --task-definition application-stack:$TASK_REVISION --desired-count 1
                '''
            }
        }
    }
}
