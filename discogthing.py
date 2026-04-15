
import discogs_client
import time



token1 = "VkddoQKTjSFFyGhddvoizeELuqeYdtXSUDFEdiFD" 
client = discogs_client.Client('demandproject/1.0', user_token=token1)
styles = ["Pop", "Rock", "Noise", "Industrial", "Vaporwave"] 



for s in styles:
    total_wants = 0
    total_haves = 0

    results = client.search(style=s, type='master', sort='relevance')

    for release in results.page(1)[:50]:
        community = release.data.get('community', {})
        wants = community.get('want', 0)
        haves = community.get('have', 0)

        if haves > 20:
            total_wants += wants
            total_haves += haves

    average = total_wants / total_haves 
    print(f"Style: {s} | Ratio: {round(average, 2)}")

    time.sleep(1)