class VerifiedMerchantReviewCitationSynthesizerClient:
    def synthesize_product_reviews_with_citations(self, product_query='Ergonomic Mesh Office Chair with Lumbar Support', min_verified_reviews_count=200):
        return {
            'review_synthesis_id': 'rev_cit_5519',
            'product_query': product_query,
            'consensus_sentiment_score': 0.88,
            'pros_highlights': ['Excellent 4D adjustable armrests', 'Breathable Korean mesh fabric prevents heat buildup'],
            'cons_drawbacks': ['Headrest adjustment requires significant force initially'],
            'grounded_citations': [
                {'source': 'Wirecutter Teardown 2026', 'quote': 'Top value under $400 for 8+ hour posture support.', 'url': 'https://reviews.trusted.com/chair-01'},
                {'source': 'Reddit r/OfficeChairs Consensus', 'quote': 'Cushioning holds up after 18 months of daily use.', 'url': 'https://reddit.com/r/OfficeChairs'}
            ],
            'synthesis_report_url': 'https://reviews.synthesis.genpark.ai/reports/5519.json'
        }
