from openerp import models, fields, api
import smsgateway
import smsgator

class main_document_manager(models.Model):
    _name = 'project.project'
    _inherit = 'project.project'
    _description = 'inherit and extends on project in project.project'
    x_refno = fields.Char('Refenrence No')
    department = fields.Many2one('hr.department', string='Department')
    #pro_member = fields.Many2many ('hr.employee', 'hr_employee_rel', 'emp_id', 'employee_ids')
#     state =  fields.Selection([('draft','New'),
#                                     ('open','In Progress'),
#                                    ('dept1','DPR'),
#                                    ('dept2', 'CPR'),
#                                    ('dept3','GPR'),
#                                    ('dept4','APR')],
#                                   'Status', required=True, copy=False)
    folder_log = fields.Integer(compute='folder_count', string='Folder')
    doc_log = fields.Integer(compute='folder_count', string='Document')

    @api.one
    def folder_count(self):
	total = 0
        record_count = self.env['document.folder']
        folder_logger = record_count.search([('project_id.name','=',self.name)])
        self.folder_log = len(folder_logger)
        for records in record_count.search([('project_id.name','=',self.name)]):
            total += records.document_log
        self.doc_log = total
    
class project_sub_folder(models.Model):
    _name = 'document.folder'
    _inherit = 'mail.thread'
    _description = 'Model created for folders in a project'
    project_id = fields.Many2one('project.project', string='Parent Folder')
    name = fields.Char('Folder Name', required=True)
    ref_no = fields.Many2one('folder.ref.no', string='Reference No', required=True)
    description = fields.Text('Folder Description')
    f_department = fields.Many2one('hr.department', string='Department')
    
    document_log = fields.Integer(compute='document_count', string='Customer')
    
    @api.one
    def document_count(self):
        doc_count = self.env['document.customer']
        doc_logger = doc_count.search([('file_id.name','=',self.name)])
        self.document_log = len(doc_logger)


class document_ref_number(models.Model):
    _name = 'document.ref.no'
    _rec_name = 'xref_no'
    _description = 'The reference number library as a model'
    xref_no = fields.Char('Reference No', required=True)
    folder = fields.Many2one('document.folder',string='Folder name')
    xx_description = fields.Text('Folder Summary', help='Easy understanding of what the folder is for from the refence number')
    
    _sql_constraints = [
        ('unique_number', 'unique(xref_no)', 'Reference Number Aleady Exist'),
    ]


class folder_ref_number(models.Model):
    _name = 'folder.ref.no'
    _rec_name = 'folderxref_no'
    _description = 'The reference number library as a model'
    folderxref_no = fields.Char('Reference No', required=True)
    xproject = fields.Many2one('document.folder',string='Folder name')
    folder_description = fields.Text('Folder Summary', help='Easy understanding of what the folder is for from the refence number')
    
    _sql_constraints = [
        ('unique_number', 'unique(folderxref_no)', 'Reference Number Aleady Exist'),
    ]

class outdoc_ref_number(models.Model):
    _name = 'outdoc.ref.no'
    _rec_name = 'outxref_no'
    _description = 'The reference number library as a model'
    outxref_no = fields.Char('Reference No', required=True)
    outproject = fields.Many2one('project.project',string='Folder name')
    out_description = fields.Text('Folder Summary', help='Easy understanding of what the folder is for from the refence number')
    
    _sql_constraints = [
        ('unique_number', 'unique(outxref_no)', 'Reference Number Aleady Exist'),
    ]

       
