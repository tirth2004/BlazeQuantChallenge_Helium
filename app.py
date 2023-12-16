import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from crypto_pie_chart import crypto_pie_chart

def helium_overview():
    st.title("Helium (HNT) Overview")

    st.header("Functionality")
    st.write(
        'Stating their whitepaper : "The IOT is 800 Billion dollar industry, with over 8.4 billion devices connected online, with over 1.4 Trillion dollar spending each year. All of these devices need internet, but the current solutions are suboptimal: too expensive, too power hungry, or limited in range. Thus HNT network was introduced to let users connect to internet and geolocate themselves without the need of power hungry hardware"'

    )
    st.write(
        'Originally, HNT Network had proposed a WHIP protocol, but at present they continue to use the LoRaWAN wireless protocol ( From which WHIP was derived ). They introduced the helium hotspot, a LoRaWAN device. The Helium Hotspot enables anyone to own and operate a wireless network for low-power Internet of Things (IoT) devices. The Helium Hotspot provides hundreds of square miles of connectivity and can transmit data at a fraction of the cost of a cellular network. Hotspots also acts as miners on the Helium blockchain so owners can earn a new cryptocurrency (HNT), for building the network and transferring IoT device data.Smart pet collars, environmental sensors, bike trackers, or any compatible IoT device can connect to Helium Hotspots without Wi-Fi or cellular networks.'
    )

    st.write(
        'They introduced a new consensus protocol for their network. For miners, it constituted proof of coverage and proof of serialisation, which enabled proof of location for routers ( normal users ).'
    )

    st.header('Proof of coverage')
    st.write('Verify that Hotspots accurately represent their location, configuration, and the wireless coverage they create. Miners are rewarded HNT for perfoming PoC.')
    st.write('Reward function:')
    

    st.markdown("<h4 style='text-align: center;'>Miner Verification Variables</h4>", unsafe_allow_html=True)
    table_data = [
        ("M", "Miner"),
        ("v", "Number of successful verifications for M- Number of failed verifications for M"),
        ("h", "Height since the last successful verification for M")
    ]

    # Display table
    st.table(table_data)

    st.image("assets/Function.png", caption="Function", use_column_width=True)
    st.image("assets/Trendlines.png", use_column_width=True)

    st.header("Proof of serialisation")
    st.write(" To achieve cryptographic time consensus among decentralized clients, HNT implemented a simplified form of Google’s Roughtime. Roughtime is a protocol that aims to achieve rough time synchronization in a secure way that does not depend on any particular time server, and in such a way that, if a time server does misbehave, clients end up with cryptographic proof of that behavior.")

    st.header("Proof of location")
    st.write("Using Proof-of-Coverage and Proof-of-Serialization, HNT achieved cryptographic proof of a Miners location and cryptographic time consensus among Miners. They took advantage of these proofs to determine the physical geolocation of WHIP-compatible Devices and generate a new type of proof based on the Devices geolocations.")
    st.image("assets/SystemOverview.png", caption="Overview of entire network", use_column_width=True)
    st.write("This explains a basic functionality of their network, and how they incentivise, both users and miners to onboard their network")


def fees():
    st.title("HNT Fees and revenue model")
    st.image("assets/RevenueModel.png", use_column_width=True)
    st.write( "You need a router which costs 400USD to mine HNT. Comparing it with BTC or ETH, they require no additional hardware, though your system should have good GPU and cooling systems")
    st.write("Bitcoin fees are market-driven and can vary based on network demand and transaction priority, Ethereum uses a gas fee system, where transaction fees depend on network activity and the complexity of smart contracts. In contrast, Helium's fee structure includes a mix of variable, fixed, and transaction-specific fees tailored to its IoT-focused network")

