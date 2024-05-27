# StockFlix

StockFlix is a web application that allows users to search for stock information, view detailed company profiles, and maintain a wishlist of their favorite stocks. The application is built using Flask, integrates with the Finnhub API for stock data, and offers a user-friendly interface inspired by Netflix.

## Features

- **Search Stocks:** Search for stocks by their symbol and view current price and other details.
- **Stock Details:** View detailed information about a selected stock, including company profile and recent news.
- **Wishlist:** Add stocks to your wishlist and manage them easily.
- **Pagination:** Navigate through stock listings with pagination for a better user experience.
- **Caching:** Utilizes Flask-Caching to cache stock list data for improved performance.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Flask
- Finnhub Python Client
- Flask-Paginate
- Flask-Caching
- Bootstrap (for frontend styling)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/stockflix.git
    cd stockflix
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Finnhub API key:
    - Sign up on [Finnhub](https://finnhub.io/) to get an API key.
    - Replace the `API_KEY` in the `app.py` file with your Finnhub API key.

### Running the Application

1. Run the Flask application:
    ```bash
    flask run
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

## File Structure

- `app.py`: The main Flask application file.
- `templates/`: Directory containing HTML templates.
  - `index.html`: Home page template.
  - `detail.html`: Stock details page template.
  - `wishlist.html`: Wishlist page template.
- `static/`: Directory containing static files (CSS, JS).
  - `style.css`: Custom styles for the application.

## Usage

- **Home Page:** View a list of stocks and search for specific stocks by their symbol.
- **Stock Details:** Click on the "View Details" button to see detailed information about a stock.
- **Wishlist:** Add stocks to your wishlist by clicking "Add to Wishlist". View and manage your wishlist by clicking on the "View Wishlist" button. Remove stocks from the wishlist using the "Remove from Wishlist" button.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Finnhub](https://finnhub.io/) for providing the stock market data API.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Bootstrap](https://getbootstrap.com/) for the frontend styling.

