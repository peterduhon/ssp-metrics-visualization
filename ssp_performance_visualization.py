import matplotlib.pyplot as plt
import numpy as np

# Updated Sample Data with 5 SSPs and fictional names
ssp_ids = ['AdStream', 'BidMax', 'ClearAds', 'DigiServe', 'EcoBid']
win_rates = [0.75, 0.50, 0.65, 0.55, 0.70]
avg_bids = [5.2, 4.8, 6.1, 5.5, 6.3]
total_impressions = [1000, 800, 1200, 900, 1100]

x = np.arange(len(ssp_ids))
width = 0.2  # Adjusted width to fit all bars

# Creating the multi-bar chart
fig, ax = plt.subplots(figsize=(12, 7))
rects1 = ax.bar(x - width, win_rates, width, label='Win Rate', color='blue')
rects2 = ax.bar(x, avg_bids, width, label='Avg Bid ($)', color='green')
rects3 = ax.bar(x + width, np.array(total_impressions) / 100, width, label='Total Impressions (hundreds)', color='orange')

# Adding titles and labels
ax.set_ylabel('Values')
ax.set_title('SSP Performance Metrics')
ax.set_xticks(x)
ax.set_xticklabels(ssp_ids)
ax.legend()

# Adding data labels
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(rects1)
add_labels(rects2)
add_labels(rects3)

# Display the chart
plt.tight_layout()
plt.show()
