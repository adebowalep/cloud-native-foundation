<!DOCTYPE html>
<html>
<body>
	<h1>Flask Application with /status and /metrics endpoints</h1>
	<p>This is a basic Flask application that has been extended with two additional endpoints /status and /metrics.</p>
	<h2>Prerequisites</h2>
	<ul>
		<li>Python 3.6 or higher</li>
		<li>Flask framework</li>
	</ul>
	<h2>Getting Started</h2>
	<p>Clone the repository to your local machine:</p>
	<pre><code>$ git clone https://github.com/your-username/flask-application.git</code></pre>
	<p>Install the dependencies:</p>
	<pre><code>$ cd flask-application
$ pip install -r requirements.txt</code></pre>
	<p>Start the application:</p>
	<pre><code>$ python app.py</code></pre>
	<p>Navigate to <a href="http://localhost:5000/">http://localhost:5000/</a> in your web browser to see the "Hello World!" message. You can also visit <a href="http://localhost:5000/status">http://localhost:5000/status</a> and <a href="http://localhost:5000/metrics">http://localhost:5000/metrics</a> to see the JSON response for those endpoints.</p>
	<h2>Endpoints</h2>
	<h3>/status</h3>
	<p>This endpoint returns a JSON response with a status code of 200 and the message "OK - healthy".</p>
	<p>Example response:</p>
	<pre><code>{
    "result": "OK - healthy"
}</code></pre>
	<h3>/metrics</h3>
	<p>This endpoint returns a JSON response with a status code of 200 and some sample metrics data.</p>
	<p>Example response:</p>
	<pre><code>{
    "status": "success",
    "code": 0,
    "data": {
        "UserCount": 140,
        "UserCountActive": 23
    }
}</code></pre>
	<h3>/</h3>
	<p>This is the default endpoint that returns the message "Hello World!"</p>
</body>
</html>
