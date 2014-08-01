from openerp.osv import fields, osv

class company_employee(osv.osv):
    _name = "company.employee"
    _description = "Employee Detail"
    _columns = {
        'name' : fields.char("Name", size=64),
        'join_date' : fields.datetime('Joined Date', required=True),
        'user_id': fields.many2one('res.users', 'HR Person'),
        'note': fields.text('Terms and conditions'),
        'payment_term': fields.many2one('account.payment.term', 'Payment Term'),
        'fiscal_position': fields.many2one('account.fiscal.position', 'Fiscal Position'),
        'origin': fields.char('Source Info', size=64, help="To track reference related to employee"),
        'enable': fields.boolean('Active', help ="Indicates employee is valid or not"),
        'state': fields.selection([('new', 'New'),
            ('open', 'Accepted'),
            ('cancel', 'Refused'),
            ('close', 'Done')],
            'Status', readonly=False, track_visibility='onchange',
        ),
       
    }
    
    _sql_constraints = [
        ('name', 'unique(name)', 'The name of the Employee must be unique')
    ]
    _defaults = {
        'state': lambda *a: 'new',
        'enable': True,
    }
    _order = 'name asc'
    
    def employee_cancel(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'cancel'}, context=context)

    def employee_open(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'open'}, context=context)

    def employee_close(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'close'}, context=context)

    def employee_draft(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'new'}, context=context)
    
    def employee_turnoff(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'enable': False}, context=context)
    
  
