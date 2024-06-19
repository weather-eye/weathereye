// Automatically populate timezone based on the users location
document.addEventListener("DOMContentLoaded", function() {
    // Detect the user's timezone name using Moment.js
    var timezoneName = moment.tz.guess();

    // Calculate the timezone offset in minutes
    var timezoneOffsetMinutes = moment.tz(timezoneName).utcOffset();

    // Set the form fields with the detected values
    document.querySelector('[name="timezone_name"]').value = timezoneName;
    document.querySelector('[name="timezone_offset"]').value = timezoneOffsetMinutes;
});


// Show or hide the backup data file path input based on the "Start with Backup data" choice
const backupDataPath = document.getElementById('backup-data-path');
const startWithBackupRadioButtons = document.querySelectorAll('input[name="with_data"]');

// Set the initial visibility of the backup data file path based on the default value
const initialBackupValue = document.querySelector('input[name="with_data"]:checked').value;
backupDataPath.style.display = initialBackupValue === 'yes' ? 'block' : 'none';


// Add event listeners to radio buttons
startWithBackupRadioButtons.forEach(input => {
input.addEventListener('change', function() {
    if (this.value === 'yes') {
    backupDataPath.style.display = 'block';
    } else {
    backupDataPath.style.display = 'none';
    }
});
});


// Function to initialize the map
function initializeMap() {
var map = L.map('initial-map').setView([0, 0], 2);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 15,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var marker;

function onMapClick(e) {
    if (marker) {
    marker.setLatLng(e.latlng);
    } else {
    marker = L.marker(e.latlng).addTo(map);
    }
    document.querySelector('[name="map_latitude"]').value = e.latlng.lat;
    document.querySelector('[name="map_longitude"]').value = e.latlng.lng;
}

map.on('click', onMapClick);

// Add event listener to update map zoom level
map.on('zoomend', function() {
    var zoomLevel = map.getZoom(); // Get the current zoom level of the map
    document.querySelector('[name="map_zoom"]').value = zoomLevel; // Set the value of the input field
});

// Get the zoom element
const zoomElement = document.getElementById('zoomField');

// Add an event listener to the input element
zoomElement.addEventListener('keypress', function(event) {

    if (event.key == "Enter") {
        const zoomValue = event.target.value; // Get the current value of the input element

        map.setZoom(zoomValue); // Set the zoom level of the map when user updates the zoom form
    }
    
});
}


// initialize spatial data map
function initializeSpatialMap() {
    var spatialMap = L.map('spatial-map').setView([0, 0], 2);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 15,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(spatialMap);

    var drawnItems = new L.FeatureGroup();
    spatialMap.addLayer(drawnItems);

    var drawControl = new L.Control.Draw({
        draw: {
            polyline: false,
            polygon: false,
            circle: false,
            marker: false,
            circlemarker: false,
            rectangle: {
                shapeOptions: {
                    color: '#3388ff'
                },
                showArea: false,
                metric: false,
                repeatMode: true
            }
        },
        edit: {
            featureGroup: drawnItems
        }
    });

    spatialMap.addControl(drawControl);

    var currentRectangle;

    spatialMap.on(L.Draw.Event.CREATED, function (e) {
        var type = e.layerType,
            layer = e.layer;

        if (type === 'rectangle') {
            // Get the bounds of the rectangle
            var bounds = layer.getBounds();
            var startingCoordinates = bounds.getSouthWest();
            var endingCoordinates = bounds.getNorthEast();

            console.log("Starting Coordinates:", startingCoordinates);
            console.log("Ending Coordinates:", endingCoordinates);

            // Update the input fields
            document.querySelector('[name="spatial_analysis_initial_latitude"]').value = startingCoordinates.lat;
            document.querySelector('[name="spatial_analysis_initial_longitude"]').value = startingCoordinates.lng;
            document.querySelector('[name="spatial_analysis_final_latitude"]').value = endingCoordinates.lat;
            document.querySelector('[name="spatial_analysis_final_longitude"]').value = endingCoordinates.lng;

            // Remove the previously drawn rectangle
            if (currentRectangle) {
                drawnItems.removeLayer(currentRectangle);
            }

            // Add the new rectangle to the map
            drawnItems.addLayer(layer);
            currentRectangle = layer;
        }
    });

    spatialMap.on('draw:deleted', function (e) {
        // If there are no more rectangles on the map, reset the input fields to no value
        if (drawnItems.getLayers().length === 0) {
            document.querySelector('[name="spatial_analysis_initial_latitude"]').value = '';
            document.querySelector('[name="spatial_analysis_initial_longitude"]').value = '';
            document.querySelector('[name="spatial_analysis_final_latitude"]').value = '';
            document.querySelector('[name="spatial_analysis_final_longitude"]').value = '';
        }
    });
}


