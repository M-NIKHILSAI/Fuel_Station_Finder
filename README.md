# ⛽ Smart Fuel Station Finder

A location-based web application that helps users find nearby fuel stations with interactive maps, distance calculation, and filtering features.

---

## 🚀 Features

* 📍 Detects user location using browser geolocation
* 🗺️ Displays nearby fuel stations using Google Maps API
* 📏 Calculates distance between user and stations
* ⛽ Shows fuel prices and station details (mock data)
* 🔍 Filter and sort stations based on distance or price
* 📱 Responsive and user-friendly interface

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **API:** Google Maps JavaScript API
* **Database (Optional):** SQLite

---

## 📂 Project Structure

```
FuelFinder/
│── app.py
│── templates/
│   └── index.html
│── static/
│   ├── style.css
│   └── script.js
│── database.db (optional)
│── README.md
```

---

## ⚙️ Setup Instructions

1. Clone the repository:

```
git clone https://github.com/your-username/FuelFinder.git
cd FuelFinder
```

2. Install dependencies:

```
pip install flask
```

3. Add your Google Maps API key in the HTML file:

```
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>
```

4. Run the application:

```
python app.py
```

5. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📊 How It Works

* The app detects the user's location or accepts manual input
* Fetches nearby fuel stations (mock/API data)
* Displays results on an interactive map
* Calculates distances and shows station details

---

## 🔮 Future Improvements

* User login & saved favorite stations
* Real-time fuel price integration
* Route navigation to selected station
* Mobile app version

---

## 🤝 Contribution

Feel free to fork this repository and submit pull requests.

---

## 👨‍💻 Author

**M NIKHIL SAI**
Computer Science Engineering Student