class main_customer(models.Model):
    _name = 'document.customer'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _description = 'Incoming Document Customer Module'
    _rec_name = 'sub_name'
    name = fields.Many2one('res.partner', string='Partner', required =True)
    file_id= fields.Many2one('document.folder', string='Folder Name')
    customer_line_ids = fields.One2many('document.customer.line', 'customer_id', string='Customer File Details')
    res_name = fields.Integer('Document Resource', compute='get_resource_id')
    main_filename = fields.Char('Main Filename')
    main_fileget = fields.Binary('Document')
    x_description = fields.Text('Document Subject', required =True)
    x_remarks = fields.Text('Document Remarks')
    x_doccount = fields.Integer('Total no of Pages')
    x_date = fields.Date(default=fields.Date.today(), string='Date')
    doc_date = fields.Date('Date on document')
    x_department = fields.Many2one('hr.department', string='Department')
    doc_location = fields.Char(related='file_id.f_department.name', string='Current Location')
    x_contact = fields.Many2one('res.partner', string='Signature on Document')
    x_dummy = fields.Integer(compute='get_contact_type')
    x_signed = fields.Many2one('res.users', string='Recieved by')
    x_mainfolder = fields.Many2one('project.project', string='Project folder')
    ref_nos = fields.Many2one('document.ref.no', string='Reference')
    sub_name = fields.Char(compute='_compute_doc_subject')
    dept_check = fields.Integer(compute='dept_exist', store=True)
    loc_check = fields.Integer(compute='dept_exist', store=True)


 
    @api.onchange('x_department','doc_location')
    def message_depart_onchange(self):
        username = 'sege01'
        password = 'segunsco'
        msg_type = '0'
        dlr = '0'
        sender = 'DMS'
        message = 'This Message is been sent from GTS Document Management System'
        if self.x_department:
            rec = self.env['res.partner']
            for records in rec.search([('x_dept_res.name','=',self.x_department.name)]):
                print records.phone
                destination = records.phone
                smsgator.smsgatorSMS(username, password, destination, sender, message)
                print 'success'
#             
#    
#   working email code          
#     @api.onchange('x_department','doc_location') 
#     def req_aut(self):
#         cursor = self._cr
#         user = self._uid
#         subject="New Document from SA office"
#         body="Neccessary Messages goes here"
#         message_obj = self.pool.get('mail.mail')
#         if self.x_department:    
#             mail_rec = self.env['res.partner']
#             for records in mail_rec.search([('x_dept_res.name','=',self.x_department.name)]):
#                 email_to = records.email
#                 msg_vals = {
#                     'subject': subject,
#                     'body_text': False,
#                     'body_html': body,
#                     'email_from': 'olusegun.adesanya@gtsng.com',
#                     'email_to': email_to,
#                     'subtype': 'html',
#                     'state': 'outgoing',
#                     }
#                 msg_id = message_obj.create(cursor, user, msg_vals, context=None)
#                 if msg_id:
#                     message_obj.send(cursor, user, [msg_id], context=None) 


#     @api.onchange('x_department','doc_location') 
#     def notify_members(self):      
#         cursor = self._cr
#         user = self._uid
#         thread_pool = self.pool.get('mail.thread')
#         alert_rec = self.env['res.users']
#         if self.x_department:
#             for records in alert_rec.search([('x_dept_res.name','=',self.x_department.name)]):
#                 parted = (4, records.partner_id.id)
#                 post_vars = {'subject': "notification about order", 
#                              'body': "Yes inform me as i belong to manfacture group", 
#                              'partner_ids': parted}
#                 print parted
#             thread_pool.message_post(cursor, user, False,message_type="notification", subtype="mt_comment",context=None, **post_vars)


    @api.model
    def _needaction_domain_get(self):
        return [('dept_check', '=', 1)]


    def my_onchange_function(self, cr, uid, ids, file_id, context=None):
        if context is None: context = {}
        # If there's a value in list1 now, empty list2.
        res = {}
        if file_id:
            res['x_department'] = False
        return {'value': res}
    

    @api.one
    @api.depends('x_department')
    def dept_exist(self):
        if self.x_department:
            self.dept_check = 1
        elif self.doc_location:
	           self.loc_check = 1
        else:
            self.dept_check = 0
            self.loc_check = 0

    @api.one
    @api.depends('file_id')
    def get_resource_id(self):
        get_res =self.env['document.folder']
        str_res = get_res.search([('name','=',self.file_id.name)])
        self.res_name = str_res.id
         
    @api.one
    @api.depends('name')
    def get_contact_type(self):
        dumm = 0
        if self.name.company_type == "company":
            dumm = 1
        self.x_dummy = dumm
        
    @api.one
    @api.depends('name','x_description','x_date')
    def _compute_doc_subject(self):
        if self.name.name == False:
            title1 = 'no description'
        else:
            title1 = self.name.name
        if self.x_description == False:
            title2 = 'no description'
        else:
            title2 = self.x_description
        if self.x_date == False:
            title3 = 'no description'
        else:
            title3 = self.x_date
        sub_name = title1.replace(" ", "") + "/" + title2[:10].replace(" ", "") + "/" + title3
        self.sub_name = sub_name
        
