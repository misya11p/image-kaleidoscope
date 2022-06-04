import os
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import kaleidoscopes

def write_image(filepath, output_dir):
    for kal in [att for att in dir(kaleidoscopes) if 'kal_' in att]:
        plt.figure(figsize=(5, 5))
        exec(f'kaleidoscopes.{kal}("{filepath}")')
        plt.grid(False)
        plt.tick_params(length=0)
        plt.xticks(color="None")
        plt.yticks(color="None")
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)
        plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
        plt.savefig(os.path.join(output_dir, kal + '.png'))