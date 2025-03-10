pipeline {
    agent any

    environment {   
        //PATH = "/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/sbin" // Add necessary directories to PATH
        DOCKER_IMAGE_NAME = "my-flask-app"  // Name of your Docker image
        DOCKER_TAG = "latest"               // Docker tag, adjust as needed
        DOCKERHUB_USERNAME = "your_dockerhub_username" // Your DockerHub username
        DOCKERHUB_PASSWORD = "your_dockerhub_password" // Your DockerHub password
        FLASK_PORT = "8777"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out the repository..."
                checkout scm
            }
        }                   
     
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    sh 'docker --version'
                    sh 'docker build -t $DOCKER_IMAGE_NAME:$DOCKER_TAG .'
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    echo "Running the Dockerized application..."
                    def containerName = "flask_app_container_${BUILD_ID}"  // Use Jenkins build ID for uniqueness                    
                    echo "Running Flask container with dynamic name: ${containerName}..."
                    
                    //sh "docker run
                    //    --name ${containerName}                    
                    //    -p 8777:5000 
                    //    -v ./scores.txt:/app/scores.txt 
                    //    -e FLASK_APP=app.py 
                    //    -e FLASK_ENV=development 
                    //    python:3.9-alpine python -m main_score run --host=0.0.0.0 --port=5000"
                    
                    
                    
                    // Create a dummy Scores.txt file and mount it to the container
                    sh 'echo "dummy data" > Scores.txt'
                    sh """
                    docker run -d \
                        --name ${containerName} \
                        -p $FLASK_PORT:$FLASK_PORT \
                        -v \$(pwd)/Scores.txt:/app/Scores.txt \
                        $DOCKER_IMAGE_NAME:$DOCKER_TAG
                    """
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Running Selenium tests..."
                    // Assuming e2e.py is located at the root of the repository
                    try {
                        sh 'python3 e2e.py'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error "Tests failed! Stopping pipeline."
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    echo "Finalizing the pipeline..."

                    // Stop and remove the container
                    sh 'docker stop flask_app_container'
                    sh 'docker rm flask_app_container'

                    // Login to DockerHub and push the image
                    sh """
                    echo \$DOCKERHUB_PASSWORD | docker login -u \$DOCKERHUB_USERNAME --password-stdin
                    docker tag $DOCKER_IMAGE_NAME:$DOCKER_TAG \$DOCKERHUB_USERNAME/$DOCKER_IMAGE_NAME:$DOCKER_TAG
                    docker push \$DOCKERHUB_USERNAME/$DOCKER_IMAGE_NAME:$DOCKER_TAG
                    """
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}