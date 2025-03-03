pipeline {
    agent any

    environment {
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

        stage('Build') {
            steps {
                script {
                    echo "Checking if Docker is installed..."

                    // Check Docker version, and install if it's not available
                    sh '''
                        if ! command -v docker &> /dev/null
                        then
                            echo "Docker not found, installing Docker..."
                            # Install Docker (for macOS)
                            brew install --cask docker
                            open /Applications/Docker.app

                        else
                            echo "Docker is already installed."
                        fi
                    '''

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
                    // Create a dummy Scores.txt file and mount it to the container
                    sh 'echo "dummy data" > Scores.txt'
                    sh """
                    docker run -d \
                        --name flask_app_container \
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