def tokenomics():
    st.title("Tokenomics")

    csv_path = 'assets/hnt-usd-max.csv'
    data = pd.read_csv(csv_path)
    st.subheader("Price vs. Date (HNT)")

    # Convert 'snapped_at' to datetime
    data['snapped_at'] = pd.to_datetime(data['snapped_at'])

    # Set 'snapped_at' as the index
    data.set_index('snapped_at', inplace=True)

    # Plot the line chart
    fig, ax = plt.subplots()
    ax.plot(data['price'], label='Price', color='blue')
    ax.set(xlabel='Date', ylabel='Price', title='Price vs. Date')
    ax.legend()
    st.pyplot(fig)

    csv_path2 = 'assets/btc-usd-max.csv'
    data2 = pd.read_csv(csv_path2)
    st.subheader("Price vs. Date (BTC)")

    # Convert 'snapped_at' to datetime
    data2['snapped_at'] = pd.to_datetime(data2['snapped_at'])

    # Set 'snapped_at' as the index
    data2.set_index('snapped_at', inplace=True)

    start_date = '2020-04-18'
    end_date = '2023-12-14'
    df2_filtered = data2.loc[start_date:end_date]

    # Plot the line chart
    fig, ax = plt.subplots()
    ax.plot(df2_filtered['price'], label='Price', color='blue')
    ax.set(xlabel='Date', ylabel='Price', title='Price vs. Date')
    ax.legend()
    st.pyplot(fig)

    st.image("assets/30DayRollingAverage.png", use_column_width=True)


    st.markdown("<h4 style='text-align: center;'>Some conclusions drawn from above graphs</h4>", unsafe_allow_html=True)

    st.write("The whole crypto market was at peak in Nov 2021 because bitcoin gained popularity during covid, there was industrial adoption of blockchain, NFT boom and many more reasons. And similarly HNT was at its peak in mid Nov '21 with the highest price of USD 55.22 in comparison to Ethereum which had its peak at the similar time with price of USD 4891.70 And we all know that the whole crypto market collapsed after the FTX scandal.")
    st.write("During 2022 period, we can see changes of HNT to be comparable with BTC. Hence we can say during 2022 period, HNT was a stable token. In Recent times, the decline is unlike the BTC. Hence we can conclude HNT to be less stable in recent times.")
    st.write("Price has increased by 198% in the last 1 year")
    st.write("Down -89% from all-time high")
    st.write("If we see the 30-day rolling average, we can observe a similar average during June-July 2023 and the peak period. There has been a very significant drop of average since then")

    crypto_pie_chart()
    st.image("assets/HNTAllocation.png", use_column_width=True)
    st.image("assets/HNTSupplySchedule.png", use_column_width=True)
    st.markdown("<h4>There is no pre-mine of HNT and a maximum supply of 223 Million</h4>", unsafe_allow_html=True)

    data = {
    'Date': ['Jan', 'Feb', 'Mar', 'Apr', 'May','Jun', 'Jul','Aug','Sep','Oct','Nov','Dec'],
    'Market_Cap': [360,400,180,250,190,180,200,260,200,210,350,900],
    'Crypto Rise': [1,1,-1,0,0,0,0,0,0,0,0,0],
    'Binance Delisting': [0,0,1,1,1,1,1,0,0,0,0,0],
    'Solana Migration': [0,0,1,1,1,1,0,0,0,0,0,0],
    'Listing at Coinbase': [0,0,0,0,0,-1,1,-1,0,0,0,0],
    'Unlimited Plan announcement': [0,0,0,0,0,0,0,0,0,0,1,1]
    }
    

    # Creating DataFrame
    df = pd.DataFrame(data)

    # Streamlit app
    st.subheader('Correlation Heatmap of HNT Variables in year 2023')

    # Calculating the correlation matrix
    correlation_matrix = df.corr()

    # Generating the heatmap with adjusted box size for annotations
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})
    plt.title('Correlation Heatmap of HNT Variables in year 2023')

    # Displaying the heatmap using Streamlit
    st.pyplot(heatmap.figure)

    st.write("It can be seen that Solona Migration, Binance delisting and unlimited plan announcement (Explained in detail in sentiment analysis) played a very important role. ")

    st.image("assets/openingClosing.png", use_column_width=True)
    st.image("assets/LowHighPrices.png", use_column_width=True)
    st.write("Could generate signficant profits for people who trade at higher frequency")
    st.image("assets/TradingVolume.png", use_column_width=True)
    st.image("assets/AllTimeTradingVolume.png", use_column_width=True)


 



