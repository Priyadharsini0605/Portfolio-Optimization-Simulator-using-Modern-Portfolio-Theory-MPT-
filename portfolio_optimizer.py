
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize

# Load returns data
returns_df = pd.read_csv("portfolio_returns.csv", index_col=0, parse_dates=True)

# Calculate mean returns and covariance matrix
mean_returns = returns_df.mean()
cov_matrix = returns_df.cov()

# Portfolio performance function
def portfolio_performance(weights, mean_returns, cov_matrix):
    returns = np.dot(weights, mean_returns)
    std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = returns / std_dev
    return returns, std_dev, sharpe_ratio

# Negative Sharpe Ratio (to minimize)
def neg_sharpe_ratio(weights, mean_returns, cov_matrix):
    return -portfolio_performance(weights, mean_returns, cov_matrix)[2]

# Constraints and bounds
constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
bounds = tuple((0, 1) for _ in range(len(mean_returns)))
initial_weights = [1. / len(mean_returns)] * len(mean_returns)

# Run optimization
opt_result = minimize(neg_sharpe_ratio, initial_weights, args=(mean_returns, cov_matrix),
                      method='SLSQP', bounds=bounds, constraints=constraints)

# Get results
opt_weights = opt_result.x
opt_returns, opt_std, opt_sharpe = portfolio_performance(opt_weights, mean_returns, cov_matrix)

# Save weights
weights_df = pd.DataFrame({'Asset': mean_returns.index, 'Weight': opt_weights})
weights_df.to_csv("optimized_portfolio_weights.csv", index=False)

# Save performance summary
summary_df = pd.DataFrame({
    'Metric': ['Expected Annual Return', 'Volatility (Risk)', 'Sharpe Ratio'],
    'Value': [round(opt_returns * 252, 4), round(opt_std * np.sqrt(252), 4), round(opt_sharpe, 4)]
})
summary_df.to_csv("portfolio_summary.csv", index=False)

# Save plot
plt.figure(figsize=(8, 5))
sns.barplot(data=weights_df, x='Asset', y='Weight')
plt.title('Optimized Portfolio Weights')
plt.ylabel('Weight Allocation')
plt.xlabel('Asset')
plt.tight_layout()
plt.savefig("optimized_weights.png")
plt.close()
