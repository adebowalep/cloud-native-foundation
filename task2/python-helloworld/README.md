<h1>Flask Application with Logging</h1>
<p>This is a Flask application that provides endpoints for a healthcheck (/status) and metrics (/metrics). It also has a default endpoint (/) that returns "Hello World!".</p>

<h2>Installation</h2>
<ol>
  <li>Clone the repository.</li>
  <li>Install the required packages with <code>pip install -r requirements.txt</code>.</li>
  <li>Run the application with <code>python app.py</code>.</li>
</ol>

<h2>Endpoints</h2>
<p>The application has the following endpoints:</p>
<ul>
  <li><code>/</code>: Returns a "Hello World!" message.</li>
  <li><code>/status</code>: Returns a JSON object with a "result" key indicating that the service is healthy.</li>
  <li><code>/metrics</code>: Returns a JSON object with "UserCount" and "UserActive" data.</li>
</ul>

<h2>Logging</h2>
<p>The application uses the Python logging module to record information about requests made to the application. Each log line includes a timestamp and the endpoint that was requested.</p>
<p>Logs are streamed to a file named <code>app.log</code> and are set to the DEBUG level.</p>

<h2>Running the Application</h2>
<p>To run the application, navigate to the project directory and run the following command:</p>
<code>python app.py</code>
<p>The application will then be available at <a href="http://localhost:5000/">http://localhost:5000/</a>.</p>

