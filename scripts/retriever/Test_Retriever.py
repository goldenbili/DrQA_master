

import prettytable
from drqa import retriever








if __name__ == '__main__':
    '''
    db_class = retriever.DocDB('/home/willychang/Project/python/DrQA-master/test123.db')
    doucements = db_class.get_doc_text('Test123')
    print(doucements)
    '''

    DOC2IDX = None
    documents = []
    db_class = retriever.get_class('sqlite')
    with db_class('/home/willychang/Project/python/DrQA-master/test123.db') as doc_db:
        doc_ids = doc_db.get_doc_ids()
        for ids in doc_ids:
            documents.append(doc_db.get_doc_text(ids))
    DOC2IDX = {doc_id: i for i, doc_id in enumerate(doc_ids)}
    print(DOC2IDX)

