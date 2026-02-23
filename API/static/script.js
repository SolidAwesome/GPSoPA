document.addEventListener("DOMContentLoaded", () => {
    showSection('users'); // default section
});

function showSection(section) {
    const content = document.getElementById("content");
    content.innerHTML = "<p>Loading...</p>";

    switch(section) {
        case 'users':
            fetchUsers();
            break;
        case 'ngos':
            fetchNGOs();
            break;
        case 'centers':
            fetchCenters();
            break;
        case 'events':
            fetchEvents();
            break;
        case 'items':
            fetchItems();
            break;
    }
}

/////////////////////////////////////////////////////
// USERS
/////////////////////////////////////////////////////

function fetchUsers() {
    fetch("/users")
    .then(res => res.json())
    .then(data => {
        const content = document.getElementById("content");

        content.innerHTML = `
            <h2>Users</h2>
            <form id="userForm">
                <input type="text" id="username" placeholder="Username" required>
                <input type="number" id="userrole" placeholder="User Role ID" required>
                <input type="email" id="contact" placeholder="Contact" required>
                <button type="submit">Add User</button>
            </form>
            <ul id="userList"></ul>
        `;

        const list = document.getElementById("userList");

        data.forEach(user => {
            const li = document.createElement("li");
            li.innerHTML = `
                ${user.userid} - ${user.username} (${user.contact})
                <button onclick="editUser(${user.userid}, '${user.username}', ${user.userrole}, '${user.contact}')">Edit</button>
                <button onclick="deleteUser(${user.userid})">Delete</button>
            `;
            list.appendChild(li);
        });

        document.getElementById("userForm").addEventListener("submit", function(e) {
            e.preventDefault();

            const userData = {
                username: document.getElementById("username").value,
                userrole: parseInt(document.getElementById("userrole").value),
                contact: document.getElementById("contact").value
            };

            fetch("/users", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(userData)
            })
            .then(() => showSection('users'));
        });
    })
    .catch(err => console.error("Error fetching users:", err));
}

function editUser(id, username, userrole, contact) {
    const content = document.getElementById("content");

    content.innerHTML = `
        <h2>Edit User</h2>
        <form id="editForm">
            <input type="text" id="username" value="${username}" required>
            <input type="number" id="userrole" value="${userrole}" required>
            <input type="email" id="contact" value="${contact}" required>
            <button type="submit">Save</button>
            <button type="button" onclick="showSection('users')">Cancel</button>
        </form>
    `;

    document.getElementById("editForm").addEventListener("submit", function(e) {
        e.preventDefault();

        const updatedData = {
            username: document.getElementById("username").value,
            userrole: parseInt(document.getElementById("userrole").value),
            contact: document.getElementById("contact").value
        };

        fetch(`/users/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(updatedData)
        })
        .then(() => showSection('users'));
    });
}

function deleteUser(id) {
    fetch(`/users/${id}`, { method: "DELETE" })
    .then(() => showSection('users'));
}

/////////////////////////////////////////////////////
// NGOs
/////////////////////////////////////////////////////

function fetchNGOs() {
    fetch("/ngos")
    .then(res => res.json())
    .then(data => {
        const content = document.getElementById("content");
        content.innerHTML = "<h2>NGOs</h2><ul id='ngoList'></ul>";

        const list = document.getElementById("ngoList");

        data.forEach(ngo => {
            const li = document.createElement("li");
            li.textContent = `${ngo.ngoid} - ${ngo.ngoname} (${ngo.contact})`;
            list.appendChild(li);
        });
    })
    .catch(err => console.error("Error fetching NGOs:", err));
}

/////////////////////////////////////////////////////
// DONATION CENTERS
/////////////////////////////////////////////////////

function fetchCenters() {
    fetch("/donation_centers")
    .then(res => res.json())
    .then(data => {
        const content = document.getElementById("content");

        // Header + Show Map button in flex layout
        content.innerHTML = `
            <div class="centers-header">
                <h2>Donation Centers</h2>
                <button id="loadMapBtn">Show Map</button>
            </div>
            <div id="center-map" style="height:400px; display:none; margin-top:10px;"></div>
            <ul id="centerList" style="margin-top:10px;"></ul>
        `;

        const list = document.getElementById("centerList");

        data.forEach(center => {
            const li = document.createElement("li");
            li.textContent = `${center.centerid} - ${center.centername}, ${center.city}`;
            list.appendChild(li);
        });

        document.getElementById("loadMapBtn").addEventListener("click", loadMap);
    })
    .catch(err => console.error("Error fetching centers:", err));
}

function loadMap() {
    const mapDiv = document.getElementById("center-map");
    mapDiv.style.display = "block";

    if (window.mapInitialized) return;

    fetch("/donation_centers_map")
    .then(res => res.json())
    .then(data => {

        const map = L.map("center-map").setView([0, 0], 2);

        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution: "&copy; OpenStreetMap contributors"
        }).addTo(map);

        const bounds = [];

        data.forEach(center => {
            if (center.lat && center.lng) {
                L.marker([center.lat, center.lng])
                    .addTo(map)
                    .bindPopup(center.centername);

                bounds.push([center.lat, center.lng]);
            }
        });

        if (bounds.length > 0) {
            map.fitBounds(bounds);
        }

        window.mapInitialized = true;
    })
    .catch(err => console.error("Error loading map:", err));
}

/////////////////////////////////////////////////////
// EVENTS
/////////////////////////////////////////////////////

function fetchEvents() {
    fetch("/events")
    .then(res => res.json())
    .then(data => {
        const content = document.getElementById("content");
        content.innerHTML = "<h2>Events</h2><ul id='eventsList'></ul>";

        const list = document.getElementById("eventsList");

        data.forEach(event => {
            const li = document.createElement("li");
            li.textContent = `${event.eventid} - ${event.eventname} | NGO ID: ${event.ngoid} | Start: ${event.startdate} | End: ${event.enddate || '-'}`;
            list.appendChild(li);
        });
    })
    .catch(err => console.error("Error fetching events:", err));
}

/////////////////////////////////////////////////////
// DONATION ITEMS
/////////////////////////////////////////////////////

function fetchItems() {
    fetch("/donation_items")
    .then(res => res.json())
    .then(data => {
        const content = document.getElementById("content");
        content.innerHTML = "<h2>Donation Items</h2><ul id='itemList'></ul>";

        const list = document.getElementById("itemList");

        data.forEach(item => {
            const li = document.createElement("li");
            li.textContent = item;
            list.appendChild(li);
        });
    })
    .catch(err => console.error("Error fetching items:", err));
}