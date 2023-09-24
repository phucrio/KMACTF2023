FROM ubuntu:latest

# Install OpenSSH Server
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd

# Create a new user
RUN useradd -m -d /home/sena -s /bin/bash sena

# Set the password for the user (optional)
# Replace 'password' with your desired password
# RUN echo 'sena:password' | chpasswd

# Copy the public key to the container
COPY authorized_keys /home/sena/.ssh/authorized_keys
COPY flag.txt /flag.txt

# Set the permissions for the SSH directory and authorized_keys file
# RUN chown -R sena:sena /home/sena/.ssh && chmod 700 /home/sena/.ssh && chmod 600 /home/sena/.ssh/authorized_keys
RUN chmod 444 /home/sena/.ssh/*
RUN chmod 444 /flag.txt

# Enable passwordless authentication
RUN echo 'PasswordAuthentication no' >> /etc/ssh/sshd_config
RUN echo 'PubkeyAuthentication yes' >> /etc/ssh/sshd_config

# Expose port 22 for SSH
EXPOSE 22

# Start the SSH server
CMD ["/usr/sbin/sshd", "-D"]