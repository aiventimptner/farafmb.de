from django.views import generic

from .models import Consultation
from .utils import calc_max_step_size, time_to_seconds, seconds_to_time


class ConsultationsView(generic.TemplateView):
    template_name = 'consultations/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['data'] = {}
        office_hours = Consultation.objects.filter(is_visible=True).all()
        if office_hours:
            time_list = [office_hour.time for office_hour in office_hours]
            seconds = calc_max_step_size(time_list)
            if seconds == 0:
                seconds = 7200
            points = range(
                time_to_seconds(min(time_list)),
                time_to_seconds(max(time_list)) + seconds + seconds,
                seconds,
            )
            for time_ in [seconds_to_time(seconds) for seconds in points]:
                slots = []
                for day, name in Consultation.DAYS:
                    if time_ in time_list:
                        slots.append(office_hours.filter(time=time_, day=day).all())
                    else:
                        slots.append([])
                context['data'][time_] = slots
        context['days'] = Consultation.DAYS
        return context