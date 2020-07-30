from odoo.exceptions import UserError
from odoo import fields, api, models, _

class tech_sale_order(models.Model): 
    _inherit = "sale.order"

    #payment_methode_ids = fields.Many2many('payement.methode', string='Mode de paiement')
    
    @api.onchange('partner_id')
<<<<<<< HEAD
    def onchange_partner_id(self):
        self.centre = self.partner_id.city
        self.province = self.partner_id.state_id
        self.payment_way_id = self.partner_id.payment_methode_id

    centre = fields.Char('Centre')
    province = fields.Many2one('res.country.state', string="Province")
    payment_way_id = fields.Many2many('payement.methode', string='Mode de paiement')
=======
    def onchange_partner_id2(self):
        self.centre = self.partner_id.city
        self.province = self.partner_id.state_id
        self.payment_way_id = self.partner_id.payment_methode_id
    
    @api.onchange('partner_id')
    def onchange_partner_id3(self):
        for rec in self:
            return {'domain': {'payment_methode_id': [('partner_id', '=', rec.partner_id.id)]}}

    centre = fields.Char('Centre')
    province = fields.Many2one('res.country.state', string="Province")
    payment_way_id = fields.Many2one('payement.methode', string='Mode de paiement')
>>>>>>> displaying only qualified products

class tech_report_invoice(models.Model):
    _inherit = "account.move"

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        self.centre = self.partner_id.city
        self.province = self.partner_id.state_id
        self.cin_id = self.partner_id.cin
        self.ice_id = self.partner_id.ice
        self.country_ids = self.partner_id.country_id
        self.adress_ids = self.partner_id.street
        self.payment_way_ids = self.partner_id.payment_methode_id
    
    adress_ids = fields.Char('Rue')
    country_ids = fields.Many2many('res.country', string='Pays')
    ice_id = fields.Char('ICE')
    cin_id = fields.Char('CIN')
    centre = fields.Char('Centre')
    province = fields.Many2one('res.country.state', string="Province")
    payment_way_ids = fields.Many2many('payement.methode', string='Mode de paiement')

    # def get_amount_letter(self):
    #     amount = self.currency_id.amount_to_text(self.amount_total)
    #     return amount
    
    @api.depends('amount_total')
    def get_amount_in_words(self):
        amount_in_words = self.currency_id.amount_to_text(self.amount_total)
        return amount_in_words

    # @api.depends('amount_total', 'currency_id')
    # def compute_text(self):
    #     return amount_to_text_fr(self.amount_total, self.currency_id.symbol)

    
# class account_invoice(report_sxw.rml_parse):
#     def __init__(self, cr, uid, name, context):
#     super(account_invoice, self).__init__(cr, uid, name, context=context)
#     self.localcontext.update({
#        'time': time,
#        'amount_to_text_fr':amount_to_text_fr,


    


        # if not self.partner_id:
        #     self.update({
        #         'payment_methode_ids': False,
        #     })
        #     return
        
        # values = {
        # 'payment_methode_ids': False,self.partner_id.property_payment_term_id and self.partner_id.property_payment_term_id.id or False,
<<<<<<< HEAD
    
=======
    
>>>>>>> displaying only qualified products
