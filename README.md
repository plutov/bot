Do not use in Production!

### MySQL Slack Client Bot

`mysql-bot` makes it possible to connect to MySQL databases accessible from server on which Bot is running. It has similar interface to Unix's `mysql-client`.

It's secure, Bot doesn't store any queries and data.

### Run it with Docker

Get Slack API Token first.

```
docker build -t mysql-bot .
docker run -e SLACK_TOKEN=<token> mysql-bot
```

### How it works

```
mysql 
```