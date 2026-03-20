"""
GeoWords Converter - Convert coordinates to memorable English words and back.
"""

import math
from typing import List, Optional, Tuple
from .wordlist import WORDS


class GeoWords:
    """
    Convert geographic coordinates to memorable word combinations and back.
    
    The world is divided into a grid where each cell is mapped to a unique
    word combination. More words provide higher accuracy.
    """
    
    def __init__(self, num_words: int = 3, lat_offset: float = 0.0, lon_offset: float = 0.0):
        """
        Initialize the converter.
        
        Args:
            num_words: Number of words to use (2, 3, or 4). More = higher accuracy.
            lat_offset: Latitude offset to shift the grid (for custom word mappings).
            lon_offset: Longitude offset to shift the grid (for custom word mappings).
        """
        if num_words not in (2, 3, 4):
            raise ValueError("num_words must be 2, 3, or 4")
        
        self.num_words = num_words
        self.words = WORDS
        self.base = len(WORDS)
        
        # Coordinate ranges
        self.lat_min, self.lat_max = -90, 90
        self.lon_min, self.lon_max = -180, 180
        
        # Grid offsets for custom word mappings
        self.lat_offset = lat_offset
        self.lon_offset = lon_offset
        
        # Calculate grid resolution based on number of words
        self._update_resolution()
    
    def _update_resolution(self) -> None:
        """Update grid resolution based on number of words."""
        total_combinations = self.base ** self.num_words
        
        # Divide latitude and longitude ranges
        lat_cells = int(math.sqrt(total_combinations))
        lon_cells = int(math.sqrt(total_combinations))
        
        self.lat_step = (self.lat_max - self.lat_min) / lat_cells
        self.lon_step = (self.lon_max - self.lon_min) / lon_cells
    
    def encode(self, latitude: float, longitude: float) -> List[str]:
        """
        Convert coordinates to a list of words.
        
        Args:
            latitude: Latitude in degrees (-90 to 90)
            longitude: Longitude in degrees (-180 to 180)
            
        Returns:
            List of words representing the coordinates
        """
        # Clamp coordinates to valid ranges
        latitude = max(self.lat_min, min(self.lat_max, latitude))
        longitude = max(self.lon_min, min(self.lon_max, longitude))
        
        # Convert to grid indices (with offset)
        lat_index = int((latitude - self.lat_min + self.lat_offset) / self.lat_step)
        lon_index = int((longitude - self.lon_min + self.lon_offset) / self.lon_step)
        
        # Calculate total cells
        lat_cells = int((self.lat_max - self.lat_min) / self.lat_step)
        lon_cells = int((self.lon_max - self.lon_min) / self.lon_step)
        
        # Combine into single index
        combined_index = lat_index * lon_cells + lon_index
        
        # Ensure index is within bounds
        max_index = (self.base ** self.num_words) - 1
        combined_index = min(combined_index, max_index)
        
        # Convert to base-N representation (N = number of words)
        word_indices = []
        for _ in range(self.num_words):
            word_indices.append(combined_index % self.base)
            combined_index //= self.base
        
        # Map indices to words
        return [self.words[i] for i in word_indices]
    
    def decode(self, words: List[str]) -> Tuple[float, float]:
        """
        Convert a list of words back to coordinates.
        
        Args:
            words: List of words (should match num_words used in encoding)
            
        Returns:
            Tuple of (latitude, longitude) in degrees
        """
        # Validate words
        if len(words) != self.num_words:
            raise ValueError(f"Expected {self.num_words} words, got {len(words)}")
        
        # Convert words to indices
        indices = []
        for word in words:
            if word not in self.words:
                raise ValueError(f"Unknown word: {word}")
            indices.append(self.words.index(word))
        
        # Convert base-N representation to single index
        combined_index = 0
        for i, idx in enumerate(indices):
            combined_index += idx * (self.base ** i)
        
        # Convert back to grid indices
        lon_cells = int(math.sqrt(self.base ** self.num_words))
        lat_index = combined_index // lon_cells
        lon_index = combined_index % lon_cells
        
        # Convert to coordinates (center of cell)
        latitude = self.lat_min - self.lat_offset + lat_index * self.lat_step + self.lat_step / 2
        longitude = self.lon_min - self.lon_offset + lon_index * self.lon_step + self.lon_step / 2
        
        return latitude, longitude
    
    def get_accuracy(self) -> float:
        """
        Get the approximate accuracy in meters.
        
        Returns:
            Approximate accuracy in meters
        """
        # Earth's circumference at equator is ~40,075 km
        # 1 degree of longitude at equator is ~111.32 km
        # 1 degree of latitude is ~111.32 km
        
        lat_meters = self.lat_step * 111320  # meters per degree
        lon_meters = self.lon_step * 111320  # meters per degree (at equator)
        
        # Return average as approximate accuracy
        return (lat_meters + lon_meters) / 2
