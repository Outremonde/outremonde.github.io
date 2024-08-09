// Function to set a random background image from Picsum
async function setRandomBackgroundImage() {
    // Set the background image of the clock
    document.querySelector('body').style.backgroundImage = `url(https://picsum.photos/1920/1080/?random)`;
}

function updateClock() {
    const now = new Date();
    let hours = now.getHours();
    const minutes = String(now.getMinutes()).padStart(2, '0');
    //const seconds = String(now.getSeconds()).padStart(2, '0');
    
    // Determine AM or PM
    const meridiem = hours >= 12 ? 'pm' : 'am';
    
    // Convert hours from 24-hour to 12-hour format
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    
    // Format hours to always show two digits
    const hoursString = String(hours) /*.padStart(2, '0')*/;

    // Create time string with meridiem
    const timeString = `${hoursString}:${minutes} ${meridiem}`;
    document.getElementById('clock').textContent = timeString;
}

// Update the clock every second
setInterval(updateClock, 1000);

// Initial call to set the clock immediately on page load
updateClock();

setRandomBackgroundImage();
