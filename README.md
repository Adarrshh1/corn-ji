# 🌽 Corn Ji - AI-Powered Corn Disease Detection

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An intelligent web application for detecting corn leaf diseases using deep learning and computer vision.

## 🎯 Features

- 🔬 **AI Disease Detection** - Identifies 4 types of corn diseases with high accuracy
- 📸 **Camera Integration** - Capture leaf images directly from your device
- 📊 **Scan History** - Track all your scans with detailed results
- 🌦️ **Weather-Based Risk Assessment** - Disease risk prediction based on climate
- 📱 **Mobile Responsive** - Works seamlessly on all devices
- 🛡️ **Admin Dashboard** - Analytics and performance monitoring
- 📄 **Report Generation** - Export detailed analysis reports

## 🦠 Detected Diseases

1. **Northern Leaf Blight** 🍂
2. **Common Rust** 🟠
3. **Gray Leaf Spot** 🩶
4. **Healthy** ✅

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Adarrshh1/corn-ji.git
cd corn-ji
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run files/app.py
```

4. **Open in browser**
```
http://localhost:8501
```

## 📁 Project Structure

```
corn-ji/
├── docs/                    # Documentation
├── files/                   # Main application
│   ├── app.py              # Entry point
│   ├── components/         # UI components
│   ├── core/               # Business logic
│   │   ├── predict.py      # AI prediction engine
│   │   └── disease_info.py # Disease database
│   ├── styles/             # CSS styling
│   ├── ui/                 # User interface pages
│   └── scan_data/          # User data storage
├── models/                  # AI models
│   └── corn_model.h5       # Trained model
└── requirements.txt         # Dependencies
```

## 🎨 Screenshots

### Landing Page
Beautiful landing page with disease overview

### Scan Interface
Upload or capture leaf images for instant analysis

### Results Dashboard
Detailed disease information with treatment recommendations

### Scan History
Track all your previous scans with timestamps

## 🧠 Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI/ML**: TensorFlow, Keras
- **Image Processing**: Pillow, NumPy
- **Styling**: Custom CSS

## 📊 Model Information

- **Architecture**: CNN (Convolutional Neural Network)
- **Input Size**: 224x224x3
- **Classes**: 4 (Blight, Rust, Gray Leaf Spot, Healthy)
- **Accuracy**: 98.4%
- **Framework**: TensorFlow 2.13+

## 🎯 Usage

### For Farmers

1. Navigate to **Scan Leaf** page
2. Upload or capture a corn leaf image
3. Click **Scan Leaves** button
4. View detailed disease analysis
5. Follow treatment recommendations

### For Admins

1. Switch to **Admin Mode**
2. View analytics dashboard
3. Monitor system performance
4. Manage users and settings

## 🌟 Key Features Explained

### AI Analysis
- Real-time disease detection
- Confidence score for each prediction
- Multiple disease probability distribution

### Weather Integration
- Climate-based disease risk assessment
- 5-day weather forecast
- Preventive action recommendations

### Scan History
- Automatic scan storage
- Image compression for efficiency
- Searchable history with filters

### Mobile Support
- Responsive design
- Touch-friendly interface
- Camera access on mobile devices

## 🔧 Configuration

### Model Path
Update model path in `files/core/predict.py` if needed:
```python
model_paths = [
    "models/corn_model.h5",
    # Add custom paths here
]
```

### Styling
Customize colors and themes in `files/styles/styles.py`

## 📝 Development

### Adding New Features

1. **UI Changes** → `files/ui/`
2. **Business Logic** → `files/core/`
3. **Styling** → `files/styles/`
4. **Components** → `files/components/`

### Code Style

- Follow PEP 8 guidelines
- Use docstrings for functions
- Keep functions small and focused
- Comment complex logic

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Adarsh**
- GitHub: [@Adarrshh1](https://github.com/Adarrshh1)

## 🙏 Acknowledgments

- Disease information from agricultural research papers
- UI inspiration from modern web applications
- Community feedback and testing

## 📞 Support

For support, email or open an issue on GitHub.

## 🔮 Future Enhancements

- [ ] Multi-language support
- [ ] Offline mode
- [ ] Mobile app (iOS/Android)
- [ ] More disease types
- [ ] Pest detection
- [ ] Nutrient deficiency detection
- [ ] Integration with agricultural databases
- [ ] Real-time weather API
- [ ] PDF report generation
- [ ] WhatsApp integration

## 📈 Version History

See [CHANGELOG.md](docs/CHANGELOG.md) for detailed version history.

---

**Made with ❤️ for farmers and agriculture**

⭐ Star this repo if you find it helpful!
