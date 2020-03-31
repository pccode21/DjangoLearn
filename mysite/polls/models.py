from django.db import models
from django.utils import timezone
import datetime
from django_matplotlib.fields import MatplotlibFigureField


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class FigureModel(models.Model):
    # Plot piecewise line
    line_plot = MatplotlibFigureField(figure='plot_line',
                                      verbose_name='Line', silent=True)
    # Plot sine function
    sine_plot = MatplotlibFigureField(figure='plot_sine',
                                      verbose_name='Sine', silent=True)
    # Imshow demo
    imshow_demo = MatplotlibFigureField(figure='image_plot',
                                        verbose_name='Imshow demo', silent=True)

    # Pass arguments to plot
    with_args = MatplotlibFigureField(figure='plot_with_args',
                                      verbose_name="Args passed", silent=True,
                                      plt_args=([1, 4, 2], [5, 2, 1]),
                                      help_text="Arguments are passed to the plot "
                                      "using `plt_args` keyword."
                                    )
    # Countour plot as svg
    countour_plot = MatplotlibFigureField(figure='countour_plot',
                                    verbose_name="Contour plot", silent=True,
                                    plt_kwargs={"custom_title":
                                                "Custom figure title goes here..."
                                                }
                                    )
