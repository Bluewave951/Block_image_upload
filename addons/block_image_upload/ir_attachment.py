# -*- coding: utf-8 -*-
from osv import osv
import base64

class ir_attachment(osv.osv):
    _inherit = 'ir.attachment'

    def create(self, cr, uid, vals, context=None):
        context = context or {}

        model = vals.get('res_model')
        name = vals.get('datas_fname', '') or ''

        # เฉพาะ PR / PO
        if model in ['purchase.order', 'purchase.requisition']:

            # check file type
            if not name.lower().endswith('.pdf'):
                raise osv.except_osv('Error', 'อนุญาตเฉพาะไฟล์ PDF')

            # check size
            datas = vals.get('datas')
            if datas:
                file_size = len(base64.b64decode(datas))
                if file_size > 5 * 1024 * 1024:
                    raise osv.except_osv('Error', 'ไฟล์ต้องไม่เกิน 5 MB')

        return super(ir_attachment, self).create(cr, uid, vals, context=context)