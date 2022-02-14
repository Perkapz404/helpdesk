import frappe

@frappe.whitelist(allow_guest=True)
def get_all():
    all_agents = frappe.get_all("Agent", fields=['name', 'agent_name'])
    return all_agents