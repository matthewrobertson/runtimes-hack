# runtimes-hack

## Deploy the function

```
gcloud functions deploy pyfunc \
  --runtime=python39 \
  --project=jscma-gcf-test \
  --trigger-http \
  --allow-unauthenticated \
  --region=us-central1
```

## Deploy the actions

Install the [actions CLI](https://developers.google.com/assistant/df-asdk/actions-sdk/gactions-cli).

```
gactions update --action_package actions.json --project jscma-fun
```

## Run the unit tests

```bash
python3 -m unittest conversation_test
```