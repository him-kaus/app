(function ($) {
    $(document).ready(function () {

        DateTimeShortcuts.clockHours.default_ = [];

        for (let hour = 8; hour <= 20; hour++) {
            let verbose_name = new Date(1970, 1, 1, hour, 0, 0).strftime('%H:%M');
            DateTimeShortcuts.clockHours.default_.push([verbose_name, hour])
        }

    });
})(django.jQuery);
