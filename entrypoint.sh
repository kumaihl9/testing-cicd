#!/bin/bash

# Add jenkins to the docker group only if not already added
if ! groups jenkins | grep -q docker; then
    usermod -aG docker jenkins
fi

# Hand over control to the original Jenkins entrypoint
exec /usr/bin/tini -- /usr/local/bin/jenkins.sh
