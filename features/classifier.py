from content import content_features_count,char_count,redirect_check,header_response,\
hyperlink_count,external_javascript_file_count,page_title_length,script_with_wrong_ext, \
content_features_attribute_count,whitespace_percent
#Include a vector for any new xml tag.
def classifier(url):
    raw_features=[]
    raw_features.append(
    (
    redirect_check(url),
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
