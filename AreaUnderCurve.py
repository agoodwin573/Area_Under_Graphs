import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
#from docx import Document
#from docx.shared import Cm
#from docx.shared import Inches
#from io import BytesIO
import random
from statistics import NormalDist

def add_figure_to_docx(fig):
    """
    Copies the given Matplotlib figure to the Windows clipboard as an image.
    """
    global document
    # Adjust layout to reduce whitespace
    fig.tight_layout()

    # Save to a buffer with bbox_inches='tight'
    #memfile = BytesIO()
    #fig.savefig(memfile, format='pdf',) #bbox_inches='tight', pad_inches=0)
    #document.add_picture(memfile, height=Inches(2))
    #memfile.close()
    
def plot_shaded_area(func, x_min, x_max, func_label="f(x)", num_points=1000):
    global Solutions, counter
    # Extend the plot range by 10% on each side
    range_extension = 0.1 * (x_max - x_min)
    x_plot = np.linspace(x_min - range_extension, x_max + range_extension, num_points)
    x_fill = np.linspace(x_min, x_max, num_points)

    y_plot = func(x_plot)
    y_fill = func(x_fill)

    # Compute the definite integral (area under the curve)
    area, _ = quad(func, x_min, x_max)
    Solutions.append([func_label, area])
    # Plot setup
    fig, ax = plt.subplots()
    ax.plot(x_plot, y_plot, label=rf"$f(x) = {func_label}$", color = 'black')
    ax.fill_between(x_fill, y_fill, alpha=0.3, color='skyblue', label='Shaded Area')

    # Axes at origin
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Arrows
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    # Ticks
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xticks([x for x in ax.get_xticks() if not np.isclose(x, 0)])
    ax.set_yticks([y for y in ax.get_yticks() if not np.isclose(y, 0)])

    # Integral annotation
    #text_x = (x_min + x_max) / 2
    #text_y = max(y_fill) * 0.6 if max(y_fill) != 0 else 1
    #integral_label = rf"$\int_{{{x_min}}}^{{{x_max}}} {func_label}\,dx \approx {area:.4f}$"
    #ax.text(text_x, text_y, integral_label, ha='center', fontsize=11,
    #        bbox=dict(boxstyle="round", facecolor="white", alpha=0.6))

    # Title
    ax.set_title(rf"Area Under ${func_label}$ between $x={x_min}$ and $x={x_max}$ ", fontsize=11)

    ax.grid(True, which='both', linestyle='--', alpha=0.3)
    ax.legend()
    fig = plt.gcf()
    fig.tight_layout()
    fig.savefig("Graphs\_"+rf"{counter}.svg")
    counter+=1
    #plt.show()
    #add_figure_to_docx(fig)
    plt.clf()
    plt.close()

counter = 0
#Create Document
#document = Document()
Solutions = []
# -------- LINEAR FUNCTIONS --------
plot_shaded_area(lambda x: 2*x + 1, 1, 5, func_label="2x + 1")
plot_shaded_area(lambda x: -x + 4, -5, 3, func_label="-x + 4")
plot_shaded_area(lambda x: 0.5*x - 2, 3, 7, func_label="\\frac{1}{2}x - 2")
plot_shaded_area(lambda x: 3*x+5, 2, 12, func_label="3x+5")
plot_shaded_area(lambda x: x, 0, 10, func_label="x")

# -------- QUADRATIC FUNCTIONS --------
plot_shaded_area(lambda x: x**2, -2, 2, func_label="x^2")
plot_shaded_area(lambda x: x**2 + 4, -3, 3, func_label="x^2 + 4")
plot_shaded_area(lambda x: x**2 + 2, 2, 5, func_label="x^2 + 2")
plot_shaded_area(lambda x: 2*x**2 + x + 1, -2, 1, func_label="2x^2 + x + 1")
plot_shaded_area(lambda x: 0.5*x**2, -4, 4, func_label="\\frac{1}{2}x^2")

# -------- CUBIC FUNCTIONS --------
plot_shaded_area(lambda x: x**3, 2, 5, func_label="x^3")
plot_shaded_area(lambda x: x**3 + 3*x**2, -1, 3, func_label="x^3 - 3x^2")
plot_shaded_area(lambda x: -x**3 + 2*x, -5, -2, func_label="-x^3 + 2x")
plot_shaded_area(lambda x: 0.5*x**3 + x**2 - x, 2, 3, func_label="\\frac{1}{2}x^3 + x^2 - x")
plot_shaded_area(lambda x: 2*x**3 - x**2 + 3, -1, 3, func_label="2x^3 - x^2 + 3")

# -------- EXPONENTIAL FUNCTIONS --------
plot_shaded_area(lambda x: np.exp(x), 0, 2, func_label="e^x")
plot_shaded_area(lambda x: np.exp(-x), 0, 3, func_label="e^{-x}")
plot_shaded_area(lambda x: 2**x, -2, 2, func_label="2^x")
plot_shaded_area(lambda x: 0.5**x, -2, 2, func_label="\\left(\\frac{1}{2}\\right)^x")
plot_shaded_area(lambda x: np.exp(x) - 1, 0, 2, func_label="e^x - 1")
plot_shaded_area(lambda x: np.exp(2*x), -1, 1, func_label="e^{2x}")

# -------- LOGARITHMIC FUNCTIONS --------
plot_shaded_area(lambda x: np.log(x), 3, 7, func_label="\\ln(x)")
plot_shaded_area(lambda x: np.log(x+3), 0.5, 4, func_label="\\ln(x+3)")
plot_shaded_area(lambda x: np.log(x)+5, 3, 10, func_label="\\ln(x)+5")
plot_shaded_area(lambda x: np.log(3*x + 1), 1, 4, func_label="\\ln(3x + 1)")
#plot_shaded_area(lambda x: 3*np.log(x), 5, 14, func_label="3\\ln(x)}")
plot_shaded_area(lambda x: np.log(x**2 + 1), -2, 2, func_label="\\ln(x^2 + 1)")

# -------- TRIGONOMETRIC FUNCTIONS --------
plot_shaded_area(lambda x: np.sin(x), 0, np.pi, func_label="\\sin(x)")
plot_shaded_area(lambda x: np.cos(x), 0, np.pi, func_label="\\cos(x)")
plot_shaded_area(lambda x: np.sin(2*x), 0, np.pi, func_label="\\sin(2x)")
plot_shaded_area(lambda x: np.cos(x) + 1, 0, 2*np.pi, func_label="\\cos(x) + 1")
plot_shaded_area(lambda x: np.sin(x)**2, 0, np.pi, func_label="\\sin^2(x)")
plot_shaded_area(lambda x: np.sin(x) * np.cos(x), 0, np.pi, func_label="\\sin(x)\\cos(x)")
plot_shaded_area(lambda x: np.tan(x), -np.pi/4, np.pi/4, func_label="\\tan(x)")
plot_shaded_area(lambda x: np.abs(np.sin(x)), 0, 2*np.pi, func_label="|\\sin(x)|")

#document.add_page_break()
#document.add_heading("SOLUTIONS")
for line in Solutions:
    print("The area under the curve"+rf" {line[0]} "+ "is " + str(round(line[1],3)))#, style='List Number')


#document.save("AreaUnderCurvesQuestions.docx")