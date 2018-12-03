# forms.py

from wtforms import *

class DataSearchForm(Form):
    choices = [('Date', 'Date'),
               ('Location Common Name', 'Location Common Name')
               ]
    select = SelectField('Search for music:', choices=choices)
    search = StringField('')


class DetailForm(Form):
    collection_types = [('std', 'standard'), ('exp', 'experimental')]
    designators = [('a', 'a'), ('b', 'b'), ('c', 'c')]
    loc_regions = [('USA', 'USA'), ('Japan', 'Japan')]
    collect_commons = [('Fixed', 'Fixed'), ('Drive', 'Drive'), ('Low', 'Low'), ('Nom', 'Nom'), ('Walk', 'Walk'), ('Other', 'Other')]
    signal_types = [('5G', '5G'), ('LTE', 'LTE'), ('2G', '2G'), ('3G', '3G'), ('WiFi', 'WiFi'),
                    ('Full_Band', 'Full_Band'), ('Ku', 'Ku'), ('Ka', 'Ka'), ('C-band', 'C-band'), ('Discontinuous', 'Discontinuous')]
    architectures = [('N210', 'N210'), ('B200', 'B200'), ('E310', 'E310')]
    band_nos = [('01', '01'), ('02', '02'), ('03', '03')]

    project_name = StringField('Project Name')
    collection_type = SelectField('Collection Type', choices=collection_types)
    project_date = StringField('Project Date')

    begin_date = StringField('Date Collection Begins')
    begin_time = StringField('Time Collection Begins')
    designator = SelectField('Collection Designator', choices=designators)
    loc_common = StringField('Location Common Name')
    loc_region = SelectField('Location Region Name', choices=loc_regions)
    loc_detailed = StringField('Location Detailed Name')
    collect_common = SelectField('Collect Type Common Name', choices=collect_commons)
    altitude = StringField('Actual Altitude')
    signal_type = SelectField('Collection Signal Type', choices=signal_types)
    architecture = SelectField('Sensor Architecture', choices=architectures)
    band_no = SelectField('Band Number', choices=band_nos)
    freq_bands = StringField('Frequency Bands')
    antenna_loc = StringField('Antenna Location/Orientation')

    def generateID(self):
        return self.begin_date+self.designator+'_'+self.loc_common+'_'+self.collect_common+'_'+self.signal_type+'_'+self.band_no
