from content import *
from lexical import *
from link import *
from network import *
from dnsresponse import *
from javascript import *

#Input URLs wont have http/https specification at the begining. Except at one function.
def classifier(url):
    raw_features=[]
    raw_features.append(
#Content features tuple.
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
    max_min_avg_file_extensions(url),
    suspicious_content_tag(url),
    source_in_other_domain(url),
    double_documents(url),
    same_different_origin_count(url),
    script_with_wrong_ext(url),
    page_title_length(url),
    external_javascript_file_count(url),
    char_count(url),
    whitespace_percent(url)
    ),
    #Lexical features tuple.
    (
    url_length(url),
    special_chars(url),
    ratio_special_chars(url),
    path_length(url),
    digit_count(url),
    alphabet_count(url),
    scheme_http_or_not(url),
    Presence_of_IP(url),
    domain_token_count(url),
    longest_domain_token_count(url),
    longest_token_path(url),
    hostname_unicode(url),
    countdots(url),
    blacklisted_word_present(url),
    hyphens_instead_dots_domain(url),
    another_char_hostname(url),
    directory_length(url),
    sub_directory_tokens_count(url),
    sub_directory_special_count(url),
    argument_length(url),
    query_variables_count(url),
    max_length_variable(url),
    subdomain_length(url),
    count_at_symbol(url),
    suspicious_word_count(url),
    filename_length(url),
    port_number(url)
    ),
    #Link features tuple.
    (
    sitepopularity(url),
    pagespeed_rank(url),
    time(url)
    ),
    #Network features tuple.
    (
    redirect_count_total(url),
    start_end_cert(url),
    TLD_presence(url),
    subdomain_presence(url),
    host_components_count(url)
    ),
    #DNS Response features.
    (
    resolved_ip_count(url),
    nameserver_count(url),
    #Dont put http at the beginning of URL.
    location(url),
    WhoIS(url),
    DNS_response(url),
    mailserver_IP(url),
    reverse_IP(url),
    nameserver_IP(url),
    PTR(url),
    PTR_A_record(url),
    same_ip(url)
    ),
    #Javascript features.
    (
    eval_count(url),
    setTimeout_count(url),
    setInterval_count(url),
    entropy_of_strings(url),
    long_variables_functions(url),
    fingerprint_function(url),
    suspicious_strings_functions(url),
    dom_modification(url),
    average_length_string(url),
    whitespace_script(url),
    length_of_strings(url),
    string_with_iframe(url),
    script_in_chars(url),
    obfuscation_functions(url),
    event_trigger_functions(url),
    one_line_code(url)
    )
    )

classifier("www.google.com")
