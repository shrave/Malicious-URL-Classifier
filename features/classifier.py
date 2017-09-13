from content import *

def classifier(url):
    raw_features=[]
    raw_features.append(
    (
    content_features_count(url,'iframe'),
    content_features_count(url,'script'),
    redirect_check(url),
    line_count(url),
    hyperlink_count(url),
    content_features_count(url,'html'),
    content_features_count(url,'applet'),
    content_features_count(url,'embed'),
    content_features_count(url,'xml'),
    content_features_count(url,'style'),
    content_features_count(url,'for'),
    content_features_count(url,'meta'),
    content_features_count(url,'img'),
    content_features_count(url,'src'),
    content_features_count(url,'div'),
    content_features_count(url,'object'),
    content_features_count(url,'applet'),
    content_features_attribute_count(url,'meta','refresh'),
    header_response(url),
    script_with_wrong_ext(url),
    page_title_length(url),
    external_javascript_file_count(url),
    char_count(url),
    whitespace_percent(url)
    )
    )
