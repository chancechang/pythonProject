function last_page() {
    if (page != 1) {
        page = page - 1;
    }
    get_proxy_ip(page, 15, 'last');
}

function next_page() {
    page = page + 1;
    get_proxy_ip(page, 15, 'next');
}

function decode_str(scHZjLUh1) {
    scHZjLUh1 = Base64["\x64\x65\x63\x6f\x64\x65"](scHZjLUh1);
    key = '\x6e\x79\x6c\x6f\x6e\x65\x72';
    len = key["\x6c\x65\x6e\x67\x74\x68"];
    code = '';
    for (i = 0; i < scHZjLUh1["\x6c\x65\x6e\x67\x74\x68"]; i++) {
        var coeFYlqUm2 = i % len;
        code += window["\x53\x74\x72\x69\x6e\x67"]["\x66\x72\x6f\x6d\x43\x68\x61\x72\x43\x6f\x64\x65"](scHZjLUh1["\x63\x68\x61\x72\x43\x6f\x64\x65\x41\x74"](i) ^ key["\x63\x68\x61\x72\x43\x6f\x64\x65\x41\x74"](coeFYlqUm2))
    }
    return Base64["\x64\x65\x63\x6f\x64\x65"](code)
}

function str_to_json(str) {
    return (new Function("return " + str))();
}

function get_proxy_ip(page, num, click_btn) {
    var timestamp = Date.parse(new Date());
    timestamp = timestamp / 1000;
    var token = md5(String(page) + String(num) + String(timestamp));
    $.get('../proxy?page=' + page + '&num=' + num + '&token=' + token + '&t=' + timestamp, function(result) {
        if (result.status === 'true') {
            var setHtml = "";
            $("#ip-list").html(setHtml);
            var encode_str = result.list;
            var items = str_to_json(decode_str(encode_str));
            for (var index = 0; index < items.length; ++index) {
                item = items[index];
                setHtml += "<tr>\n<td>" + (index + 1) + "</td>\n";
                setHtml += "<td>" + item.ip.toString() + "</td>\n";
                setHtml += "<td>" + item.port.toString() + "</td>\n";
                setHtml += "<td>" + item.time.toString() + "</td>\n</tr>\n";
            }
            $("#ip-list").html(setHtml);
            if (click_btn === 'next') {
                document.getElementById("last-page").disabled = false;
                if (items.length < 15) {
                    document.getElementById("next-page").disabled = true;
                }
            } else {
                document.getElementById("next-page").disabled = false;
                if (page === 1) {
                    document.getElementById("last-page").disabled = true;
                }
            }

        }
    });
}

function refresh_page() {
    history.go(0);
}

var page = 1;
last_page();
setInterval(refresh_page, 20000);