class main_customer_line(models.Model):
    _name = 'document.customer.line'
    _description = 'This in document customer line'
    customer_id = fields.Many2one('document.customer', string='Customer Reference')
    x_date = fields.Date('Date')
    x_notes = fields.Char('Additional notes')
    x_filename = fields.Char('Image Filename')
    x_fileget = fields.Binary('File Name')
    
class outgoing_files(models.Model):
    _name = 'document.outgoing'
    _description = 'Incoming Document Customer Module'
    _inherit = 'mail.thread'
    _rec_name = 'outsub_name'
    description = 'Hold Outgoing Document Details'
    name =  fields.Text('Subject')
    con_name = fields.Many2one('res.partner', string='Company')
    date = fields.Date(default=fields.Date.today(), string='Date')
    signed = fields.Many2one('res.users', String='Signed by')
    summary = fields.Text('Summary')
    cont_amt = fields.Float('Contract Amount')
    cont_terms = fields.Text('Contract Terms')
    pic_date = fields.Date('Pickup Date')
    out_file = fields.Binary('File Name')
    out_filename = fields.Char('Main FileName')
    outgoing_line_ids = fields.One2many('outgoing.files.line', 'outgoing_id', string='Outgoing File Details')
    xref_nos = fields.Many2one('outdoc.ref.no', string='Reference')
    xx_dummy = fields.Integer(compute='get_outcontact_type')
    xx_contact = fields.Many2one('res.partner', string='Contact Person')
    outsub_name = fields.Char(compute='_compute_outdoc_subject', string='Document Name')
    tt_department = fields.Many2one('hr.department', string='Department')
    
    
    @api.one
    @api.depends('con_name')
    def get_outcontact_type(self):
        dumm = 0
        if self.con_name.company_type == "company":
            dumm = 1
        self.xx_dummy = dumm
        
    @api.one
    @api.depends('name','con_name','date')
    def _compute_outdoc_subject(self):
        for record in self:
            if record.con_name.name == False:
                title1 = 'no description'
            else:
                title1 = record.con_name.name
            if record.name == False:
                title2 = 'no description'
            else:
                title2 = record.name
            if record.date == False:
                title3 = 'no description'
            else:
                title3 = record.date
            print title1
            print title2
            print title3
            outsub_name = title1.replace(" ", "") + "/" + title2[:10].replace(" ", "") + "/" + title3
        self.outsub_name = outsub_name
        
        

class ougoing_files_line(models.Model):
    _name = 'outgoing.files.line'
    outgoing_id = fields.Many2one('document.outgoing', string='Ougoing Reference')
    xx_date = fields.Date('Date')
    xx_notes = fields.Char('Additional notes')
    xx_filename = fields.Char('Image Filename')
    xx_fileget = fields.Binary('File Name')

class customer_file_respartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    file_log = fields.Integer(compute='file_count', string='Files')
    outfile_log = fields.Integer(compute='out_file_count')
    x_dept_res = fields.Many2one('hr.department', string='Department')
    
    @api.one
    def file_count(self):
        file_count =  self.env['document.customer']
        file_logger = file_count.search([('name','=',self.name)])
        self.file_log = len(file_logger)
                
    @api.one
    def out_file_count(self):
        outfile_count =  self.env['document.outgoing']
        outfile_logger = outfile_count.search([('con_name','=',self.name)])
        self.outfile_log = len(outfile_logger)    
            
