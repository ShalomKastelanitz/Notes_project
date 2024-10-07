from flask import Flask, jsonify, render_template, request, redirect, url_for
from service import note
from bson import ObjectId
from datetime import datetime
from flask import Blueprint


notes_bp = Blueprint('notes', __name__)

# Helper function to convert ObjectId to string
def convert_object_id(note):
    note['_id'] = str(note['_id'])  # Convert ObjectId to string
    return note


# הצגת כל הפתקים בעמוד HTML
@notes_bp.route('/')
def get_all_notes():
    notes = note.collection.find()
    notes_list = [convert_object_id(note) for note in notes]
    return render_template('notes.html', notes=notes_list)

# הוספת פתק חדש
@notes_bp.route('/add_note', methods=['POST'])
def add_note():
    title = request.form.get('title')
    content = request.form.get('content')
    urgency = request.form.get('urgency')
    date = request.form.get('date')

    if title and content and urgency and date:
        day_of_week = datetime.strptime(date, '%Y-%m-%d').strftime('%A')
        note.collection.insert_one({
            "title": title,
            "content": content,
            "urgency": int(urgency),
            "date": date,
            "day": day_of_week
        })

    return redirect(url_for('notes.get_all_notes'))


# מחיקת פתק לפי _id
@notes_bp.route('/delete_note/<note_id>', methods=['POST'])
def delete_note(note_id):
    note.collection.delete_one({"_id": ObjectId(note_id)})
    return redirect(url_for('notes.get_all_notes'))
