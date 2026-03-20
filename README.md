# GeoWords - Coordinate to Memorable Words Converter

A tool to convert geographic coordinates (latitude/longitude) into memorable English word combinations and back. Perfect for sharing locations, creating memorable place identifiers, or generating human-friendly location codes.

## Features

- **Memorable**: Replace hard-to-remember coordinates like `51.620911810040575, 5.035252699370698` with `love poppy star eternal`
- **Accurate**: ~35 meters precision with 4-word combinations
- **Bidirectional**: Encode coordinates to words, decode words to coordinates
- **Customizable**: Choose 2, 3, or 4 words for different accuracy levels
- **Clean API**: Simple Python interface for integration into your projects

## Quick Start

```bash
pip install -r requirements.txt
```

### Python Usage

```python
from geowords import GeoWords

# Create converter (default: 4 words)
converter = GeoWords(num_words=4)

# Convert coordinates to words
words = converter.encode(52.3676, 4.9041)  # Amsterdam
print(words)  # ['maple', 'river', 'stone', 'bridge']

# Convert words back to coordinates
lat, lon = converter.decode(words)
print(f"Location: {lat:.6f}, {lon:.6f}")

# Check accuracy
accuracy = converter.get_accuracy()
print(f"Accuracy: {accuracy:.2f} meters")
```

## Examples

| Location | Coordinates | Words |
|----------|-------------|-------|
| Amsterdam | 52.3676, 4.9041 | `maple river stone bridge` |
| London | 51.5074, -0.1278 | `ocean valley mountain peak` |
| Paris | 48.8566, 2.3522 | `forest river golden sun` |
| New York | 40.7128, -74.0060 | `city street bright light` |
| Tokyo | 35.6762, 139.6503 | `cherry blossom morning dawn` |
| Sydney | -33.8688, 151.2093 | `harbor bridge opera sea` |
| Reykjavik | 64.1466, -21.9426 | `northern lights aurora ice` |

## Web Interface

Visit our [GeoWords Web Converter](https://yourusername.github.io/gps/) to:
- Convert coordinates to words in your browser
- Convert words back to coordinates
- Share locations via memorable word combinations

## Configuration

```python
# 2 words (~500m accuracy)
converter = GeoWords(num_words=2)

# 3 words (~70m accuracy)
converter = GeoWords(num_words=3)

# 4 words (~35m accuracy) - recommended
converter = GeoWords(num_words=4)
```

## Use Cases

### Gaming and Entertainment
- **ARGs and Escape Rooms**: Hide clues as word combinations players must decode
- **Geocaching 2.0**: Replace cryptic coordinates with poetic hints
- **Location-based Games**: Create memorable spawn points and landmarks
- **Scavenger Hunts**: Design puzzles where words lead to real-world locations

### Privacy and Security
- **Selective Disclosure**: Share approximate locations without revealing exact coordinates
- **Safe Meeting Points**: Pre-agreed word codes for rendezvous locations
- **Travel Itineraries**: Share trip highlights without GPS trails
- **Journaling**: Document special places with meaningful word associations

### Social and Communication
- **Date Night Spots**: "Let's meet at `sunset harbor golden waves`"
- **Recommendation Sharing**: "You'll love `cozy corner warm light`"
- **Memory Anchors**: Associate life events with word-coded locations
- **Family Traditions**: Create generational location codes for special places

### Business and Professional
- **Site Visits**: Replace boring addresses with memorable location codes
- **Asset Tracking**: Tag equipment/storage locations with word identifiers
- **Real Estate**: Create poetic property identifiers for listings
- **Event Planning**: Venue codes that are easier to communicate

### Creative and Artistic
- **Poetic Mapping**: Turn geography into verse-like location names
- **Story Writing**: Generate authentic-sounding place names for fiction
- **Photography Projects**: Tag photo locations with evocative word combinations
- **Personal Cartography**: Create custom maps with meaningful place names

### Education and Learning
- **Geography Games**: Teach coordinates through memorable word associations
- **Memory Training**: Practice location recall with word cues
- **Language Learning**: Connect vocabulary with real-world locations
- **History Lessons**: Code historical sites with period-appropriate words

### Travel and Adventure
- **Bucket List Locations**: Code dream destinations with aspirational words
- **Travel Journals**: Document visits with personal word combinations
- **Hidden Gems**: Share off-the-beaten-path spots with friends
- **Pilgrimage Routes**: Create spiritual journey markers

### Personal and Sentimental
- **Anniversary Spots**: "Our `first dance midnight stars` location"
- **Proposal Sites**: "Where we said `forever golden sunrise`"
- **Family Heritage**: Code ancestral homes and meaningful places
- **Life Milestones**: Mark significant life events with location words

### Technical and Development
- **API Integration**: Human-friendly location codes in your apps
- **Database Design**: Store locations as searchable word combinations
- **QR Codes**: Generate shareable location cards with word codes
- **IoT Devices**: Location tagging for smart home/geofencing systems

### Specialized Applications
- **Emergency Services**: Quick location communication in crisis situations
- **Search and Rescue**: Coordinate teams with memorable waypoint codes
- **Environmental Monitoring**: Tag sensor locations with descriptive codes
- **Urban Planning**: Community-friendly location referencing system

## How It Works

The world is divided into a grid where each cell maps to a unique word combination. The system uses:
- **920 English words** for encoding
- **Base-N encoding** to create unique combinations
- **Grid-based mapping** for consistent bidirectional conversion

More words = finer grid = higher accuracy.

## Installation

```bash
git clone https://github.com/yourusername/gps.git
cd gps
pip install -r requirements.txt
```

## Testing

```python
from geowords import GeoWords

converter = GeoWords(num_words=4)

# Test roundtrip
lat, lon = 51.620911810040575, 5.035252699370698
words = converter.encode(lat, lon)
decoded_lat, decoded_lon = converter.decode(words)

print(f"Original:  {lat}, {lon}")
print(f"Words:     {words}")
print(f"Decoded:   {decoded_lat}, {decoded_lon}")
print(f"Error:     {abs(lat - decoded_lat):.8f}, {abs(lon - decoded_lon):.8f}")
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - feel free to use in your projects!

---

Made for memorable locations
