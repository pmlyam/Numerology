import React from "react";
import "./Footer.css";

export function Footer({ props }) {
  return (
    <footer className="footer">
      <a href="#form" className="footer__button">
        {props.length ? "Рассчитать другую дату" : "Рассчитать дату"}
      </a>
      <div className="footer__container">
        <p className="footer__text">2023 Ness Numerology</p>
        <p className="footer__text">
          На сайте содержится информация, предназначенная для лиц старше 18 лет.
        </p>
        <a href="mailto:ness.numerology@gmail.com" className="footer__link">
          ness.numerology@gmail.com
        </a>
      </div>
    </footer>
  );
}
