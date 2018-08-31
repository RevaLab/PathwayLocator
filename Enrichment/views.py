import json

import scipy.stats as stats

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
# Create your views here.


@csrf_exempt
def index(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        query_list = set(data['genes'])
    else:
        data = {}
        query_list = set()

    enrichment_results = {}

    db_all = settings.KEGG['all']
    bg = db_all.union(query_list)

    for pw in settings.KEGG['dict']:
        pathway = settings.KEGG['dict'][pw]['genes']
        pvalue = find_p_val(pathway, query_list, bg)
        if pvalue < 0.01 and len(settings.KEGG['dict'][pw]['locations']):
            enrichment_results[pw] = {
                'pval': pvalue,
                'locations': list(settings.KEGG['dict'][pw]['locations'])
            }

    return JsonResponse(enrichment_results)


def find_p_val(pathway, query_list, bg):

    overlap = len(pathway.intersection(query_list))

    if not overlap:
        return 1.0

    pathway_len = len(pathway)
    query_list_len = len(query_list)
    bg_len = len(bg)

    pathway_only = pathway_len - overlap
    query_list_only = query_list_len - overlap
    bg_only = bg_len - pathway_len - query_list_len + overlap

    try:
        odds_ratio, pvalue = stats.fisher_exact(
            [
                [overlap, pathway_only],
                [query_list_only, bg_only]
            ],
            alternative='greater'
        )
        return pvalue
    except ValueError:
        print('Something is wrong with this 2x2 table: \n')
        print([overlap, pathway_only], [query_list_only, bg_only])
        return 'NaN'
