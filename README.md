# Odoo 6 + PostgreSQL 9 Project

A Docker-based Odoo 6.1 environment with custom addons for enhancing Purchase Order and Purchase Requisition functionality.

## Project Overview

This project sets up Odoo 6.1 with PostgreSQL 9.3 using Docker Compose. It includes a custom addon called **Block PR PO Attachment** that restricts file uploads for Purchase Orders and Purchase Requisitions.

## Custom Addons

### Block PR PO Attachment (v1.0)

A custom addon that enforces file upload restrictions for Purchase Orders (PO) and Purchase Requisitions (PR).

**Features:**
- ✅ Restricts file attachments to PDF format only
- ✅ Enforces maximum file size limit of 5 MB
- ✅ Applies restrictions only to Purchase Order and Purchase Requisition documents
- ✅ Raises user-friendly error messages in Thai language

**Restrictions apply to:**
- `purchase.order` - Purchase Orders
- `purchase.requisition` - Purchase Requisitions

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation & Setup

1. **Clone or navigate to the project directory:**
   ```bash
   cd odoo6+pg9
   ```

2. **Start the Docker containers:**
   ```bash
   docker-compose up -d
   ```

3. **Access Odoo:**
   - Open your browser and navigate to `http://localhost:8069`
   - Default database credentials:
     - Username: `openerp`
     - Password: `openerp`

### Installing the Custom Addon

1. In Odoo, go to **Settings → Modules** (or **Module Management**)
2. Update the modules list
3. Search for **"Block PR PO Attachment"**
4. Click **Install**

## Project Structure

```
odoo6+pg9/
├── docker-compose.yml          # Docker Compose configuration
├── README.md                    # This file
└── addons/
    └── block_image_upload/
        ├── __init__.py          # Python package initialization
        ├── __openerp__.py       # Addon manifest
        └── ir_attachment.py     # Core addon logic
```

## Docker Services

### Odoo Service
- **Image:** lcrea/odoo:6.1
- **Port:** 8069
- **Extra Addons:** Mounted from `./addons` directory

### PostgreSQL Service
- **Image:** postgres:9.3
- **Database Name:** (default postgres database)
- **User:** openerp
- **Password:** openerp

## Configuration

### Environment Variables

The following environment variables are configured in `docker-compose.yml`:

- `DB_HOST`: db (PostgreSQL container)
- `DB_USER`: openerp
- `DB_PASSWORD`: openerp

## Troubleshooting

### Connecting to the Database

If you need to access PostgreSQL directly:

```bash
docker-compose exec db psql -U openerp
```

### Viewing Logs

```bash
docker-compose logs -f odoo
```

### Restarting Services

```bash
docker-compose restart
```

### Complete Reset

To reset everything and start fresh:

```bash
docker-compose down -v
docker-compose up -d
```

## Development Notes

- The addon is written for Odoo 6.1 using the OSV (Object Services) framework
- File validation occurs at the `create()` method level of the `ir.attachment` model
- Error messages are in Thai language; modify `ir_attachment.py` to change them

## Support

For issues or questions about this project, please check the addon code in `addons/block_image_upload/`.

## License

Please refer to your organization's licensing agreements.

---

**Last Updated:** March 2026
