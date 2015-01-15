    result=None
    p0=head
    p1=head

    if (head.val !=(head.next).val):
        result=head

    while(p0.next!=None):
        # the last two nodes
        if (p0.next.next==None):
            if (p0.val == p0.next.val):
                if (p0!=p1):
                    p1.next =None
            else:
                p1.next = p0.next
                p1 = p1.next
                # if result not initialized
                if (result==None):
                    result =p1


        # in the middle                
        elif (p0.val < p0.next.val):
            if (p0.next.val<p0.next.next.val):
                p1.next = p0.next
                p1 = p1.next
                # if result not initialized
                if(result==None):
                    result = p1

        p0=p0.next

    return result