from db import Session, engine
from models import Measurement, Base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text, func



def clear_table(session):
    session.query(Measurement).delete()
    session.commit()

def main():
    Base.metadata.create_all(engine)

    with Session() as session:
        clear_table(session)
        try:
            heidelberg_measurements = [
            Measurement(
                device_name="Heidelberg CoreMaker H200",
                value=182.1,
                timestamp=text("datetime('now', '-5 day')")
            ),
            Measurement(
                device_name="Heidelberg CoreMaker H200",
                value=182.8,
                timestamp=text("datetime('now', '-4 day')")
            ),
            Measurement(
                device_name="Heidelberg CoreMaker H200",
                value=183.4,
                timestamp=text("datetime('now', '-3 day')")
            ),
            Measurement(
                device_name="Heidelberg CoreMaker H200",
                value=184.0,
                timestamp=text("datetime('now', '-2 day')")
            ),
            Measurement(
                device_name="Heidelberg CoreMaker H200",
                value=183.6,
                timestamp=text("datetime('now', '-1 day')")
            ),
            ]

            # --- Laempe L40
            laempe_measurements = [
                Measurement(
                    device_name="Laempe L40",
                    value=147.9,
                    timestamp=text("datetime('now', '-3 day')")
                ),
                Measurement(
                    device_name="Laempe L40",
                    value=148.4,
                    timestamp=text("datetime('now', '-2 day')")
                ),
                Measurement(
                    device_name="Laempe L40",
                    value=149.1,
                    timestamp=text("datetime('now', '-1 day')")
                ),
            ]

            # --- Omega Sinto FBO-II
            omega_measurements = [
                Measurement(
                    device_name="Omega Sinto FBO-II",
                    value=36.2,
                    timestamp=text("datetime('now', '-4 day')")
                ),
                Measurement(
                    device_name="Omega Sinto FBO-II",
                    value=36.8,
                    timestamp=text("datetime('now', '-2 day')")
                ),
                Measurement(
                    device_name="Omega Sinto FBO-II",
                    value=37.1,
                    timestamp=text("datetime('now')")
                ),
            ]

            session.add_all(
                heidelberg_measurements
                + laempe_measurements
                + omega_measurements
            )
            session.commit()
            print("Załadowano dane poprawnie\n")


            results = session.query(Measurement.device_name, func.count(Measurement.id).label("count")).group_by(Measurement.device_name).all()
            for result in results:
                print(f"Maszyna:  {result.device_name},  Ilość prób:  {result.count}")

            print("\n")

            avg_results = session.query(Measurement.device_name, func.round(func.avg(Measurement.value),2).label("avg")).group_by(Measurement.device_name).all()
            for result in avg_results:
                print(f"Maszyna:  {result.device_name},  Średnia z prób:  {result.avg}")


        except SQLAlchemyError as e:
            print("SQLAlchemyError:", e)
            session.rollback()

if __name__ == "__main__":
    main()
