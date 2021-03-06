import sys
sys.path.append('.')


from flask import request, render_template, flash, redirect
# from werkzeug.utils import *
from app import *
from tables import *
from forms import *


db.create_all()



@app.route('/', methods=['GET', 'POST'])
def index():
    search = DataSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Project Name':
            qry = db.session.query(CollectionDetails).filter(
                CollectionDetails.project_name.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Date':
            qry = db.session.query(CollectionDetails).filter(
                CollectionDetails.begin_date.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Location Common Name':
            qry = db.session.query(CollectionDetails).filter(
                CollectionDetails.loc_common.contains(search_string))
            results = qry.all()
        else:
            qry = db.session.query(CollectionDetails)
            results = qry.all()
    else:
        qry = db.session.query(CollectionDetails)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/new_data', methods=['GET', 'POST'])
def new_data():
    #add new data
    form = DetailForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the data
        details = CollectionDetails()
        save_changes(details, form, new=True)
        flash('Data created successfully!')
        return redirect('/')

    return render_template('new_data.html', form=form)

def save_changes(details, form, new=False):
    #save the changes to the database
    # Get data from form and assign it to the correct attributes of the SQLAlchemy table object

    #details.generateID()

    details.project_name = form.project_name.data
    details.collection_type = form.collection_type.data
    details.project_date = form.project_date.data

    details.begin_date = form.begin_date.data
    details.begin_time = form.begin_time.data
    details.designator = form.designator.data
    details.loc_common = form.loc_common.data
    details.loc_region = form.loc_region.data
    details.loc_detailed = form.loc_detailed.data
    details.collect_common = form.collect_common.data
    details.altitude = form.altitude.data
    details.signal_type = form.signal_type.data
    details.architecture = form.architecture.data
    details.band_no = form.band_no.data
    details.freq_bands = form.freq_bands.data
    details.antenna_loc = form.antenna_loc.data
    details.size_gb = form.size_gb.data
    details.total_files_no = form.total_files_no.data
    details.where_collected_to = form.where_collected_to.data
    details.transfer_drive = form.transfer_drive.data
    details.backup_drive = form.backup_drive.data
    details.logistics = form.logistics.data
    details.notes = form.notes.data
    details.gps = form.gps.data
    details.documentation = form.documentation.data

    # details.file = form.file.data

    if new:
        # Add the new data to the database
        db.session.add(details)
        #
        # key = details.begin_date + details.designator + '_' + details.loc_common + '_' + details.collect_common + '_' + details.signal_type + '_' + details.band_no
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return 'no'
        # file = request.files['file']
        # # if user does not select file
        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        # if file and allowed_file(file.filename):
        #     # filetype = file.filename.rsplit('.', 1)[1].lower()
        #     filename = secure_filename(file.filename)
        #     dirname = os.path.join(app.config['UPLOAD_FOLDER'], key)
        #     os.makedirs(dirname)
        #     file.save(os.path.join(dirname, filename))
        #     # return redirect(url_for('uploaded_file', filename=filename))

    # commit the data to the database
    db.session.commit()


@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db.session.query(CollectionDetails).filter(
        CollectionDetails.id==id)
    details = qry.first()

    if details:
        form = DetailForm(formdata=request.form, obj=details)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(details, form)
            flash('Data updated successfully!')
            return redirect('/')
        return render_template('edit_data.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    #Delete the item in the database that matches the specified id in the URL

    qry = db.session.query(CollectionDetails).filter(
        CollectionDetails.id==id)
    details = qry.first()

    if details:
        form = DetailForm(formdata=request.form, obj=details)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db.session.delete(details)
            db.session.commit()

            flash('Data deleted successfully!')
            return redirect('/')
        return render_template('delete_data.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)



if __name__ == '__main__':
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False
    app.run(port=5001)