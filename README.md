# 🔐 Quantum Password Manager

A cutting-edge password management system that combines traditional security with quantum computing technology. Built with Flask, AWS services, and quantum circuits for enhanced security.

![Project Poster](A3%20poster_page-0001.jpg)

## 🚨 SECURITY ALERT

**⚠️ CRITICAL: This project contains placeholder credentials that MUST be replaced before use!**

Before running this application, you MUST:

1. **Replace AWS credentials** in `run_app.py`
2. **Update bucket names** in `Dockerfile`
3. **Create a `.env` file** with your actual credentials
4. **Never commit real credentials** to version control

**Files that need credential updates:**

- `run_app.py` - Lines 4-8: Replace placeholder AWS credentials
- `Dockerfile` - Lines 39-41: Update bucket names
- `.env` file - Create with your actual AWS credentials

## 🌟 Features

### 🔒 Security Features

- **Quantum-Inspired Encryption**: Uses AWS Braket quantum circuits for password verification
- **Cloud Storage**: Encrypted passwords stored securely in AWS S3
- **Two-Factor Authentication**: Enhanced security with 2FA support
- **Session Management**: Secure cookie-based session handling
- **Fernet Encryption**: Military-grade encryption for password storage

### 👤 User Features

- **User Authentication**: Secure registration and login system
- **Password Vault**: Organize and manage all your passwords
- **Password Generator**: Quantum-inspired password generation
- **Responsive Design**: Works seamlessly on all devices
- **Email Notifications**: Stay informed about account activities
- **Customizable Settings**: Personalize your security preferences

### 🚀 Technical Features

- **Flask Web Framework**: Modern Python web development
- **SQLite Database**: Lightweight, reliable data storage
- **AWS Integration**: Cloud services for scalability
- **Docker Support**: Easy deployment and containerization
- **Production Ready**: Gunicorn WSGI server for production

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Git** (for cloning the repository)
- **AWS Account** (for quantum computing and cloud storage)

### AWS Setup Requirements

