{'name': 'Top 10 Customers',
 'installable': True,
 'auto_install': False,
 'version': '16.0.1.0.0',
 'depends': ['base', 'website'],
 "data": [
     'views/customer_views.xml',
     'views/snippet_inherit_view.xml',
     'views/q_web.xml',
 ],
 'assets': {
     'web.assets_frontend': [
         '/top_customers/static/src/js/dynamic_snippet.js',
         '/top_customers/static/src/xml/snippet_view.xml',
         '/top_customers/static/src/css/snippet.scss',
     ]}

 }
