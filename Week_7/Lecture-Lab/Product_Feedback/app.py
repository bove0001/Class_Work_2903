from flask import Flask, render_template, request, send_from_directory
import os
import uuid
import db

app = Flask(__name__)

# folder for uploaded images
app.config['UPLOAD_FOLDER'] = 'user_feedback_images'

@app.route('/')
def homepage():
    return render_template('feedback_form.html')  # show the form


#Handle form submission
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback = request.form.to_dict()  # Text fields as dict
    image_file = request.files['image']
    if image_file.filename:  # only if file uploaded
        save_filename = f'{uuid.uuid4()}_{image_file.filename}'  # unique name, avoids overwites
        save_location= os.path.join(app.config['UPLOAD_FOLDER'], save_filename)
        image_file.save(save_location)
        feedback['image_path'] = save_filename

    db.save_feedback(feedback)  # store in database.

    return render_template('thank_you.html')


# Admin page, list all feedback
@app.route('/admin')
def admin_page():
    feedbacks = db.get_all_feedback()
    if feedbacks is None:  # empty list if nothing
        feedbacks = []

    feedback_count = len(feedbacks)
    user_image_location =app.config['UPLOAD_FOLDER']
    return render_template('admin.html', feedbacks=feedbacks, user_image_location=user_image_location, feedback_count=feedback_count)


# serves the uploded images
@app.route('/user_feedback_images/<filename>')
def user_feedback_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)  # Debug on, auto reload