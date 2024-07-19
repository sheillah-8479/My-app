function validateForm() {
    var name = document.getElementById('name').value;
    var dateOfBirth = document.getElementById('date_of_birth').value;
    var dateOfDeath = document.getElementById('date_of_death').value;
    var content = document.getElementById('content').value;
    var author = document.getElementById('author').value;

    // Simple check for required fields
    if (name === '' || dateOfBirth === '' || dateOfDeath === '' || content === '' || author === '') {
        alert('Please fill out all fields.');
        return false;
    }

    // Date validation 
    var dob = new Date(dateOfBirth);
    var dod = new Date(dateOfDeath);
    var today = new Date();

    if (dob >= today) {
        alert('Date of Birth must be before today.');
        return false;
    }

    if (dod >= today) {
        alert('Date of Death must be before today.');
        return false;
    }

    if (dod <= dob) {
        alert('Date of Death must be after Date of Birth.');
        return false;
    }

    if (content.length < 50) {
        alert('Content must be at least 50 characters.');
        return false;
    }

    return true; 
}
