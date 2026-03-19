import facebook_business
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi

def analyze_meta_ads(access_token, ad_account_id):
    FacebookAdsApi.init(access_token=access_token)
    account = AdAccount(f'act_{ad_account_id}')
    fields = ['campaign_name', 'spend', 'impressions', 'inline_link_clicks']
    params = {'date_preset': 'last_7d'}
    insights = account.get_insights(fields=fields, params=params)
    return list(insights)