def market_sentiments():
    st.title("Market Sentiments")

    st.header("Historical market sentiments")
    st.subheader("2019-2020")
    st.write("The token was launched on July 29th, 2019. Since then, it has captured the spotlight.")
    st.write("The HNT token started well enough, trading around USD0.50 initially and rose to USD2.00 within two months. ")
    st.write("The coin’s worth began to grow in August 2020, attaining just over USD1. ")
    st.write("The price sank back to USD 1.25 the subsequent month, increasing to USD 2.00 by October.")

    st.subheader("2021")
    st.write("The price of HNT had been steadily increasing since February to claim the USD 18 tag. ")
    st.write("The HNT coin’s price then fluctuated between USD 18 and USD 12.")
    st.write("On May 28th, HNT hit an all-time high of USD 23. The price then gradually dropped to USD 10 before rising again. ")
    st.write("The cost of HNT reached USD 18.5 due to a USD 111 million investment by Andreessen Horowitz’s crypto fund, which included Ribbit 10T Holdings, Alameda Research, and Multicoin Capital.")

    st.subheader("2022-2023")
    st.write("HNT had lost significant value after the proposed major change, as the core developers of crypto-powered wireless network wanted to move from its own blockchain to Solana, overall HNT was down by 47% in Aug '22.")
    st.write("Helium network migrated to Solana on Apr 18 ‘23 due to which Helium’s IOT token surges 370%.")
    st.write("Though the Helium Network is largest in IOT sector compared to its competitors but the market is on low since 2022 but market saw a little growth in past 1 month because Helium Mobile brings together the Helium Network, a peer-to-peer IoT network, and the nation’s largest 5G provider, T-Mobile, to offer its unlimited plan.")
    st.write("HNT, the governance token for Helium Network, has rallied 213% in the past 30 days.")

    st.header("Social media analysis")
    st.write("Market Sentiment is very volatile, as helium’s developers suggested Solana move, the users weren't happy as they expected there will be many new problems on the new blockchain and many users converted their tokens .")
    st.image("assets/1year.png", use_column_width=True)
    st.write("Initially in the year 2023 the whole crypto market was on rise so HNT grew too but as the major announcements came regarding Solana migration most of the users anticipated the issues and even Binance delisted HNT token ahead of migration so many users moved from the Helium network which led to HNT token hit rock bottom and as the migration took place a bit excitement arouse but the the anticipated problems came true and developer and miners faced many issues in the new system.")
    st.write("Then in the july HNT got listed on coinbase which led to little happiness among users but that didn’t changed much for the long and HNT decline continued but then Helium stepped up and on Dec. 5, Nova Labs, the creator of the open-source Helium network, launched a nationwide data plan in the U.S. As Per a crypto news report, Nova Labs partnered with T-Mobile to launch a USD 20 per month unlimited phone plan. Since then the HNT price is on rise and on a surge of 240% this year ending. And the market sentiment is bullish and users are looking to hold their tokens as they expect more from helium and currently they are happy according to social media research. As token prices surge 258% this month.")
    st.image("assets/1month.png", use_column_width=True)


def governance():
    st.title("Helium DAO Governance mechanism")

    st.write("The process by which the Network can be modified, whether in its technical architecture, the tokens' economic model, or meta-governance changes, is governed by the global community of Helium token owners. Helium token (HNT, IOT, MOBILE) owners include Hotspot owners, Network users, wireless network operators, hardware manufacturers, and more. Tokens are created by providing some form of work for the Network. Tokens must be locked for voting on network changes, ensuring long-term stakeholder alignment.")
    st.write("Anyone participating in the Helium ecosystem can submit a Helium Improvement Proposal (HIP) as a first step to modifying the Network. All HIPs are published in the public Helium GitHub repository, then discussed and debated in public forums, including the Helium community Discord server, and on monthly Community Calls. Any Helium token owner is eligible to vote on HIPs. To vote, a Helium token owner must first lock their tokens for a period of time, up to four years, which grants the owner voting power determined by the number of locked tokens and the lock duration. A 2/3 supermajority of the quorum passes proposals.")
    st.write("The Helium Foundation serves as a steward for the governance process. The Foundation established the initial framework and managed the open Helium GitHub repositories. The Foundation does not vote on HIPs but does vet proposals for compliance with the law and technical feasibility. The Foundation’s role is to provide expert advice and guidance and to implement HIPs after they have passed.")
    st.subheader("Voting Power by lock:")
    st.write("Network participants can deposit HNT tokens to a “governance staking contract”, which are locked and delegated to one or many validators of their choosing. Users have control over the number of tokens they choose to stake, and the period they choose to stake them for. The minimum lockup period is 250,000 blocks and the maximum lockup period is 2,500,000 blocks (both the minimum and maximum time thresholds can be decided by HNT governance).")
    st.write("A user’s voting power is determined by 1) the amount of HNT they vote with, and 2) the amount of time they commit to locking up their tokens. The structure applies a linear multiplier of time to the amount of HNT locked up in the voting contract. For the maximum amount of 2,500,000 blocks, users receive 50x the voting power. For the minimum amount of a 250,000 block lockup, users receive 1x the voting power.")
    st.image("assets/votingpower.png", use_column_width=True)





    

    

# Main Streamlit App
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a section", ["Helium Overview", "Fees and revenue model", "Tokenomics", "Market Sentiments", "Governance"])
    
    if page == "Helium Overview":
        helium_overview()
    elif page == "Fees and revenue model":
        fees()
    elif page == "Tokenomics":
        tokenomics()
    elif page == "Market Sentiments":
        market_sentiments()
    elif page == "Governance":
        governance()

if __name__ == "__main__":
    main()
