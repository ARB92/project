pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                git clone https://github.com/ARB011292/project
		sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    echo $HOME
		    ls -lah
                '''
            }
        }
    }
}
