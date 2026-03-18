import facebook_business
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi

def analyze_meta_ads(access_token, ad_account_id):
    """
    Skill for Manus to pull and analyze Meta Ads insights.
    """
    try:
        FacebookAdsApi.init(access_token=access_token)
        account = AdAccount(f'act_{ad_account_id}')
        
        # سحب بيانات الأداء لآخر 7 أيام
        fields = ['campaign_name', 'spend', 'impressions', 'inline_link_clicks', 'conversions']
        params = {'date_preset': 'last_7d'}
        
        insights = account.get_insights(fields=fields, params=params)
        return insights
    except Exception as e:
        return f"Error connecting to Meta API: {str(e)}"
