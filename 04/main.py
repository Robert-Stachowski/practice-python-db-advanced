from db import Session, engine
from models import Measurment, Base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text, func


def main():
    Base.metadata.create_all(engine)

    with Session() as session:
        try:
            heidelberg_measurements = [
            Measurment(
                device_name="Heidelberg CoreMaker H200",
                value=182.1,
                timestamp=text("datetime('now', '-5 day')")
            ),
            Measurment(
                device_name="Heidelberg CoreMaker H200",
                value=182.8,
                timestamp=text("datetime('now', '-4 day')")
            ),
            Measurment(
                device_name="Heidelberg CoreMaker H200",
                value=183.4,
                timestamp=text("datetime('now', '-3 day')")
            ),
            Measurment(
                device_name="Heidelberg CoreMaker H200",
                value=184.0,
                timestamp=text("datetime('now', '-2 day')")
            ),
            Measurment(
                device_name="Heidelberg CoreMaker H200",
                value=183.6,
                timestamp=text("datetime('now', '-1 day')")
            ),
            ]

            # --- Laempe L40
            laempe_measurements = [
                Measurment(
                    device_name="Laempe L40",
                    value=147.9,
                    timestamp=text("datetime('now', '-3 day')")
                ),
                Measurment(
                    device_name="Laempe L40",
                    value=148.4,
                    timestamp=text("datetime('now', '-2 day')")
                ),
                Measurment(
                    device_name="Laempe L40",
                    value=149.1,
                    timestamp=text("datetime('now', '-1 day')")
                ),
            ]

            # --- Omega Sinto FBO-II
            omega_measurements = [
                Measurment(
                    device_name="Omega Sinto FBO-II",
                    value=36.2,
                    timestamp=text("datetime('now', '-4 day')")
                ),
                Measurment(
                    device_name="Omega Sinto FBO-II",
                    value=36.8,
                    timestamp=text("datetime('now', '-2 day')")
                ),
                Measurment(
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


            results = session.query(Measurment.device_name, func.count(Measurment.id).label("count")).group_by(Measurment.device_name).all()
            for result in results:
                print(f"Maszyna:  {result.device_name},  Ilość prób:  {result.count}")

            print("\n")

            avg_results = session.query(Measurment.device_name, func.round(func.avg(Measurment.value),2).label("avg")).group_by(Measurment.device_name).all()
            for result in avg_results:
                print(f"Maszyna:  {result.device_name},  Średnia z prób:  {result.avg}")


        except SQLAlchemyError as e:
            print("SQLAlchemyError:", e)
            session.rollback()

if __name__ == "__main__":
    main()
