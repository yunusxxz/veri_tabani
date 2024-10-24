from sqlalchemy import Column, Integer, String, Boolean
# SQLAlchemy'den sütun türleri için gerekli modülleri içe aktarıyoruz.
from config import Base
# Daha önce tanımladığımız temel sınıfı (Base) kullanarak veritabanı tabloları tanımlamak için içe aktarıyoruz.


# Todo sınıfı, 'todos' adlı bir veritabanı tablosunu temsil eder.
class Todo(Base):
    __tablename__ = 'todos'  # Tablo adı 'todos' olarak ayarlanır. Bu, SQLAlchemy'nin veritabanında bu ismi kullanmasını sağlar.

    # Sütun tanımlamaları:
    id = Column(Integer, primary_key=True, index=True)
    # 'id' sütunu, her görevi benzersiz şekilde tanımlayan birincil anahtardır (primary key).
    # Integer türünde olup veritabanında hızlı aramalar için bir dizin (index) oluşturulur.

    title = Column(String)
    # 'title' sütunu, her görev için kısa bir başlık içerir. String türündedir ve varsayılan olarak boş bırakılamaz.

    description = Column(String, nullable=True)
    # 'description' sütunu, görevin açıklamasını tutar. String türündedir ve boş bırakılabilir (nullable=True).

    completed = Column(Boolean, default=False)
    # 'completed' sütunu, görevin tamamlanıp tamamlanmadığını gösterir. Boolean türündedir.
    # Varsayılan olarak False (tamamlanmamış) olarak ayarlanmıştır.
