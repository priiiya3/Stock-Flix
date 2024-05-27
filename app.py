from flask import Flask, flash, render_template, request, redirect, url_for
import finnhub
from flask_paginate import Pagination, get_page_parameter
from flask_caching import Cache

app = Flask(__name__)
app.secret_key = 'cp9k8ihr01qid795km8g'

# Setup Finnhub client
API_KEY = 'cp9k8ihr01qid795km70cp9k8ihr01qid795km7g'
finnhub_client = finnhub.Client(api_key=API_KEY)

# Configure Flask-Caching
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Wishlist to store stock symbols
wishlist = []

# Cache decorator for fetching stock list
@cache.cached(timeout=300, key_prefix='stock_list')
def fetch_stock_list():
    try:
        stock_list = finnhub_client.stock_symbols('US')
        return stock_list
    except finnhub.exceptions.FinnhubAPIException as e:
        flash(f"API error: {e}", "danger")
        return []

# Fetch stock data by symbol
def fetch_stock_data(symbol):
    try:
        return finnhub_client.quote(symbol)
    except finnhub.exceptions.FinnhubAPIException as e:
        flash(f"API error: {e}", "danger")
        return None

# Fetch company profile by symbol
def fetch_company_profile(symbol):
    try:
        profile = finnhub_client.company_profile2(symbol=symbol)
        # print(profile)
        if 'name' in profile:
            # print(profile, "herehee")
            return profile
        else:
            flash(f"Company name not found for symbol {symbol}", "warning")
            return None
    except finnhub.exceptions.FinnhubAPIException as e:
        flash(f"API error: {e}", "danger")
        return None

# Fetch stock news by symbol
def fetch_stock_news(symbol):
    try:
        return finnhub_client.company_news(symbol, _from="2023-01-01", to="2023-12-31")
    except finnhub.exceptions.FinnhubAPIException as e:
        flash(f"API error: {e}", "danger")
        return []


# Home Page
@app.route('/')
def index():
    query = request.args.get('symbol')
    if query:
        stock_data = fetch_stock_data(query)
        if stock_data:
            stocks = [{'symbol': query, 'name': 'Searched Stock', 'current_price': stock_data['c']}]
        else:
            stocks = []
    else:
        stocks = fetch_stock_list()
    
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10
    total = len(stocks)
    stocks_paginated = stocks[(page - 1) * per_page: page * per_page]
    
    stock_data_list = []
    for stock in stocks_paginated:
        # Fetch company profile to get company name
        company_profile = fetch_company_profile(stock['symbol'])
        if company_profile and 'name' in company_profile:
            company_name = company_profile['name']
        else:
            company_name = 'Unknown'
        
        stock_data = fetch_stock_data(stock['symbol'])
        if stock_data:
            stock_info = {
                'symbol': stock['symbol'],
                'name': company_name,  # Use the fetched company name
                'current_price': stock_data['c']
            }
            stock_data_list.append(stock_info)

    pagination = Pagination(page=page, total=total, per_page=per_page, record_name='stocks')
    return render_template('index.html', stocks=stock_data_list, pagination=pagination, query=query)


# Detail page route
@app.route('/detail/<symbol>')
def detail(symbol):
    stock_data = fetch_stock_data(symbol)
    company_profile = fetch_company_profile(symbol)
    stock_news = fetch_stock_news(symbol)
    if not stock_data or not company_profile:
        return redirect(url_for('index'))
    return render_template('detail.html', stock_data=stock_data, company_profile=company_profile, stock_news=stock_news)

# Wishlist page route
@app.route('/wishlist')
def view_wishlist():
    wishlist_data = [fetch_company_profile(stock) for stock in wishlist]
    # print(wishlist_data)
    return render_template('wishlist.html', wishlist=wishlist_data)

# Add to wishlist route
@app.route('/add_to_wishlist/<symbol>')
def add_to_wishlist(symbol):
    if symbol not in wishlist:
        wishlist.append(symbol)
    return redirect(url_for('view_wishlist'))

# Remove from wishlist route
@app.route('/remove_from_wishlist/<ticker>')
def remove_from_wishlist(ticker):
    # print("inside fucntion")
    if ticker in wishlist:
        wishlist.remove(ticker)
        flash(f"{ticker} removed from wishlist", "success")
    else:
        flash(f"{ticker} not found in wishlist", "danger")
    # print("RETURNING")
    return redirect(url_for('view_wishlist'))



if __name__ == '__main__':
    app.run(debug=True)
