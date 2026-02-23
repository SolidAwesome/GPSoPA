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
        case 'status':
            fetchStatuses();
            break;
        case 'items':
            fetchItems();
            break;
    }
}

// --- USERS ---
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
                <button onclick="deleteUser(${user.userid})">Delete</button>
            `;
            list.appendChild(li);
        });

        // Handle form submit
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
            .then(res => res.json())
            .then(() => showSection('users'));
        });
    });
}

function deleteUser(id) {
    fetch(`/users/${id}`, { method: "DELETE" })
    .then(() => showSection('users'));
}

// --- NGOs ---
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
    });
}

// --- Donation Centers ---
function fetchCenters() {
    fetch("/donation_centers")
    .then(res => res.json())
    .then(data => {
        const content = document.getElementById("content");
        content.innerHTML = "<h2>Donation Centers</h2><ul id='centerList'></ul>";
        const list = document.getElementById("centerList");
        data.forEach(center => {
            const li = document.createElement("li");
            li.textContent = `${center.centerid} - ${center.centername}, ${center.city}`;
            list.appendChild(li);
        });
    });
}

// --- Donation Status ---
function fetchStatuses() {
    fetch("/donation_status")
    .then(res => res.json())
    .then(data => {
        const content = document.getElementById("content");
        content.innerHTML = "<h2>Donation Status</h2><ul id='statusList'></ul>";
        const list = document.getElementById("statusList");
        data.forEach(s => {
            const li = document.createElement("li");
            li.textContent = s;
            list.appendChild(li);
        });
    });
}

// --- Donation Items ---
function fetchItems() {
    fetch("/donation_items")
    .then(res => res.json())
    .then(data => {
        const content = document.getElementById("content");
        content.innerHTML = "<h2>Donation Items</h2><ul id='itemList'></ul>";
        const list = document.getElementById("itemList");
        data.forEach(i => {
            const li = document.createElement("li");
            li.textContent = i;
            list.appendChild(li);
        });
    });
}