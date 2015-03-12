$( document ).ready(function() {
    $("select").each( function() {
        var lang = $(this).data('lang');
        var lang_code = $(this).data('lang-code');
        $(this).select2({
            tags: true,
            tokenSeparators: [';'],
            minimumInputLength: 1,
            placeholder: lang + ' words',
            ajax: {
                delay: 250,
                url: '/ajax/words.json?l=' + lang_code,
                data: function (params) {
                    return {q: params.term}
                },
                processResults: function (data) {
                    return {results: data};
                }
            }
        });
    });
});
