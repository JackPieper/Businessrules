import psycopg2

conn = psycopg2.connect(host="localhost", database="op=op voordeelshop", user="postgres", password="PostGres")
cursor = conn.cursor()

cursor.execute("""drop table if exists content_rec;
                drop table if exists collab_rec;
                
                Create table content_rec (
                    profileprofileid Foreign key references profile(profileid)
                    productproductid foreign key references product(productid)
                );
                
                Create table collab_rec (
                    profileprofileid Foreign key references profile(profileid)
                    productproductid foreign key references product(productid)
                );
                
                insert into content_rec(profileprofileid, productproductid) 
                values select profile.profileid, product.productid from profile, product 
                inner join content_rec on content_rec.profileprofileid = profile.profileid
                inner join content_rec on content_rec.productproductid = product.productid
                where product.category = select product.category from viewed_before
                inner join product, profile on viewed_before.profileprofileid = profile.profileid, product.productid = viewed_before.productproductid;
                
                insert into collab_rec(profileprofileid, productproductid)
                values select content_rec.profileprofileid, content_rec.productproductid from content_rec
                where content_rec.profileprofileid = viewed_before.profileprofileid where viewed_before.productproductid = content_rec.productid"""")
conn.commit()
# Tables worden hier aangemaakt waarnain de content filter tabel de waardes worden gezet waar de category hetzelfde is als de category van producten uit de viewed_before
# Daarna wordt voor de collaborative filter gekeken naar welk account dezelfde viewed_before heeft en word dan de lijst van de content filter van dat account in de collaborative filter van de user gezet