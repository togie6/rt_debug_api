#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import rt
from keys import api_keys
import logging
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(level=logging.WARN)


ticket_reply_text = """
Line 1 text
Line 2 text
Line 3 text
Line 4 text
Line 5 text
Line 6 text
"""

def create_rt_ticket(requestor: str, queue: str, subject: str, ticket_text: str):
    """Create an RT ticket using the RT API and replies
       to requestor automatically based on arguments.
    
    Parameters:
        requestor: (str): Ticket requestor.
        subject (str): Subject line for the ticket.
        ticket_text: (str):  Text content for the RT ticket reply.

    Returns:
        tid: (str): Ticket ID
    """
    rt_url = api_keys['rt']['url']
    
    rt_user = api_keys['rt']['user']
    
    rt_pass = api_keys['rt']['password']

    req = rt.Rt(rt_url, rt_user, rt_pass, verify_cert=False)
    req.login()
    

    tid = req.create_ticket(
        Queue=queue, 
        Status="open", 
        Subject=subject, 
        Requestors=requestor
        ) 

    req.reply(tid, text=ticket_text)

    req.logout()

     
    return tid




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generates notification if an unpublished MISP event is detected')
    parser.add_argument('queue', type=str, action="store", help='Queue for ticket to be created in')
    parser.add_argument('--subject', '-s', type=str, nargs="?", required=True, default="Test Ticket rt_sig_bug", help='Server to generate a report on')
    parser.add_argument('--requestor', '-r', type=str, nargs="?", default=False, help='Send unpublished events to RT')
    args = vars(parser.parse_args())


    ticket = create_rt_ticket(
        queue=args["queue"],
        requestor=args["requestor"],
        subject=args["subject"],
        ticket_text=ticket_reply_text,
        )

    print("Ticket created: {}".format(str(ticket)))

    print("Ticket data: {}".format(json.dumps(args, indent=1)))

    



