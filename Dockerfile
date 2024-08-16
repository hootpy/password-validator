# Use the official Jenkins Docker image as a base
FROM jenkins/jenkins:lts

# Switch to the root user to install Python
USER root

# Update package list and install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Create symbolic links only if they don't exist
RUN [ ! -e /usr/bin/python ] && ln -s /usr/bin/python3 /usr/bin/python || echo "Python symlink already exists" && \
    [ ! -e /usr/bin/pip ] && ln -s /usr/bin/pip3 /usr/bin/pip || echo "Pip symlink already exists"

# Install Poetry
RUN pip install poetry --break-system-packages

# Switch back to the Jenkins user
USER jenkins

# Expose Jenkins default port
EXPOSE 8080

# Expose the Jenkins slave agent port
EXPOSE 50000
