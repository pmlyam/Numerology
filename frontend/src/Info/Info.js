import React from "react";
import "./Info.css";
import { InfoItem } from "./InfoItem/InfoItem";

export function Info({ props }) {
  return (
    <section className="info">
      <h2 className="info__heading">Основные качества</h2>
      <div className="info__containers">
        {props[0]?.map((item) => (
          <InfoItem props={item} key={item.name} />
        ))}
      </div>
      <h2 className="info__heading">Дополнительные качества</h2>
      <div className="info__containers">
        {props[1]?.map((item) => (
          <InfoItem props={item} key={item.name} />
        ))}
      </div>
    </section>
  );
}
