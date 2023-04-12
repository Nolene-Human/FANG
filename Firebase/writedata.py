

#write user to database
doc_ref = database.collection(u"users").document(auth.current_user)
doc_ref.set({u'Network Name':FAN_name,
       u'Email':email})