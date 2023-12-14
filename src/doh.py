import base64
import requests 
import dns.message
import dns.rdatatype

def Query(server_name):
	DNS_url = 'https://dns.403.online/dns-query?dns='
	req = requests.session() 

	quary_params = {
		'name': server_name,
		'type': 'A',
		'ct': 'application/dns-message',
	}
      
	try:
		query_message = dns.message.make_query(server_name,'A')
		query_wire = query_message.to_wire()
		query_base64 = base64.urlsafe_b64encode(query_wire).decode('utf-8')
		query_base64 = query_base64.replace('=','')         

		query_url = DNS_url + query_base64
		ans = req.get( query_url , params=quary_params , headers={'accept': 'application/dns-message'})
        
		if ans.status_code == 200 and ans.headers.get('content-type') == 'application/dns-message':
			answer_msg = dns.message.from_wire(ans.content)

			resolved_ip = None
			for x in answer_msg.answer:
				if (x.rdtype == dns.rdatatype.A):
					resolved_ip = x[0].address                        
					break
                           
			return resolved_ip
		else:
			return False
	except Exception as e:
		return False