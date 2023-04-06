import React from "react";
import "./Decoding.css";
import Pythagoras from "../images/Pythagoras Picture.png";
import numbers from "../images/numbers.png";

export function Decoding() {
  return (
    <section className="decoding">
      <h2 className="decoding__title">
        Психоматрица Пифагора: как просчитать свою судьбу по&nbsp;дате рождения
      </h2>
      <div className="decoding__container">
        <div className="decoding__text-container">
          <p className="decoding__text">
            Психоматрица Пифагора, как и нумерология, имеет египетские корни, и
            была разработана жрецами. Пифагор же упростил систему, больше
            основываясь на математических вычислениях по дате рождения, сделав
            ее доступной и понятной для каждого.
          </p>
          <p className="decoding__text">
            По методике квадрата Пифагора каждая цифра занимает свою клетку, и
            отвечает за определенные черты характера. Система определения
            проста: чем больше одинаковых цифр в одной клетке, тем сильнее
            проявляется или развита конкретная черта характера.
          </p>
          <p className="decoding__text">
            Карту Пифагора также часто называют картой судьбы. Но то, что
            говорит карта — это не приговор, а только то, что дается при
            рождении, с чем мы пришли в этот мир, и на что лучше опираться. Это
            база, а уже использовать ее или нет — личный выбор каждого.
          </p>
          <p className="decoding__text">
            Считается, что Душа, приходя в этот мир, сама выбирает место, время,
            условия, чтобы проработать какие-либо уроки. По матрице Пифагора
            можно отследить, что стоит сделать, если у вас недостаточно цифр,
            определяющих таланты или позитивные знания. По мере перерождения
            Души и прохождения уроков матрица становится более наполненной.
          </p>
        </div>
        <div className="decoding__image">
          <img alt="Pythagoras" src={Pythagoras}></img>
        </div>
      </div>
      <h2 className="decoding__title">Как рассчитать матрицу Пифагора</h2>
      <div className="decoding__container">
        <div className="decoding__grid-container">
          <div className="decoding__grid-item">
            <p className="decoding__grid-heading">11</p>
            <p className="decoding__grid-subheading">Характер</p>
          </div>
          <div className="decoding__grid-item">
            <p className="decoding__grid-heading">4</p>
            <p className="decoding__grid-subheading">Здоровье</p>
          </div>
          <div className="decoding__grid-item">
            <p className="decoding__grid-heading">-</p>
            <p className="decoding__grid-subheading">Удача</p>
          </div>
          <div className="decoding__grid-item">
            <p className="decoding__grid-heading">222</p>
            <p className="decoding__grid-subheading">Энергия</p>
          </div>
          <div className="decoding__grid-item">
            <p className="decoding__grid-heading">-</p>
            <p className="decoding__grid-subheading">Логика</p>
          </div>
          <div className="decoding__grid-item">
            <p className="decoding__grid-heading">8</p>
            <p className="decoding__grid-subheading">Долг</p>
          </div>
          <div className="decoding__grid-item">
            <p className="decoding__grid-heading">3</p>
            <p className="decoding__grid-subheading">Интерес</p>
          </div>
          <div className="decoding__grid-item">
            <p className="decoding__grid-heading">66</p>
            <p className="decoding__grid-subheading">Труд</p>
          </div>
          <div className="decoding__grid-item">
            <p className="decoding__grid-heading">9</p>
            <p className="decoding__grid-subheading">Память</p>
          </div>
        </div>
        <div className="decoding__text-container">
          <p className="decoding__text">
            Для примера возьмем 20 июля 1996 года
          </p>
          <ol className="decoding__items">
            <li className="decoding__item">
              Первое число: складываем все цифры без нулей 2+3+1+9+8+1 = 24.
            </li>
            <li className="decoding__item">
              Второе число: складываются цифры первого 2+4 = 6.
            </li>
            <li className="decoding__item">
              Третье число: первую цифру из общей даты рождения умножаем на 2
              (2*2=4). Вычитаем получившуюся цифру из суммы пункта два
              (24-4=20).
            </li>
            <li className="decoding__item">
              Четвертое число: складываем цифры третьего числа 4+2 (ноль не
              считаем) = 6.
            </li>
          </ol>
          <p className="decoding__text">
            Получились все необходимые цифры для внесениях их в квадрат. Выделим
            их повторно:
          </p>
          <ul className="decoding__points">
            <li className="decoding__point">Основные числа: 2 3 1981</li>
            <li className="decoding__point">Дополнительные числа: 24 6 2 6</li>
          </ul>
          <p className="decoding__text">
            Теперь считаем, сколько у нас получилось единиц, двоек и так далее,
            и вносим их в таблицу. В блоке 1 получится две единицы. В блоке 2 —
            три двойки, в блоке 3 — одна тройка, в блоке 4 — одна четверка, в
            блоке пять — пусто, в блоке 6 — две шестерки, в блоке 7 — пусто, в
            блоке 8 — одна восьмерка, в блоке 9 — одна девятка.
          </p>
        </div>
      </div>
      <h2 className="decoding__title">Значения цифр</h2>
      <div className="decoding__mean-container">
        <div className="decoding__text-container">
          <p className="decoding__text">
            1 — характер человека, его способность отстаивать свои интересы, а
            также степень желания властвовать.
          </p>
          <p className="decoding__text">
            2 — энергия. Это активность в социуме, в семье, на работе, в
            обществе.
          </p>
          <p className="decoding__text">
            3 — познавательный потенциал, аналитические способности, склонность
            к наукам.
          </p>
          <p className="decoding__text">4 — здоровье</p>
          <p className="decoding__text">
            5 — это логика и интуиция. Анализ, планирование, правильные выводы.
          </p>
          <p className="decoding__text">
            6 — это трудолюбие, склонность к физическому труду.
          </p>
          <p className="decoding__text">7 — везение и удача.</p>
          <p className="decoding__text">
            8 — это чувство долга по отношению к близким людям
          </p>
          <p className="decoding__text">9 — ум, память, интуиция, яснознание</p>
        </div>
        <img alt="numbers" src={numbers} className="decoding__numbers"></img>
      </div>
    </section>
  );
}
