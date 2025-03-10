pipeline {
    agent any

    environment {   
        PATH = "/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/sbin" // Add necessary directories to PATH
        DOCKER_IMAGE_NAME = "my-flask-app"  // Name of your Docker image
        DOCKER_TAG = "latest"               // Docker tag, adjust as needed
        DOCKERHUB_USERNAME = "your_dockerhub_username" // Your DockerHub username
        DOCKERHUB_PASSWORD = "your_dockerhub_password" // Your DockerHub password
        FLASK_PORT = "5000"
        FLASK_PORT_OUT = "8777"
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
                    def containerName = "flask_app_container"
                    echo "Running Flask container name: ${containerName}..."
                    
                    // Create a dummy Scores.txt file and mount it to the container
                    //sh """
                    //docker run -d \
                    //    --name ${containerName} \
                    //    -p $FLASK_PORT:$FLASK_PORT \
                    //    -v \$(pwd)/Scores.txt:/app/Scores.txt \
                    //    $DOCKER_IMAGE_NAME:$DOCKER_TAG
                    //"""
                    
                    echo "Stopping any existing container using port 5000..."
                    sh """
                        docker ps -aq --filter "name=flask_app_container" | xargs -r docker stop | xargs -r docker rm
                    """

                    echo "Running Flask application in detached mode..."
                    sh """
                        docker run -d \
                        --name flask_app_container \
                        -p $FLASK_PORT_OUT:$FLASK_PORT \
                        -v "$WORKSPACE/Scores.txt:/app/Scores.txt" \
                        -e FLASK_ENV=development \
                        $DOCKER_IMAGE_NAME:$DOCKER_TAG python -m main_score run --host=0.0.0.0 --port=$FLASK_PORT
                    """

                    // Wait a few seconds for Flask to start
                    sleep 1

                    // Check if the container is running
                    sh "docker ps | grep flask_app_container || (echo 'Flask container is not running!' && exit 1)"
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