# Odoo 6 + PostgreSQL 9 Development Environment

A complete development setup for Odoo 6.1 with PostgreSQL 9 database backend, containerized with Docker for easy deployment and development.

## 📋 Overview

This project is an Odoo 6 ERP system with custom modules designed for enterprise resource planning. It includes a PostgreSQL 9 database backend and Docker containerization for consistent development environments across team members.

**Project Details:**
- **Odoo Version:** 6.1
- **Database:** PostgreSQL 9
- **Python Version:** 2.7 (Odoo 6 compatibility)
- **Deployment:** Docker & Docker Compose

## 🚀 Quick Start

### Prerequisites
- Docker Desktop installed
- Docker Compose (included with Docker Desktop)
- Git for version control
- Windows Terminal or Command Prompt

### Installation Steps

1. **Clone the repository:**
```bash
cd d:\Workshop_openerp-dev - 13-03-2026\odoo6+pg9
```

2. **Start the Docker containers:**
```bash
docker-compose up -d
```

3. **Access Odoo in your browser:**
```
http://localhost:8069
```

4. **Login with default credentials:**
- Username: `admin`
- Password: `admin`

5. **Stop the services:**
```bash
docker-compose down
```

## 📁 Project Structure

```
odoo6+pg9/
├── addons/                           # Custom Odoo modules
│   ├── block_pr_po_attachment/       # Purchase Order attachment blocker
│   │   ├── __init__.py
│   │   ├── __openerp__.py
│   │   ├── models.py
│   │   ├── views/
│   │   └── static/
│   └── [other_custom_modules]/
├── config/
│   └── odoo.conf                     # Odoo configuration file
├── initdb/
│   ├── restore.sh                    # Database restore script
│   └── [backup files]/
├── docker-compose.yml                # Docker services orchestration
├── Dockerfile                        # Odoo container image definition
├── .gitignore                        # Git ignore patterns
├── .gitattributes                    # Git line ending configuration
└── README.md                         # This file
```

## 🐳 Docker Services Configuration

### Odoo Web Service
- **Container Name:** odoo_web
- **Port:** 8069 (Odoo interface)
- **Image:** Odoo 6.1
- **Database:** Connected to PostgreSQL service
- **Volumes:** 
  - Custom addons from `./addons`
  - Configuration from `./config/odoo.conf`

### PostgreSQL Database Service
- **Container Name:** odoo_db
- **Port:** 5432 (internal database port)
- **Image:** PostgreSQL 9
- **Database Name:** odoo
- **Default User:** odoo
- **Default Password:** odoo
- **Volumes:** Database data persistence

## 📦 Custom Modules

### Block PR PO Attachment Module
**Location:** `addons/block_pr_po_attachment/`

**Purpose:** Restricts PDF file uploads to a maximum of 5 MB for Purchase Orders and Requisitions.

**Features:**
- Validates file size before upload
- Supports PDF format validation
- Custom error messages for size violations
- Applied to Purchase Order and Requisition documents

**Installation:**
1. Go to Odoo's Module list
2. Search for "Block PR PO Attachment"
3. Click Install

## 🔧 Development Workflow

### Running Commands in Docker

**View Odoo logs:**
```bash
docker logs -f odoo_web
```

**View PostgreSQL logs:**
```bash
docker logs -f odoo_db
```

**Access Odoo container shell:**
```bash
docker exec -it odoo_web bash
```

**Access PostgreSQL shell:**
```bash
docker exec -it odoo_db psql -U odoo -d odoo
```

### Database Management

**Backup Odoo database:**
```bash
docker exec odoo_db pg_dump -U odoo odoo > backup_$(date +%Y%m%d_%H%M%S).sql
```

**Restore from backup:**
```bash
docker exec -i odoo_db psql -U odoo odoo < backup_file.sql
```

**Access database directly:**
```bash
docker exec -it odoo_db psql -U odoo odoo
```

### Module Development

**Reload a specific module:**
```bash
docker exec odoo_web odoo -u module_name
```

**Install a new module:**
```bash
docker exec odoo_web odoo -i module_name
```

## 🐛 Troubleshooting

### Port 8069 Already in Use

**Find process using the port:**
```bash
netstat -ano | findstr :8069
```

**Kill the process (replace PID):**
```bash
taskkill /PID <PID> /F
```

**Or change port in docker-compose.yml:**
```yaml
ports:
  - "8070:8069"  # Change 8070 to desired port
```

### Database Connection Errors

**Verify PostgreSQL is running:**
```bash
docker logs odoo_db
```

**Recreate containers with fresh database:**
```bash
docker-compose down -v
docker-compose up -d
```

**Check database connectivity:**
```bash
docker exec odoo_web odoo -c /etc/odoo/odoo.conf --db_host=odoo_db --db_user=odoo
```

### Container Won't Start

**Check container status:**
```bash
docker ps -a
```

**View detailed error logs:**
```bash
docker logs odoo_web
docker logs odoo_db
```

**Rebuild containers:**
```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Line Ending Issues (CRLF/LF)

Git may show warnings about line endings. This is normal on Windows. The `.gitattributes` file ensures consistent line endings.

## ⚙️ Configuration

### Odoo Configuration (`config/odoo.conf`)
Key settings:
- Database host: `odoo_db`
- Database user: `odoo`
- Database password: `odoo`
- Admin password: Set during initialization
- Addons path: `/mnt/extra-addons`

### Docker Compose Configuration (`docker-compose.yml`)
- Service networking between odoo and database
- Volume mounting for persistence
- Port mappings
- Environment variables

## 📝 Git Workflow

**Initial commit:**
```bash
git add .
git commit -m "Initial Odoo 6 setup with PostgreSQL 9"
```

**Ignore unnecessary files** (already in `.gitignore`):
- Python cache files
- IDE configuration
- Database files
- Docker overrides
- Environment variables

## 🤝 Team Development

**For team members:**
1. Clone the repository
2. Run `docker-compose up -d`
3. Access Odoo at `http://localhost:8069`
4. Coordinate addon development in the `addons/` folder

**Avoid committing:**
- Database files
- Local configuration overrides
- IDE-specific settings
- Generated Python bytecode

## 📞 Support & Documentation

**Odoo Documentation:** https://www.odoo.com/documentation/6.1/

**PostgreSQL 9 Docs:** https://www.postgresql.org/docs/9.0/

**Docker Documentation:** https://docs.docker.com/

For project-specific issues, contact the development team.

## 📄 License

Internal use only - Proprietary

---

**Last Updated:** March 20, 2026
**Odoo Version:** 6.1
**PostgreSQL Version:** 9