// Function to scroll to the bottom of the page
function scrollToBottom() {
window.scrollTo({
    top: document.body.scrollHeight,
    behavior: 'smooth'
});
}

// Function to scroll to the top of the page
function scrollToTop() {
window.scrollTo({
    top: 0,
    behavior: 'smooth'
});
}


// Logic for hiding and showing passwords
const passwordInputs = document.querySelectorAll(".password-field input[type='password']");
const toggleButtons = document.querySelectorAll(".password-field i");
toggleButtons.forEach((button, index) => {
button.addEventListener("click", function() {
    const passwordInput = passwordInputs[index];
    if (passwordInput.type === "password") {
    passwordInput.type = "text";
    button.textContent = " Hide Password";
    button.classList.remove("fa-eye")
    button.classList.add("fa-eye-slash")
    } else {
    passwordInput.type = "password";
    button.textContent = " Show Password";
    button.classList.remove("fa-eye-slash")
    button.classList.add("fa-eye")
    }
});
});


// next and continue buttons
let currentTab = 0;
const tabs = document.querySelectorAll('.tabcontent');
const tabLinks = document.querySelectorAll('.tablinks');
document.addEventListener('DOMContentLoaded', () => {
showTab(currentTab);
});

function showTab(n) {
tabs.forEach((tab, index) => {
    tab.style.display = (index === n) ? 'block' : 'none';
});
tabLinks.forEach((tabLink, index) => {
    tabLink.className = tabLink.className.replace(' active', '');
    if (index === n) tabLink.className += ' active';
});
document.querySelector('.btn-back').style.display = (n === 0) ? 'none' : '';
document.querySelector('.btn-continue').style.display = (n === tabs.length - 1) ? 'none' : '';

// Get all elements with the ID 'next-continue-btn'
var continueBtn = document.getElementById('next-continue-btn');

if (currentTab == 0) {
    continueBtn.classList.remove('next-btn');
    continueBtn.classList.add('btn-continue');
} else {
    continueBtn.classList.remove('btn-continue');
    continueBtn.classList.add('next-btn');
}

// Get all elements with the ID 'submit-btn'
var submitBtn = document.getElementById('submitBtn');

if (currentTab == 5) {
    submitBtn.classList.remove('hide');
} else {
    submitBtn.classList.add('hide');
}

// copying form values to the summary page when the user gets to the summary page
if (currentTab == 5) {
    const formFields = [{ id: 'surface_repo_path', summaryId: 'summary4' },
                        { id: 'data_path', summaryId: 'summary5' },
                        { id: 'admin', summaryId: 'summary6' },
                        { id: 'admin_password', summaryId: 'summary7' },
                        { id: 'admin_email', summaryId: 'summary8' },
                        { id: 'map_latitude', summaryId: 'summary9' },
                        { id: 'map_longitude', summaryId: 'summary10' },
                        { id: 'map_zoom', summaryId: 'summary11' },
                        { id: 'spatial_analysis_initial_latitude', summaryId: 'summary12' },
                        { id: 'spatial_analysis_initial_longitude', summaryId: 'summary13' },
                        { id: 'spatial_analysis_final_latitude', summaryId: 'summary14' },
                        { id: 'spatial_analysis_final_longitude', summaryId: 'summary15' }
                    ];

    "{% if form.remote_connect_password %}"
    formFields.push({ id: 'host', summaryId: 'summary1' }, 
                    { id: 'remote_connect_password', summaryId: 'summary2' }, 
                    { id: 'remote_root_password', summaryId: 'summary3' },
                    )
    "{% endif %}"

    formFields.forEach(field => {
    const inputField = document.querySelector(`[name="${field.id}"]`);
    if (inputField) {
        document.getElementById(field.summaryId).value = inputField.value;
    }
    });
}

}

function nextTab() {
if (currentTab < tabs.length - 1) {
    currentTab++;

    if (currentTab == 3){
    showTab(currentTab);
    initializeMap();
    } else if (currentTab == 4) {
    showTab(currentTab);
    initializeSpatialMap();
    } else {
    showTab(currentTab);
    };
}
}

function prevTab() {
if (currentTab > 0) {
    currentTab--;

    if (currentTab == 3){
    showTab(currentTab);
    initializeMap();
    } else if (currentTab == 4) {
    showTab(currentTab);
    initializeSpatialMap();
    } else {
    showTab(currentTab);
    };
}
}