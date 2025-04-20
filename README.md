
# 📈 Portfolio Optimization Simulator

This project simulates a portfolio optimization strategy using Modern Portfolio Theory (MPT). It identifies the optimal asset weights that maximize the Sharpe Ratio for a portfolio of five simulated financial assets.

### 💼 Project Overview
- Implements portfolio theory using Python
- Uses historical (simulated) return data for 5 assets
- Applies optimization techniques to calculate maximum Sharpe Ratio allocation

### 📊 Data
- **File:** `portfolio_returns.csv`
- **Assets:** Stock_A, Stock_B, Stock_C, Stock_D, Stock_E
- **Period:** ~2 years of daily returns (504 business days)
- **Generated:** Simulated using NumPy for demonstration purposes

### 🔍 Key Metrics (Annualized)
- ✅ **Expected Return**: Based on weighted mean of asset returns
- ✅ **Volatility**: Standard deviation of portfolio returns
- ✅ **Sharpe Ratio**: Return-to-risk ratio, optimized

### 📁 Files Included
- `portfolio_returns.csv` – Simulated daily returns for 5 assets
- `optimized_portfolio_weights.csv` – Output weights from optimization
- `portfolio_summary.csv` – Expected return, volatility, Sharpe Ratio
- `optimized_weights.png` – Visualization of portfolio allocation

### ⚙️ Methods Used
- Covariance matrix and mean return calculations
- Portfolio return and risk computation
- Sharpe Ratio maximization using `scipy.optimize.minimize`
- Constraints: Weights sum to 1, bounds (0 ≤ weight ≤ 1)

---

### 🚀 How to Run
```bash
pip install numpy pandas matplotlib seaborn scipy
python portfolio_optimizer.py  # (If saved as a .py script)
```

---

👩‍💻 Created by [Priyadharsini Manivannan](https://www.linkedin.com/in/priyadharsini-manivannan)  
📧 mpriyadharsini6599@gmail.com | [GitHub](https://github.com/Priyadharsini0605)
