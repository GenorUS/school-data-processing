import requests


class Slack:
    def __init__(self, webhook, channel=None):
        self.webhook = webhook
        self.channel = channel

    def to_dict(self):
        val = {
            'webhook': self.webhook,
            'channel': self.channel
        }

        return val

    def to_string(self):
        val = "webhook: {}\nchannel: {}".format(self.webhook, self.channel)

        return val

    def message(self, message, channel_override=None):
        payload = {
            'text': message,
        }

        if channel_override:
            payload['channel'] = channel_override
        elif self.channel:
            payload['channel'] = self.channel

        try:
            response = requests.post(self.webhook, json=payload)
        except:
            if response.status_code != 200:
                raise ValueError(
                    'Request to slack returned an error {}, the response is:{}'.format(response.status_code,
                                                                                       response.text)
                )

    def __repr__(self):
        return self.to_string()
