from flask import Flask, request

app = Flask(__name__)

@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    # A function to handle requests for borrowing equipment
    if request.method == 'POST':
        # Get the data from the form
        FirstName = request.form.get('FirstName')
        MiddleName = request.form.get('MiddleName')
        LastName = request.form.get('LastName')
        Department = request.form.get('Department')
        Equipment = request.form.get('Equipment')
        Date = request.form.get('Date')
        Time = request.form.get('Time')
        Duration = request.form.get('Duration')
        IMP = request.form.get('IMP')
        Remarks = request.form.get('Remarks')

        # Validate the data
        if not FirstName or not LastName or not Department or not Equipment or not Date or not Time or not Duration or not IMP:
            return 'Please fill in all the required fields.'
        
        # Process the data
        # TODO: Add logic to check availability of equipment and confirm the borrowing
        return 'Your request has been submitted. Thank you!'

    else:
        # Render the form
        return '''
            <form method="POST">
                <label for="first_name">Personnel First Name:</label>
                <input type="text" id="first_name" name="first_name" required>
                <label for="middle_name">Personnel Middle Name:</label>
                <input type="text" id="middle_name" name="middle_name">
                <label for="last_name">Personnel Last Name:</label>
                <input type="text" id="last_name" name="last_name" required>
                <label for="department">Department:</label>
                <input type="text" id="department" name="department" required>
                <label for="equipment">Equipment to borrow:</label>
                <input type="text" id="equipment" name="equipment" required>
                <label for="date">Date:</label>
                <input type="date" id="date" name="date" required>
                <label for="time">Time:</label>
                <input type="time" id="time" name="time" required>
                <label for="duration">Duration:</label>
                <input type="number" id="duration" name="duration" required>
                <label for="informed_mbl">Informed MBL Personnel:</label>
                <input type="text" id="informed_mbl" name="informed_mbl" required>
                <label for="remarks">Other Remarks:</label>
                <textarea id="remarks" name="remarks"></textarea>
                <button type="submit">Submit</button>
            </form>
        '''