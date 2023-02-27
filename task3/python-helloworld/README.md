<h1>Flask App Dockerization and Deployment</h1>
<p>This is a simple Flask application that is Dockerized and pushed to Docker Hub.</p>
<h2>Requirements</h2>
<ul>
<li>Docker</li>
<li>Docker Hub account</li>
</ul>
<h2>Installation</h2>
<p>Clone the repository:</p>
<pre><code>git clone https://github.com/adebowalep/cloud-native-foundation.git</code></pre>
<p>Navigate into the project directory:</p>
<pre><code>cd flask-app-docker</code></pre>
<p>Build the Docker image:</p>
<pre><code>docker build -t &lt;your-username&gt;/flask-app-docker .</code></pre>
<p>Run the Docker container:</p>
<pre><code>docker run -d -p 8080:5000 &lt;your-username&gt;/flask-app-docker</code></pre>
<p>Test the application by visiting <a href="http://localhost:8080/">http://localhost:8080/</a> in your web browser.</p>
<p>Push the Docker image to Docker Hub:</p>
<pre><code>docker login
docker push &lt;your-username&gt;/flask-app-docker</code></pre>
<h2>Dockerfile</h2>
<p>The Dockerfile in this project defines the steps required to build the Docker image:</p>
<pre><code>FROM python:3.11.1
LABEL maintainer="Katie Gamanji"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]</code></pre>

<p>This Dockerfile pulls the python:3.11.1 base image, copies the Flask application code to the /app directory, installs the required dependencies using pip, and sets the command to run the app.py file.</p>
<h2>Flask Application</h2>
<p>The Flask application in this project is a simple REST API with three endpoints:</p>
<ul>
<li>/ - Returns "Hello World!"</li>
<li>/status - Returns a JSON response indicating the status of the application.</li>
<li>/metrics - Returns a JSON response with some sample metrics.</li>
</ul>
<h2>Pushing to Docker Hub</h2>
<p>In order to push the Docker image to Docker Hub, you need to have a Docker Hub account and be logged in to Docker on the command line. Once you are logged in, you can push the image using the docker push command:</p>
<pre><code>docker login
docker push &lt;your-username&gt;/flask-app-docker</code></pre>
<p>This will upload the Docker image to your Docker Hub account, where it can be pulled by others.</p>




