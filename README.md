
# Weather App

This Weather App is a Flask-based web application that provides weather forecasts using the OpenWeatherMap API.

## Getting Started

These instructions will guide you through setting up and running the application on your local machine.

### Prerequisites

- Python 3
- pip (Python package manager)
- Access to the terminal or command line interface

### Installation

Follow these steps to get your development environment running:

#### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone git@github.com:Infopercept/python-weather-app.git
cd python-weather-app
```

#### Step 2: Create a Virtual Environment

Create a virtual environment in the project directory:

```bash
# For Unix or MacOS
python3 -m venv venv

# For Windows
python -m venv venv
```

#### Step 3: Activate the Virtual Environment

Activate the virtual environment:

```bash
# For Unix or MacOS
source venv/bin/activate

# For Windows
.\venv\Scripts\activate
```

#### Step 4: Install Dependencies

Install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

#### Step 5: Set Up the Environment Variable

Set up the `OWM_API_KEY` environment variable with your OpenWeatherMap API key:

```bash
# For Unix or MacOS
export OWM_API_KEY='your_api_key_here'

# For Windows
set OWM_API_KEY=your_api_key_here
```

#### Step 6: Run the Application

Run the Flask application:

```bash
python main.py
```

### Accessing the Application

Once the application is running, open your web browser and navigate to `http://localhost:5000` to view the Weather App.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/Infopercept/python-weather-app/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Infopercept/python-weather-app/LICENSE.md) file for details.


## Screenshots (Desktop)
<img src="/screenshots/weather_app_desktop_home_page_screenshot.png">
<img src="/screenshots/weather_app_desktop_forecast_page_screenshot.png">
<img src="/screenshots/weather_app_desktop_error_page_screenshot.png">

## Screenshots (Mobile)
<img src="/screenshots/weather_app_iphone_forecast_page_screenshot.png" style="width:400px;"> <img src="/screenshots/weather_app_iphone_home_page_screenshot.png" style="width:400px;">

## Reflection
Building a Python project from scratch without relying on a tutorial taught me a lot but I was also able to implement the app's key functionality (getting and displaying weather data) due to the work I did with APIs in Angela Yu's Python bootcamp. While deploying this web app, I  learned about git and version control as well as storing API keys as environment variables with .env and the purpose of .gitignore. This project turned out to be frustrating and complicated at times but I learned and grew a lot as a developer by tackling each problem. For instance, I struggled to make this website responsive because I discovered that the Chrome browser tools are not entirely accurate for the mobile view. Hence, when the app was deployed, the website didn't look the way I expected ore desired on mobile. So I switched to a free desktop application called Responsively and it provided views for multiple devices which allowed me to improve my CSS. In addition, I had difficulty positioning my footer at the bottom of my page and had to refer to [this resource](https://stackoverflow.com/questions/51683107/making-a-footer-stay-at-the-bottom-of-the-page-both-in-mobile-view-and-desktop-v) to adjust my CSS accordingly. 

If I were to do this project again, there are a few changes I would make. I would make the website render beautifully on iPads as well by eliminating the space between elements. I also wasn't sure how to add more functionality to this app while maintaining a seamless UI/UX design this time and I would love to do so in the future. E.g. I could add an option for users to specify the country of the city they enter (if multiple countries share the same city name). I could also display the low and high temperatures for each day in the five day forecast instead of only displaying the temperature at noon (which I understand is not an accurate estimate of the overall temperature). It would also be useful to enable location detection to allow the user to get more accurate weather data for their current location by using their precise coordinates instead of relying on the geocoding API provided by OpenWeather.  

## Useful Resources
- [OpenWeather API Documentation](https://openweathermap.org/api/one-call-3)
- [Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [Guide to CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [StackOverflow Post on Centering in CSS Grid](https://stackoverflow.com/questions/45536537/centering-in-css-grid)
- [Youtube video on searching blog posts with Flask](https://www.youtube.com/watch?v=kmtZTo-_gJY)
- [Article on retrieving HTML form data with Flask](https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/)
- [StackOverflow post on building Flask app search bar](https://stackoverflow.com/questions/39960942/flask-app-search-bar)
- [Article on storing API keys as environment variables](https://jonathansoma.com/lede/foundations-2019/classes/apis/keeping-api-keys-secret/)
– [StackOverflow post on storing API keys in Heroku](https://stackoverflow.com/questions/71593743/storing-api-key-in-heroku)
- [Making a footer stay at the bottom of the page both in mobile view and desktop view](https://stackoverflow.com/questions/51683107/making-a-footer-stay-at-the-bottom-of-the-page-both-in-mobile-view-and-desktop-v)

## Image Credit
- [Home page background image](https://unsplash.com/photos/2KXEb_8G5vo)
- [Error page desktop background image](https://unsplash.com/photos/U-Kty6HxcQc)

### Icons 
- <a target="_blank" href="https://icons8.com/icon/pLiaaoa41R9n/wind">Wind</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/37802/thermometer">Thermometer</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/99328/clouds">Clouds</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/101829/rain">Rain</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/67657/fog">Fog</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/hXkspV0LTEoE/snow">Snow</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/G3xS4dQTvswX/rainy-weather">Rainy Weather</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/101843/storm">Storm</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/59878/search">Search</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/39789/chevron-left">Chevron Left</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/99362/summer">Summer</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
- <a target="_blank" href="https://icons8.com/icon/akbaie9da2Be/tornado">Tornado</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
