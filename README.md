# Bitcoin Status API

This is a simple API that returns many informations about Bitcoin.

This API is hosted on Render and you can access it [here](https://bitcoin-status-api.onrender.com/)
(⚠️ **This may take a few seconds to load because the server may be sleeping**).

This API is the first step of a project that I'm working on, which is a iOS application that shows informations about Bitcoin exlusively.

## Tech Stack

- FastAPI
- Python
- Render

## Endpoints

### GET /crypto-price

This endpoint returns the current price of any cryptocurrency in any currency.

#### Query Parameters

- `crypto`: The cryptocurrency you want to get the price. Default is `bitcoin`.

- `currency`: The currency you want to get the price. Default is `usd`.

#### Example

```bash
curl https://bitcoin-status-api.onrender.com/crypto-price?crypto=bitcoin&currency=usd
```

### GET /crypto-market-chart

Get historical market data include price, market cap, and 24h volume

1 day from current time = 5 minute interval data
2 - 90 days from current time = hourly data
above 90 days from current time = daily data (00:00 UTC)
max days = since 2011

Cache based on days range:

1 day = 30 seconds cache
2-90 days = 30 minutes cache
90 days = 12 hours cache

Anything above 365 days will return max days data (since 2011) only for Btc/Usd.

#### Query Parameters

- `crypto`: The cryptocurrency you want to get the market chart. Default is `bitcoin`.

- `currency`: The currency you want to get the market chart. Default is `usd`.

- `days`: The number of days you want to get the market chart. Default is `1`.

#### Example

```bash
curl https://bitcoin-status-api.onrender.com/crypto-market-chart?crypto=bitcoin&currency=usd&days=10
```

### GET /crypto-market-cap

COMING SOON

### GET /fng

This endpoint returns the current Fear and Greed Index. You can also get the historical data.

The fear and greed index is an index that shows the current sentiment of the market. It goes from 0 to 100, where 0 is extreme fear and 100 is extreme greed.

The first value returned in the array is the most recent value.

#### Query Parameters

- `days`: The number of days you want to get the historical data. Default is `1`.

#### Example

```bash
curl https://bitcoin-status-api.onrender.com/fng?days=10
```

### GET /cbbi

This endpoint returns the current Crypto and Bitcoin Bull Market Index. You can also get the historical data.

The Crypto and Bitcoin Bull Market Index is an index that shows the current sentiment of the market. It goes from 0 to 100, where 0 is supposed to be the bottom of the bear market and 100 is supposed to be the top of the bull market.

The first value returned in the array is the most recent value.

As the request fetch a lot of data, it may take a few seconds to load, this data is also stored in cache.

#### Query Parameters

- `days`: The number of days you want to get the historical data. Default is `1`.

#### Example

```bash
curl https://bitcoin-status-api.onrender.com/cbbi?days=10
```

### GET /upcomming-events

This endpoint returns the upcomming economic events that may affect the price of Bitcoin.

The data is fetched from [Forexfactory](https://www.forexfactory.com/).

#### Query Parameters

- `currencies`: The currencies you want to get the events. Default is `usd`. You can pass multiple currencies separated by commas.

- `only_high_impact`: If you want to get only the high impact events. Default is `false`.

```bash
curl https://bitcoin-status-api.onrender.com/upcomming-events?currencies=usd,eur&only_high_impact=true

```

### GET /news

This endpoint returns the latest news about Bitcoin. It use a RSS feed from [CoinTelegraph](https://cointelegraph.com).

#### Example

```bash
curl https://bitcoin-status-api.onrender.com/news
```

