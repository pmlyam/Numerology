import React from "react";
import "./TextContainer.css";

export function TextContainer() {
  return (
    <section className="textContainer">
      <button className="footer__button">Рассчитать другую дату</button>
      <div className="footer__container">
        <p className="footer__text">2023 Ness Numerology</p>
        <p className="footer__text">
          На сайте содержится информация, предназначенная для лиц старше 18 лет.
        </p>
        <a href="mailto:ness.numerology@gmail.com" className="footer__link">
          ness.numerology@gmail.com
        </a>
      </div>
    </section>
  );
}
