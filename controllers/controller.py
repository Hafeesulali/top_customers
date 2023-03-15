import itertools

from odoo import http
from odoo.http import request


class TopCustomers(http.Controller):
    @http.route(['/top_ten_customer'], type="json", auth="public")
    def top_ten(self):
        sale_partner_list = [rec.partner_id.id for rec in request.env["sale.order"].search([])]
        partner_ids = request.env["res.partner"].search([])
        top_dict = {}
        new_list = []
        for i in partner_ids:
            if i.id in sale_partner_list:
                top_dict.update({
                    i: sale_partner_list.count(i.id)

                })
        sort = dict(sorted(top_dict.items(), key=lambda item: item[1], reverse=True))
        limited = dict(itertools.islice(sort.items(), 10))
        for i in limited:
            new_list.append([
                i.name, i.id
            ])
        chunk_size = 4
        top_cust = [new_list[i:i + chunk_size] for i in range(0, len(new_list), chunk_size)]
        return top_cust


class CustomerDetails(http.Controller):
    @http.route(['/top_customers/customer_details'], type="http", auth="public", csrf=False, website=True)
    def customer_details(self, **post):
        customer = request.env['res.partner'].sudo().browse(int(post.get("customer")))
        customer_dict = {
            "customers": customer
        }
        print(customer_dict)
        return request.render('top_customers.customer_details', customer_dict)
