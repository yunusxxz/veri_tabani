# config.py: 'To-Do List' projesi için veritabanı bağlantı ayarlarını içeren dosya.

from sqlalchemy import create_engine  # SQLAlchemy'nin veritabanı motorunu oluşturmak için kullanılan modül.
from sqlalchemy.orm import sessionmaker, declarative_base  # ORM oturumu ve veritabanı modelleri için temel sınıf modülleri.

# SQLite için bağlantı cümlesi:
CONNECTION_STRING = "sqlite:///data.db"
# Bu, veritabanı bağlantı adresidir. 'sqlite' ifadesi SQLite veritabanını belirtiyor ve
# 'data.db' dosyasına bağlanılacağını ifade ediyor. Bağlantı adresi 'sqlite:///data.db' şeklindedir.
# 'sqlite:///' üç eğik çizgiyle belirtilen dosya yolunu ifade eder.

# Veritabanı motoru oluşturuluyor.
engine = create_engine(CONNECTION_STRING, echo=True)
# create_engine, veritabanı ile bağlantıyı sağlayan ve veri alışverişini yöneten bir motor (engine) oluşturur.
# echo=True ile, SQLAlchemy tarafından oluşturulan SQL komutlarının konsolda görünmesi sağlanır;
# bu, geliştirme sırasında komutların incelenebilmesi için faydalıdır.

# Oturum sınıfı oluşturuluyor.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# sessionmaker, veritabanıyla etkileşim için bir oturum (session) sınıfı oluşturur.
# 'autocommit=False' ile işlemler otomatik olarak veritabanına yazılmaz, işlem sonunda
# manuel olarak onaylanması (commit) gerekir.
# 'autoflush=False' ile veri değişiklikleri otomatik olarak veritabanına yansıtılmaz, bu da performansı artırabilir.
# 'bind=engine' ile bu oturum sınıfı, 'engine' nesnesine bağlanır.

# Veritabanı modelleri için temel sınıf oluşturuluyor.
Base = declarative_base()
# declarative_base, veritabanı tablosu olarak kullanılacak sınıfların temelini oluşturan bir nesne yaratır.
# Bu sayede, veritabanı tabloları gibi davranacak sınıflar kolayca tanımlanabilir.
