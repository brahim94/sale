from odoo import models, fields, api

class tech_sale_order(models.Model): 
    _inherit = "sale.order"

    #payment_methode_ids = fields.Many2many('payement.methode', string='Mode de paiement')
    
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        self.centre = self.partner_id.city
        self.province = self.partner_id.state_id
        self.payment_way_id = self.partner_id.payment_methode_id

    centre = fields.Char('Centre')
    province = fields.Many2one('res.country.state', string="Province")
    payment_way_id = fields.Many2many('payement.methode', string='Mode de paiement')

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


    
    


        # if not self.partner_id:
        #     self.update({
        #         'payment_methode_ids': False,
        #     })
        #     return
        
        # values = {
        # 'payment_methode_ids': False,self.partner_id.property_payment_term_id and self.partner_id.property_payment_term_id.id or False,
    