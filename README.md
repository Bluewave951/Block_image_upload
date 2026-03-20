# Odoo 6 + PostgreSQL 9 Development Environment

A complete development setup for Odoo 6.1 with PostgreSQL 9 database backend.

## 📋 Overview

This project contains a containerized Odoo 6 ERP system with custom modules for purchase order management and document attachment handling.

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose installed
- Windows Terminal or CMD

### Running the Project

1. **Start services:**
```bash
docker-compose up -d
```

2. **Access Odoo:**
- URL: `http://localhost:8069`
- Default credentials: `admin` / `admin`

3. **Stop services:**
```bash
docker-compose down
```

## 📁 Project Structure

```
odoo6+pg9/
├── addons/                    # Custom modules
│   ├── block_pr_po_attachment/
│   │   ├── __init__.py
│   │   ├── __openerp__.py
│   │   ├── models.py
│   │   └── views/
│   └── ...
├── config/
│   └── odoo.conf             # Odoo configuration
├── docker-compose.yml         # Docker services definition
├── Dockerfile                 # Odoo container image
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## 🐳 Docker Services

### Odoo Service
- **Image:** Odoo 6.1
- **Port:** 8069
- **Database:** PostgreSQL 9
- **Volumes:** Custom addons mounted from `./addons`

### PostgreSQL Service
- **Port:** 5432
- **Database Name:** odoo
- **User:** odoo
- **Password:** odoo

## 📦 Custom Modules

### Block PR PO Attachment
Restricts PDF file uploads to a maximum of 5 MB for Purchase Orders and Requisitions.

**Features:**
- Validates file size before upload
- Supports PDF format only
- Custom error messages

## 🔧 Development Commands

### Database Management
```bash
# Backup database
docker exec odoo_db pg_dump -U odoo odoo > backup.sql

# Restore database
docker exec -i odoo_db psql -U odoo odoo < backup.sql
```

### Odoo Management
```bash
# View logs
docker logs -f odoo_web

# Execute Odoo script
docker exec odoo_web python manage.py
```

### Terminal Commands
```bash
# List running containers
docker ps

# Access container shell
docker exec -it odoo_web bash

# Restart services
docker-compose restart
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in docker-compose.yml or kill process
netstat -ano | findstr :8069
taskkill /PID <PID> /F
```

### Database Connection Error
```bash
# Verify PostgreSQL is running
docker logs odoo_db

# Recreate containers
docker-compose down -v
docker-compose up -d
```

### Module Installation Issues
```bash
# Reload modules
docker exec odoo_web odoo -u module_name
```

## 📝 License

Internal use only

## 👤 Support

For issues or questions, contact the development team.