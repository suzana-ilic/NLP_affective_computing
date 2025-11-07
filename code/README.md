# Text Data Labeling Tool

A simple and intuitive GUI application for labeling text data with emotion categories, designed for emotion recognition and affective computing research.

![Data Labeling App](https://github.com/user-attachments/assets/35ad8b05-08e4-434c-b694-7e966996d7e0)

## Features

- **User-friendly GUI**: Built with Python's tkinter library for easy cross-platform usage
- **Emotion Labels**: Pre-configured with Ekman's 6 basic emotions plus neutral:
  - anger 🤬
  - disgust 🤢
  - fear 😨
  - joy 😀
  - neutral 😐
  - sadness 😭
  - surprise 😲
- **Text Input**: Multi-line text input field for entering text samples
- **Data Management**: 
  - View all labeled entries in a table format
  - Delete individual entries
  - Clear all data
  - Track total number of labeled entries
- **CSV Export**: Download labeled data as CSV file with text and label columns
- **Timestamps**: Automatic timestamping of each labeled entry

## Requirements

- Python 3.x
- tkinter (usually comes pre-installed with Python)

On Ubuntu/Debian systems, if tkinter is not installed:
```bash
sudo apt-get install python3-tk
```

## Usage

### Running the Application

```bash
python3 code/data_labeling_app.py
```

Or directly:
```bash
cd code
python3 data_labeling_app.py
```

### How to Label Data

1. **Enter Text**: Type or paste the text you want to label in the "Text" field
2. **Select Label**: Choose the appropriate emotion label from the dropdown menu
3. **Add Label**: Click the "Add Label" button to save the entry
4. **View Data**: All labeled entries appear in the table below with:
   - ID number
   - Text (truncated if longer than 100 characters)
   - Label
   - Timestamp
5. **Manage Data**:
   - Select an entry and click "Delete Selected" to remove it
   - Click "Clear All" to remove all entries (confirmation required)
6. **Export**: Click "Export to CSV" to save your labeled data
   - Choose a location and filename
   - The CSV will contain two columns: `text` and `label`

### CSV Output Format

The exported CSV file contains the following columns:

```csv
text,label
"I am so happy today! Everything is going great.",joy
"This is absolutely disgusting and unacceptable.",disgust
"I'm really worried about what might happen next.",fear
```

## Use Cases

- Creating training datasets for emotion recognition models
- Annotating text data for affective computing research
- Building labeled corpora for sentiment analysis
- Quick data labeling for machine learning experiments
- Educational purposes in NLP and emotion recognition courses

## Technical Details

- **Language**: Python 3
- **GUI Framework**: tkinter (standard library)
- **Data Storage**: In-memory (during session)
- **Export Format**: CSV (UTF-8 encoded)
- **Window Size**: 900x700 pixels (adjustable)

## Integration with Research

This tool complements the emotion recognition research in this repository by providing an easy way to:
- Create custom labeled datasets
- Annotate new data for model training
- Prepare evaluation datasets
- Conduct inter-annotator agreement studies

The emotion labels align with the basic emotions discussed in the main research (see main [README.md](../README.md)).

## Future Enhancements

Potential improvements for future versions:
- Custom label categories
- Import existing CSV files for editing
- Inter-annotator agreement metrics (Cohen's kappa)
- Multi-label support
- Save/load session functionality
- Keyboard shortcuts for faster labeling
- Undo/redo functionality

## License

This tool is part of the NLP_affective_computing repository and follows the same license.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## Acknowledgments

Emotion labels based on Ekman's basic emotions model, consistent with the research framework described in the main repository.
