from db import SessionLocal, engine
from models import Measurement, Base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from datetime import datetime, timedelta



def clear_table(session):
    session.query(Measurement).delete()
    session.commit()

def main():
    Base.metadata.create_all(engine)

    with SessionLocal() as session:
        clear_table(session)
        try:
            now = datetime.utcnow()

            heidelberg_measurements = [
                Measurement(device_name="Heidelberg CoreMaker H200", value=182.1, timestamp=now - timedelta(days=5)),
                Measurement(device_name="Heidelberg CoreMaker H200", value=182.8, timestamp=now - timedelta(days=4)),
                Measurement(device_name="Heidelberg CoreMaker H200", value=183.4, timestamp=now - timedelta(days=3)),
                Measurement(device_name="Heidelberg CoreMaker H200", value=184.0, timestamp=now - timedelta(days=2)),
                Measurement(device_name="Heidelberg CoreMaker H200", value=183.6, timestamp=now - timedelta(days=1)),
            ]

            laempe_measurements = [
                Measurement(device_name="Laempe L40", value=147.9, timestamp=now - timedelta(days=3)),
                Measurement(device_name="Laempe L40", value=148.4, timestamp=now - timedelta(days=2)),
                Measurement(device_name="Laempe L40", value=149.1, timestamp=now - timedelta(days=1)),
            ]

            omega_measurements = [
                Measurement(device_name="Omega Sinto FBO-II", value=36.2, timestamp=now - timedelta(days=4)),
                Measurement(device_name="Omega Sinto FBO-II", value=36.8, timestamp=now - timedelta(days=2)),
                Measurement(device_name="Omega Sinto FBO-II", value=37.1, timestamp=now),
            ]

            session.add_all(
                heidelberg_measurements
                + laempe_measurements
                + omega_measurements
            )
            session.commit()
            print("Załadowano dane poprawnie\n")


            results = session.query(
                Measurement.device_name,
                func.count(Measurement.id).label("count"),
                func.round(func.avg(Measurement.value), 2).label("avg"),
            ).group_by(Measurement.device_name).all()

            for result in results:
                print(f"Maszyna: {result.device_name},  Ilość prób: {result.count},  Średnia: {result.avg}")


        except SQLAlchemyError as e:
            print("SQLAlchemyError:", e)
            session.rollback()

if __name__ == "__main__":
    main()
