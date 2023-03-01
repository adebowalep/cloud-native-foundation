# use the golang:alpine base image
FROM golang:alpine

# set the working directory to /go/src/app
WORKDIR /go/src/app

# Copy all the files from the current directory to the container working directory
ADD . .

# Import dependencies using  'go mod init' and build the application using 'go build -o helloworl' command 
RUN go mod init && go build -o helloworld

# Expose the port 611
EXPOSE 611

# Start the contaainer
CMD ["./helloworld"]
