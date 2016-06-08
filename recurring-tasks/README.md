# OVerview

Create Trello cards on a weekly or monthly basis.

The cards will be in a specific list on a specific board.

# Config

Example Configuration `config.yaml`:

```
monthly:
  '1':
  - plan finances for the month
trello:
  api-key: API-KEY-HERE
  api-secret: API-SECRET-HERE
  board: qs9sZTxs
  list: 5624e269b8a14c9076961c7d
  token: TOKEN-HERE
  token-secret: TOKEN-SECRET_HERE
weekly:
  monday:
  - task
  thursday:
  - take out trash
```

## trello

The `trello` section defines API keys and which board and list to use.

If you don't know the board or list IDs, you can run the script in debug
(`./recurring-tasks -d`) and it will print a list of IDs for the boards or
lists.

## monthly

Using weekday names, specify a list of tasks to perform on each day

## monthly

Using the day of the month (integer), specify a list of tasks to perform
on that day.

# Usage

To run this as a daily cron job:

```
0 6 * * * cd /home/matt/scripts/recurring-tasks;./recurring-tasks -c personal.yaml
```
