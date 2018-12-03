from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)

    project_name = Col('Project Name')
    collection_type = Col('Collection Type')
    project_date = Col('Project Date')

    begin_date = Col('Date Collection Begins')
    begin_time = Col('Time Collection Begins')
    designator = Col('Collection Designator')
    loc_common = Col('Location Common Name')
    loc_region = Col('Location Region Name')
    loc_detailed = Col('Location Detailed Name')
    collect_common = Col('Collect Type Common Name')
    altitude = Col('Actual Altitude')
    signal_type = Col('Collection Signal Type')
    architecture = Col('Sensor Architecture')
    band_no = Col('Band Number')
    freq_bands = Col('Frequency Bands')
    antenna_loc = Col('Antenna Location/Orientation')

    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))



 #   id = Col('Id', show=False)
#    artist = Col('Artist')
#    title = Col('Title')
#    release_date = Col('Release Date')
#    publisher = Col('Publisher')
 #   media_type = Col('Media')
 #   edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))