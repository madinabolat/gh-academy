package org.example;

public class lc_121_BestTimeToBuyAndSellStock {
        public static int maxProfitBruteForce(int[] prices) {
            if (prices.length == 1){
                return 0;
            }
            int maxProfit = 0;
            for (int i = 0; i < prices.length; i++){
                for (int j = i+1; j < prices.length; j++){
                    maxProfit = Math.max(maxProfit, prices[j]-prices[i]);
                }
            }
            return maxProfit;
        }

        public static int maxProfit(int[] prices){
            int lowestSoFar = prices[0];
            int profit = 0;
            for (int todaysPrice : prices){
                lowestSoFar = Math.min(lowestSoFar, todaysPrice);
                profit = Math.max(profit, todaysPrice - lowestSoFar);
            }
            return profit;
        }

    public static int maxProfitAlt(int[] prices){
            int n = prices.length;
            int max_profit = 0;
            int cheapest_price_to_buy_before_day_i = prices[0];
            for (int i = 1; i<n; i++){
                int profit = prices[i]-cheapest_price_to_buy_before_day_i;
                if (profit > max_profit){
                    max_profit = profit;
                }
                if (prices[i]<cheapest_price_to_buy_before_day_i){
                    cheapest_price_to_buy_before_day_i = prices[i];
                }
            }
            return max_profit;
    }

    public static void main(String[] args) {
        int[] prices = new int[]{7,1,5,3,6,4};
        System.out.println(maxProfitAlt(prices));
    }

}
