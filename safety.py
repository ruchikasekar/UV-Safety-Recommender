import sreamlit as s
from uv_utils import uv_index
# Set up the sreamlit app's metadata
s.set_page_config(page_title="UV Safety Recommender", page_icon="🌞")

# App title and description
s.title("🌞 UV Safety Recommender")
s.markdown("""
Get personalized sun exposure advice based on your **skin type**, **sunscreen use**, and **real-time UV index** from your city.
""")

# Ask the user for input
city = s.text_input("🏠 Enter your city:", help="E.g., Berkeley, New York, Mumbai")

skin = s.selectbox(
    "💅 Select your skin type (Fitzpatrick scale):",
    ["I", "II", "III", "IV", "V", "VI"],
    help="""
    Type I: Very fair, always burns  
    Type II: Fair, usually burns  
    Type III: Medium, sometimes burns  
    Type IV: Olive, rarely burns  
    Type V: Brown, very rarely burns  
    Type VI: Very dark, never burns
    """
)

spf = s.slider(
    "🧴 Sunscreen SPF:",
    min_value=0,
    max_value=100,
    value=30,
    help="SPF 15 doubles safe time, SPF 30 triples it, etc."
)

# When a city is provided, fetch UV data and compute recommendation
if city:
    uv = uv_index(city)

    if uv is not None:
        # Show UV index result
        s.markdown(f"**☀️ UV Index in {city.title()}:** `{uv}`")

        # Calculate safe sun exposure time
        safe_time = calculate_safe_minutes(skin, spf, uv)

        # Display result
        s.success(f"✅ Recommended max sun exposure: **{safe_time} minutes**")

        # Give context or warnings based on UV index
        if uv >= 8:
            s.warning("⚠️ UV is **very high** today. Wear protective clothing and avoid going outside mid-day.")
        elif uv >= 6:
            s.info("😎 UV is **moderately high**. Consider sunglasses, hats, and sunscreen.")
        else:
            s.write("🌤️ UV levels are low. Enjoy the outdoors, but don’t forget to reapply sunscreen!")

    else:
        s.error("❌ Could not retrieve UV data for that city. Check the city name and try again.")
else:
    s.info("👆 Enter a city above to get sarted.")
