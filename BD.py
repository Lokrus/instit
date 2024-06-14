
import psycopg2 
try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='qwerty123',
        database='baza'
        )
    tables = []
    with connection.cursor() as cu:
        cu.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_CATALOG='baza'")
        tabless=cu.fetchall()
        schet=1 #+
        for i in tabless:
            if i[2][:3]=='pg_' or i[2][:3]=='sql':
                continue
            tables.append(i[2])
        STOLBY={'Animal':['id','species_id','gender_id','color_id','color_symmetry_id','body_length','head_length','hip_length','shin_length','foot_length','description','weigth'], 'Cloud': ['id','name'], 'Color': ['id','name'], 'Color_Symmetry': ['id','name'], 'Employee': ['id','surname','name','middle_name','phone','e-mail','organization_id','post_id'], 'Gender': ['id','name'], 'Group': ['id','name'], 'Group_Employee': ['id','group_id','employee_id'], 'Observation': ['id','date','tima','animal_id','employee_id','route_id','weather_conditions_id','coordinates','description'], 'Organization': ['id','name','address','phone','e-mail','inn'], 'Photo': ['id','animal_id','photo','EXIF'], 'Point':['id','name','coordinates','map','description'], 'Post': ['id','name'], 'Route':['id','name','map','description'], 'Route_Point': ['id','route_id','point_id'], 'Scientific_paper':['id','name','publication','group_actors_id','group_mentors_id','organization_id','year'], 'Scientific_paper_Observation': ['id','scientific_paper_id','observation_id'], 'Species': ['id','family','genus','specie'], 'Weather_conditions': ['id','temperature','air_pressure','wind_id','wind_speed','humidity','cloud_id','weather_event_id'], 'Weather_event': ['id','name'], 'Wind': ['id','name']}
        cu.execute("SELECT * FROM "+'"'+'Animal'+'"')
        anim=cu.fetchall()
        for i in anim:
            print(i)

           
   
   
except Exception as _ex:
    print(_ex)
finally:
    if connection:
        connection.close()
        print('closed')
        
