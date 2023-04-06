import React from "react";
import "./Quote.css";

export function Quote() {
  return (
    <section className="quote">
      <div className="quote__image">
        <div className="quote__container">
          <div className="quote__heading">
            <p className="quote__title">Психоматрица по&nbsp;дате рождения</p>
            <p className="quote__subtitle">(Квадрат Пифагора)</p>
          </div>
          <p className="quote__text">
            Метод позволяет определить по дате рождения типичные черты
            характера, заложенные человеку при рождении
          </p>
        </div>
      </div>

      <div className="quote__arrow" />
    </section>
  );
}
