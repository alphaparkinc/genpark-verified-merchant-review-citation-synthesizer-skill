from client import VerifiedMerchantReviewCitationSynthesizerClient

def main():
    client = VerifiedMerchantReviewCitationSynthesizerClient()
    res = client.synthesize_product_reviews_with_citations('Noise Cancelling Over-Ear Headphones')
    print('Merchant Review Citation Synthesizer: ' + res['review_synthesis_id'])
    print('Sentiment: ' + str(res['consensus_sentiment_score']) + ' | Top Pro: ' + res['pros_highlights'][0])
    print('Citation [1]: ' + res['grounded_citations'][0]['source'] + ' - "' + res['grounded_citations'][0]['quote'] + '"')
    print('Report URL: ' + res['synthesis_report_url'])

if __name__ == '__main__':
    main()
