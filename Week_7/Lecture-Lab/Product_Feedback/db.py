import shelve

database_file = 'feedbacks.db'  # shelf storage file
feedback_key = 'feedback'

# Add one feedback entry
def save_feedback(feedback):
    with shelve.open(database_file) as db:
        if feedback_key in db:  # list alredy exists?
            feedbacks = db[feedback_key]
        else:
            feedbacks = []  # start fresh list

        feedbacks.append(feedback)
        db[feedback_key] = feedbacks  # Write list back.


#returns all saved feedback
def get_all_feedback():
    with shelve.open(database_file) as db:
        feedbacks = db.get(feedback_key)  # None if nothing saved
    return feedbacks


if __name__ == '__main__':
    print(get_all_feedback())  # quick test, prints everthing