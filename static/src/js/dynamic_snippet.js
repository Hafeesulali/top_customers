odoo.define('top_customers.dynamic', function (require) {
//console.log('ssssssssssssssss')
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   var core=require("web.core")
   var Qweb=core.qweb
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_snippet_blog',
       start: function () {
           rpc.query({
               route: '/top_ten_customer',
               params: {},
           }).then(function (result) {
           result[0].set_active=true;
               $(".qweb_top").append(Qweb.render('top_customers.snippet',{result}));
           });
       },
   });

   PublicWidget.registry.dynamic_snippet_blog = Dynamic;
   return Dynamic;
});