1. **AWS Account**: Create an account at [AWS Console](https://aws.amazon.com/)
2. **AWS Braket Access**: Enable AWS Braket service for quantum computing
3. **S3 Bucket**: Create buckets for password storage and quantum results
4. **IAM User**: Create an IAM user with appropriate permissions

## 🛠️ Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/quantum-password-manager.git
cd quantum-password-manager
```

### Step 2: Create Virtual Environment

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration

**⚠️ IMPORTANT: Replace all placeholder credentials before running the application!**

Create a `.env` file in the project root with your AWS credentials:

```env
# Flask Configuration
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///quantum_vault.db

# AWS Configuration
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_BUCKET_NAME=your-password-bucket-name
AWS_REGION=us-east-1
BRAKET_BUCKET_NAME=your-braket-results-bucket
```

**Also update the following files with your credentials:**

- `run_app.py` - Replace placeholder AWS credentials
- `Dockerfile` - Update bucket names for Docker deployment

### Step 5: Initialize Database

```bash
python app.py
```

This will create the SQLite database and necessary tables.

## 🚀 Running the Application

### Development Mode

```bash
python app.py
```

### Using the Run Script

```bash
python run_app.py
```

### Production Mode (with Gunicorn)

```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

### Docker Deployment

```bash
# Build the Docker image
docker build -t quantum-password-manager .

# Run the container
docker run -p 5000:5000 quantum-password-manager
```

## 🌐 Access the Application

Once running, open your web browser and navigate to:

```
http://localhost:5000
```

## 📱 Usage Guide

### 1. User Registration

- Click "Register" on the home page
- Fill in your details and create a secure password
- Verify your email address

### 2. Login

- Use your registered email and password
- Enable 2FA for enhanced security

### 3. Password Management

- **Add Passwords**: Store new passwords with descriptions
- **View Vault**: See all your stored passwords
- **Generate Passwords**: Use quantum-inspired generation
- **Edit/Delete**: Manage existing entries

### 4. Security Settings

- Configure password generation preferences
- Set up email notifications
- Manage 2FA settings

## 🔬 Quantum Features

### Quantum Circuit Verification

The application uses AWS Braket to run quantum circuits for password verification:

```python
# Bell state circuit for quantum verification
bell = Circuit().h(0).cnot(0, 1)
```

### Testing Quantum Devices

Run the quantum device test script:

```bash
python test_quantum_devices.py
```

This will:

- List all available quantum devices
- Test device connectivity
- Run sample quantum circuits

## 🏗️ Project Structure

```
quantum-password-manager/
├── app.py                 # Main Flask application
├── quantum_encryption.py  # Quantum computing integration
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── Procfile              # Heroku deployment
├── run_app.py            # Application runner script
├── test_quantum_devices.py # Quantum device testing
├── templates/            # HTML templates
│   ├── base.html         # Base layout
│   ├── home.html         # Landing page
│   ├── login.html        # Login form
│   ├── register.html     # Registration form
│   ├── dashboard.html    # User dashboard
│   ├── vault.html        # Password vault
│   ├── generator.html    # Password generator
│   └── settings.html     # User settings
├── static/               # Static assets
└── instance/             # Database files
```

## 🔧 Configuration

### AWS Services Configuration

1. **S3 Bucket Setup**:

   - Create a bucket for encrypted passwords
   - Configure CORS if needed
   - Set appropriate permissions

2. **Braket Configuration**:

   - Enable AWS Braket service
   - Create a bucket for quantum results
   - Configure IAM permissions

3. **Environment Variables**:
   - Set all required AWS credentials
   - Configure Flask secret key
   - Set database URL

## 🚀 Deployment

### Heroku Deployment

1. Create a Heroku app
2. Set environment variables in Heroku dashboard
3. Deploy using Git:

```bash
heroku create your-app-name
git push heroku main
```

### AWS Elastic Beanstalk

1. Install EB CLI
2. Initialize EB application:

```bash
eb init
eb create
eb deploy
```

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d
```

## 🧪 Testing

### Run Quantum Device Tests

```bash
python test_quantum_devices.py
```

### List Available Devices

```bash
python test_quantum_devices.py
```

## 🔒 Security Considerations

- **⚠️ CRITICAL: Replace all placeholder credentials** before deployment
- **Never commit AWS credentials** to version control
- **Use environment variables** for sensitive data
- **Enable HTTPS** in production
- **Regular security updates** for dependencies
- **Monitor AWS usage** and costs
- **Use IAM roles** instead of access keys when possible
- **Rotate credentials** regularly
- **Enable MFA** for AWS accounts

## 🐛 Troubleshooting

### Common Issues

1. **AWS Credentials Error**:

   - Verify your AWS credentials in `.env` file
   - Check IAM permissions

2. **Quantum Device Unavailable**:

   - Ensure AWS Braket is enabled
   - Check device status in AWS console

3. **Database Errors**:

   - Delete `instance/quantum_vault.db` and restart
   - Check database permissions

4. **Port Already in Use**:
   - Change port in `app.py` or kill existing process
   - Use different port: `python app.py --port 5001`

## 📊 Performance

- **Response Time**: < 2 seconds for most operations
- **Quantum Verification**: ~5-10 seconds per password operation
- **Database**: SQLite optimized for small to medium scale
- **Cloud Storage**: AWS S3 for scalable password storage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flask** web framework
- **AWS Braket** for quantum computing
- **Bootstrap** for frontend design
- **Font Awesome** for icons
- **Qiskit** for quantum computing tools

## 📞 Support

For support and questions:

- Create an issue on GitHub
- Contact the development team
- Check the troubleshooting section

---

**⚠️ Important**: This is a research project demonstrating quantum computing integration. For production use, ensure all security measures are properly configured and tested.

**🔬 Research Project**: Final Year Project Phase 2 - Quantum Computing in Password Management
